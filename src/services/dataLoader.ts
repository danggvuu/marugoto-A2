import a2_2Vocab from '../../data/vocab_a2_2_official.json';
import a2_2Kanji from '../../data/kanji_vocab_a2_2_official.json';
import masterVocab from '../../data/master_vocab_enriched.json';
import grammarSource from '../../data/grammar_extracted.json';
import kanjiA2_1Words from '../../data/kanji_vocab_11_18.json';
import kanjiCharacters from '../../data/kanji_extracted.json';
import examSource from '../../assets/data/de_thi_tong_hop_11_18_data.js?raw';
import mini1114Source from '../../assets/data/mini_11_14_data.js?raw';
import mini1518Source from '../../assets/data/mini_15_18_data.js?raw';
import { lessonCatalog, type LessonMeta } from './lessonCatalog';
import type { ExamItem, ExamSet, GrammarEntry, KanjiEntry, LessonSummary, QuizQuestion, VocabEntry } from '../types/study';

interface RawVocab {
  jp?: string; kana?: string; kanji?: string; romaji?: string; vi?: string; hv?: string; icon?: string; l?: string;
}
interface RawKanjiWord { word: string; kana: string; mean: string; }
interface RawA21KanjiWord { lesson: number; kanji: string; kana: string; vi: string; }
interface RawKanjiCharacter {
  char: string; hv: string; strokes: number; on?: string; kun?: string;
  mnemonic?: string; formula?: string; meaning?: string;
}
interface LegacyLessonArrays {
  VOCAB_DATA: Array<Record<string, unknown>>;
  VERB_DATA: Array<Record<string, unknown>>;
  QUIZ_DATA: QuizQuestion[];
}

const a2_2VocabData = a2_2Vocab as Record<string, RawVocab[]>;
const a2_2KanjiData = a2_2Kanji as Record<string, unknown>;
const masterVocabData = masterVocab as RawVocab[];
const grammarData = grammarSource as GrammarEntry[];
const kanjiCharacterData = kanjiCharacters as RawKanjiCharacter[];
const kanjiA21WordData = kanjiA2_1Words as RawA21KanjiWord[];
const legacyLessonSources = import.meta.glob('/assets/js/lessons/lesson_*.js', {
  eager: true,
  query: '?raw',
  import: 'default',
}) as Record<string, string>;
const legacyHtmlSources = import.meta.glob('/legacy_html/lessons/Marugoto_*.html', {
  eager: true,
  query: '?raw',
  import: 'default',
}) as Record<string, string>;

function parseLegacyArray(source: string, name: string): unknown[] {
  const match = source.match(new RegExp(`(?:const|let|var) ${name}\\s*=\\s*(\\[[\\s\\S]*?\\]);`));
  if (!match) return [];
  try {
    return JSON.parse(match[1]) as unknown[];
  } catch {
    try {
      return Function(`"use strict"; return (${match[1]});`)() as unknown[];
    } catch {
      return [];
    }
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
  const html = legacyHtmlSources[`/legacy_html/lessons/${file}`];
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

export const kanjiA2_1: KanjiEntry[] = kanjiA21WordData.map((entry, index) => ({
  id: `a2-1-${entry.lesson}-kanji-word-${index + 1}`,
  lesson: entry.lesson,
  level: 'A2-1' as const,
  word: entry.kanji,
  kana: entry.kana,
  meaning: entry.vi,
  characters: getKanjiCharacters(entry.kanji, entry.vi),
}));

export const allKanji = [...kanjiA2_1, ...kanjiA2_2];
export const grammarEntries = grammarData.map(entry => ({ ...entry, category: entry.tag ?? entry.category }));

function parseSourceObject(source: string): Record<string, unknown> {
  const expression = source.slice(source.indexOf('=') + 1).replace(/;\s*$/, '');
  return Function(`"use strict"; return (${expression});`)() as Record<string, unknown>;
}

const miniExam = (source: string, code: string, name: string): ExamSet => {
  const raw = parseSourceObject(source);
  const groups = Object.entries(raw).filter(([key, value]) => key.startsWith('part') && Array.isArray(value)).map(([key, value]) => ({ groupTitle: key, items: (value as Array<Record<string, unknown>>).map(item => ({ id: Number(item.id), type: 'mc', prompt: String(item.q ?? item.prompt ?? item.sentence ?? ''), promptVi: String(item.vi ?? item.context ?? ''), options: (item.options ?? item.chips ?? item.accepted) as string[] | undefined, correct: Number(item.correct ?? item.starIndex ?? 0), explain: String(item.explain ?? '') })) }));
  return { code, name, timeLimit: 30, sections: [{ id: code, partNumber: 1, partTitle: name, groups }] };
};

  ...set,
  sections: set.sections.map(section => ({
    ...section,
    groups: section.groups.map(group => ({
      ...group,
      items: group.items.map(item => item.options?.length ? item : ({ ...item, options: item.parts, type: 'mc' }))
    }))
  }))
}));

function mapA2_1Vocab(meta: LessonMeta): VocabEntry[] {
  const master = masterVocabData.filter(entry => entry.l === `A2-${meta.number}`);
  if (master.length) return master.map((entry, index) => ({
    id: `a2-1-${meta.number}-${index + 1}`,
    lesson: meta.number,
    level: 'A2-1' as const,
    jp: entry.jp ?? entry.kanji ?? '', kana: entry.kana ?? '', kanji: entry.kanji ?? '',
    romaji: entry.romaji ?? '', meaning: entry.vi ?? '', hv: entry.hv,
  }));
  const source = getLessonSource(meta);
  return (parseLegacyArray(source, 'VOCAB_DATA') as Array<Record<string, unknown>>).map((entry, index) => ({
    id: `a2-1-${meta.number}-${index + 1}`, lesson: meta.number, level: 'A2-1' as const,
    jp: String(entry.jp ?? entry.kanji ?? ''), kana: String(entry.kana ?? ''), kanji: String(entry.kanji ?? entry.jp ?? ''),
    romaji: String(entry.romaji ?? ''), meaning: String(entry.vi ?? ''),
  }));
}

export const lessonSummaries: LessonSummary[] = lessonCatalog.map(meta => {
  const source = getLessonSource(meta);
  const legacy: LegacyLessonArrays = {
    VOCAB_DATA: parseLegacyArray(source, 'VOCAB_DATA') as Array<Record<string, unknown>>,
    VERB_DATA: parseLegacyArray(source, 'VERB_DATA') as Array<Record<string, unknown>>,
    QUIZ_DATA: parseLegacyArray(source, 'QUIZ_DATA') as QuizQuestion[],
  };
  const authoredQuiz = legacy.QUIZ_DATA.filter(item => Array.isArray(item.options) && item.options.length === 4 && Number.isInteger(item.correct) && item.correct >= 0 && item.correct < item.options.length);
  const vocab = meta.level === 'A2-2'
    ? vocabA2_2.filter(entry => entry.lesson === meta.number)
    : mapA2_1Vocab(meta);
  const kanji = (meta.level === 'A2-2' ? kanjiA2_2 : kanjiA2_1).filter(entry => entry.lesson === meta.number);
  const authoredGrammar = grammarData.filter(entry => entry.level === meta.level && entry.lesson === meta.number);
  const grammar = authoredGrammar.length ? authoredGrammar : parseLegacyGrammar(meta);
  return {
    ...meta,
    vocab,
    grammar,
    kanji,
    quiz: authoredQuiz,
  };
});

export function getLesson(level: string, lesson: number): LessonSummary | undefined {
  return lessonSummaries.find(item => item.level.toLowerCase() === level.toLowerCase() && item.number === lesson);
}

export const a2_1VocabularyTotal = masterVocabData.filter(entry => /^A2-(?:[1-9]|10)$/.test(entry.l ?? '')).length;
export const a2_2VocabularyTotal = vocabA2_2.length;
