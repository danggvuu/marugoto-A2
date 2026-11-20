import a2_2Vocab from '../../data/vocab_a2_2_official.json';
import a2_2Kanji from '../../data/kanji_vocab_a2_2_official.json';
import masterVocab from '../../data/master_vocab_enriched.json';
import grammarSource from '../../data/grammar_extracted.json';
import kanjiA2_1Words from '../../data/kanji_vocab_11_18.json';
import kanjiCharacters from '../../data/kanji_extracted.json';
import examSource from '../../assets/data/de_thi_tong_hop_11_18_data.js?raw';
import mini1114 from '../../data/mini_11_14.json';
import mini1518 from '../../data/mini_15_18.json';
import { lessonCatalog, type LessonMeta } from './lessonCatalog';
import type { ExamGroup, ExamItem, ExamSet, GrammarEntry, KanjiEntry, LessonSummary, QuizQuestion, VocabEntry } from '../types/study';

interface RawVocab {
  jp?: string; kana?: string; kanji?: string; romaji?: string; vi?: string; hv?: string; icon?: string; l?: string;
}
interface RawKanjiWord { word: string; kana: string; mean: string; }
interface RawA21KanjiWord { lesson: number; kanji: string; kana: string; vi: string; }
interface RawKanjiCharacter {
  char: string; hv: string; strokes: number; on?: string; kun?: string;
  mnemonic?: string; formula?: string; meaning?: string;
}
interface LessonJson { level: string; lesson: number; vocab: Array<Record<string, unknown>>; verbs: Array<Record<string, unknown>>; quiz: QuizQuestion[]; }

const a2_2VocabData = a2_2Vocab as Record<string, RawVocab[]>;
const a2_2KanjiData = a2_2Kanji as Record<string, unknown>;
const masterVocabData = masterVocab as RawVocab[];
const grammarData = grammarSource as GrammarEntry[];
const kanjiCharacterData = kanjiCharacters as RawKanjiCharacter[];
const kanjiA21WordData = kanjiA2_1Words as RawA21KanjiWord[];
const lessonJsonSources = import.meta.glob('../../data/lessons/*.json', { eager: true, import: 'default' }) as Record<string, LessonJson>;
import lessonGrammar from '../../data/lesson_grammar.json';

function getLessonData(meta: LessonMeta): LessonJson {
  const key = `../../data/lessons/${meta.level.toLowerCase().replace('-', '_')}_${String(meta.number).padStart(2, '0')}.json`;
  return lessonJsonSources[key] ?? { level: meta.level, lesson: meta.number, vocab: [], verbs: [], quiz: [] };
}

function parseLegacyGrammar(meta: LessonMeta): GrammarEntry[] {
  return (lessonGrammar as Record<string, GrammarEntry[]>)[`${meta.level}/${meta.number}`] ?? [];
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

const miniExam = (raw: Record<string, unknown>, code: string, name: string): ExamSet => {
  let nextId = 1;
  const groups: ExamGroup[] = [];
  const mapItem = (item: Record<string, unknown>): ExamItem => {
    const chips = item.chips as string[] | undefined;
    const options = (item.options ?? chips) as string[] | undefined;
    const starChip = String(item.starChip ?? '');
    return { id: nextId++, type: options?.length ? 'mc' : 'self-study',
      prompt: String(item.q ?? item.promptA ?? item.situation ?? item.sentence ?? item.vi ?? item.prompt ?? ''),
      promptVi: chips ? `${item.pre ?? ''} ___ ___ ★ ___ ${item.post ?? ''}` : String(item.context ?? ''),
      options, correct: chips ? chips.indexOf(starChip) : typeof item.correct === 'number' ? item.correct : undefined,
      explain: String(item.explain ?? item.promptB ?? item.modelSentence ?? item.displayAnswer ?? ''),
    };
  };
  for(const [key,value] of Object.entries(raw)) {
    if(!/^(?:part\d+Data|p\d+)$/.test(key) || !Array.isArray(value)) continue;
    const regular: ExamItem[] = [];
    for(const item of value as Array<Record<string,unknown>>) {
      if(Array.isArray(item.questions)) groups.push({groupTitle:String(item.title ?? 'Đọc hiểu'),groupInstruction:String(item.text ?? ''),items:item.questions.map(question=>mapItem(question as Record<string,unknown>))});
      else regular.push(mapItem(item));
    }
    if(regular.length) groups.push({groupTitle:key,items:regular});
  }
  return {code,name,timeLimit:30,sections:[{id:code,partNumber:1,partTitle:name,groups}]};
};

const rawExamData = JSON.parse(examSource.slice(examSource.indexOf('=') + 1).replace(/;\s*$/, '')) as ExamSet[];
export const examSets: ExamSet[] = [...rawExamData, miniExam(mini1114 as Record<string, unknown>, 'MINI-11-14', 'Mini Test Bài 11–14'), ...(mini1518.EXAMS_LIST as unknown as Array<Record<string,unknown>>).map(set=>miniExam(set, `MINI-15-18-${set.code}`, `Mini Test 15–18 · ${set.shortTitle}`))].map(set => ({
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
  const source = getLessonData(meta);
  return (source.vocab).map((entry, index) => ({
    id: `a2-1-${meta.number}-${index + 1}`, lesson: meta.number, level: 'A2-1' as const,
    jp: String(entry.jp ?? entry.kanji ?? ''), kana: String(entry.kana ?? ''), kanji: String(entry.kanji ?? entry.jp ?? ''),
    romaji: String(entry.romaji ?? ''), meaning: String(entry.vi ?? ''),
  }));
}

export const lessonSummaries: LessonSummary[] = lessonCatalog.map(meta => {
  const lessonData = getLessonData(meta);
  const authoredQuiz = lessonData.quiz.filter(item => Array.isArray(item.options) && item.options.length === 4 && Number.isInteger(item.correct) && item.correct >= 0 && item.correct < item.options.length);
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
