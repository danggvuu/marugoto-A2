import a2_2Vocab from '../../data/vocab_a2_2_official.json';
import a2_2Kanji from '../../data/kanji_vocab_a2_2_official.json';
import masterVocab from '../../data/master_vocab_enriched.json';
import grammarSource from '../../data/grammar_extracted.json';
import kanjiCharacters from '../../data/kanji_extracted.json';
import examSource from '../../assets/data/de_thi_tong_hop_11_18_data.js?raw';
import { lessonCatalog, type LessonMeta } from './lessonCatalog';
import type { ExamSet, GrammarEntry, KanjiEntry, LessonSummary, QuizQuestion, VocabEntry } from '../types/study';

interface RawVocab {
  jp?: string; kana?: string; kanji?: string; romaji?: string; vi?: string; hv?: string; icon?: string; l?: string;
}
interface RawKanjiWord { word: string; kana: string; mean: string; }
interface RawKanjiCharacter {
  char: string; hv: string; strokes: number; lesson: string; on?: string; kun?: string;
  mnemonic?: string; formula?: string; meaning?: string;
}

const a2_2VocabData = a2_2Vocab as Record<string, RawVocab[]>;
const a2_2KanjiData = a2_2Kanji as Record<string, unknown>;
const masterVocabData = masterVocab as RawVocab[];
const grammarData = grammarSource as GrammarEntry[];
const kanjiCharacterData = kanjiCharacters as RawKanjiCharacter[];
const legacyLessonSources = import.meta.glob('/assets/js/lessons/lesson_*.js', {
  eager: true,
  query: '?raw',
  import: 'default',
}) as Record<string, string>;
const legacyHtmlSources = import.meta.glob('/lessons/Marugoto_*.html', {
  eager: true,
  query: '?raw',
  import: 'default',
}) as Record<string, string>;

function parseLegacyArray(source: string, name: string): unknown[] {
  const match = source.match(new RegExp(`const ${name}\\s*=\\s*(\\[[\\s\\S]*?\\n?\\]);`));
  if (!match) return [];
  try {
    return JSON.parse(match[1]) as unknown[];
  } catch {
    return [];
  }
}

function getLessonSource(meta: LessonMeta): string {
  const file = meta.level === 'A2-2'
    ? `lesson_a2_2_${String(meta.number).padStart(2, '0')}.js`
    : `lesson_${String(meta.number).padStart(2, '0')}.js`;
  return legacyLessonSources[`/assets/js/lessons/${file}`] ?? '';
}

function parseLegacyGrammar(meta: LessonMeta): GrammarEntry[] {
  const file = meta.level === 'A2-2'
    ? `Marugoto_A2_2_Lesson_${meta.number}.html`
    : `Marugoto_A2_Lesson_${meta.number}.html`;
  const html = legacyHtmlSources[`/lessons/${file}`];
  if (!html) return [];
  const document = new DOMParser().parseFromString(html, 'text/html');
  return Array.from(document.querySelectorAll('section[id^="sec-grammar"]')).map((section, index) => {
    const title = section.querySelector('.section-title')?.textContent?.trim() ?? `Mẫu câu ${index + 1}`;
    const formula = section.querySelector('.rule-formula')?.textContent?.trim() ?? '';
    const meaning = section.querySelector('.rule-meaning')?.textContent?.trim()
      ?? Array.from(section.querySelectorAll(':scope > p')).map(node => node.textContent?.trim()).filter(Boolean).join(' ')
      ?? '';
    const examples = Array.from(section.querySelectorAll('.example-item')).map(example => ({
      jp: example.querySelector('.ex-jp')?.textContent?.trim() ?? '',
      vi: example.querySelector('.ex-vi')?.textContent?.trim() ?? '',
    })).filter(example => example.jp && example.vi);
    return {
      id: meta.number * 100 + index,
      level: meta.level,
      lesson: meta.number,
      lessonTitle: meta.title,
      title,
      formula,
      meaning,
      examples,
    };
  });
}

function getKanjiCharacters(word: string, fallback: string) {
  return Array.from(word.matchAll(/[\p{Script=Han}]/gu), ([character]) => {
    const detail = kanjiCharacterData.find(item => item.char === character);
    return {
      character,
      meaning: detail?.meaning ?? fallback,
      vietnamese: detail?.hv ?? '',
      strokes: detail?.strokes ?? 0,
      on: detail?.on ?? '',
      kun: detail?.kun ?? '',
      mnemonic: detail?.mnemonic ?? '',
      formula: detail?.formula ?? '',
    };
  });
}

export const vocabA2_2: VocabEntry[] = Object.entries(a2_2VocabData).flatMap(([key, words]) => {
  const lesson = Number(key.replace('lesson_', ''));
  return words.map((word, index) => ({
    id: `a2-2-${lesson}-${index + 1}`,
    lesson,
    level: 'A2-2' as const,
    jp: word.jp ?? '',
    kana: word.kana ?? word.jp ?? '',
    kanji: word.kanji ?? word.jp ?? '',
    romaji: word.romaji ?? '',
    meaning: word.vi ?? '',
    hv: word.hv,
    icon: word.icon,
  }));
});

export const kanjiA2_2: KanjiEntry[] = Object.entries(a2_2KanjiData)
  .filter(([key, value]) => key.startsWith('lesson_') && Array.isArray(value))
  .flatMap(([key, entries]) => {
    const lesson = Number(key.replace('lesson_', ''));
    return (entries as RawKanjiWord[]).map((entry, index) => ({
      id: `a2-2-kanji-${lesson}-${index + 1}`,
      lesson,
      level: 'A2-2' as const,
      word: entry.word,
      kana: entry.kana,
      meaning: entry.mean,
      characters: getKanjiCharacters(entry.word, entry.mean),
    }));
  });

function kanjiFromA2_1(meta: LessonMeta): KanjiEntry[] {
  const cards = kanjiCharacterData.filter(entry => entry.lesson === `L${meta.number}`);
  return cards.map((entry, index) => ({
    id: `a2-1-${meta.number}-kanji-${index + 1}`,
    lesson: meta.number,
    level: 'A2-1' as const,
    word: entry.char,
    kana: entry.kun ?? entry.on ?? '',
    meaning: entry.meaning ?? entry.hv,
    characters: [{
      character: entry.char,
      meaning: entry.meaning ?? entry.hv,
      vietnamese: entry.hv,
      strokes: entry.strokes,
      on: entry.on ?? '',
      kun: entry.kun ?? '',
      mnemonic: entry.mnemonic ?? '',
      formula: entry.formula ?? '',
    }],
  }));
}

export const kanjiA2_1: KanjiEntry[] = lessonCatalog.filter(item => item.level === 'A2-1').flatMap(kanjiFromA2_1);

export const allKanji = [...kanjiA2_1, ...kanjiA2_2];
export const grammarEntries = grammarData.map(entry => ({ ...entry, category: entry.tag ?? entry.category }));

const rawExamData = JSON.parse(examSource.slice(examSource.indexOf('=') + 1).replace(/;\s*$/, '')) as ExamSet[];
export const examSets = rawExamData;

function mapA2_1Vocab(meta: LessonMeta): VocabEntry[] {
  return masterVocabData.filter(entry => entry.l === `A2-${meta.number}`).map((entry, index) => ({
    id: `a2-1-${meta.number}-${index + 1}`,
    lesson: meta.number,
    level: 'A2-1' as const,
    jp: entry.jp ?? entry.kanji ?? '',
    kana: entry.kana ?? '',
    kanji: entry.kanji ?? '',
    romaji: entry.romaji ?? '',
    meaning: entry.vi ?? '',
    hv: entry.hv,
  }));
}

export const lessonSummaries: LessonSummary[] = lessonCatalog.map(meta => {
  const source = getLessonSource(meta);
  const legacyQuiz = parseLegacyArray(source, 'QUIZ_DATA');
  const quiz = (legacyQuiz.length ? legacyQuiz : parseLegacyArray(source, 'QUIZ_QUESTIONS')) as QuizQuestion[];
  const vocab = meta.level === 'A2-2'
    ? vocabA2_2.filter(entry => entry.lesson === meta.number)
    : mapA2_1Vocab(meta);
  const kanji = (meta.level === 'A2-2' ? kanjiA2_2 : kanjiA2_1).filter(entry => entry.lesson === meta.number);
  const authoredGrammar = parseLegacyGrammar(meta);
  const grammar = authoredGrammar.length ? authoredGrammar : grammarData.filter(entry => entry.level === meta.level && entry.lesson === meta.number);
  return {
    ...meta,
    vocab,
    grammar,
    kanji,
    quiz,
  };
});

export function getLesson(level: string, lesson: number): LessonSummary | undefined {
  return lessonSummaries.find(item => item.level.toLowerCase() === level.toLowerCase() && item.number === lesson);
}

export const a2_1VocabularyTotal = lessonSummaries.filter(lesson => lesson.level === 'A2-1').reduce((total, lesson) => total + lesson.vocab.length, 0);
export const a2_2VocabularyTotal = vocabA2_2.length;
