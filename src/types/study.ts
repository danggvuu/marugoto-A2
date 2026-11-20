export interface VocabEntry {
  id: string;
  lesson: number;
  level: 'A1' | 'A2-1' | 'A2-2';
  jp: string;
  kana: string;
  kanji: string;
  romaji: string;
  meaning: string;
  hv?: string;
  icon?: string;
}

export interface GrammarExample {
  jp: string;
  ruby?: string;
  vi: string;
}

export interface GrammarEntry {
  id: number;
  level: string;
  lesson: number;
  lessonTitle: string;
  title: string;
  tag?: string;
  category?: string;
  formula: string;
  meaning: string;
  notes?: string;
  examples: GrammarExample[];
}

export interface KanjiEntry {
  id: string;
  lesson: number;
  level: 'A2-1' | 'A2-2';
  word: string;
  kana: string;
  meaning: string;
  characters: KanjiCharacter[];
}

export interface KanjiCharacter {
  character: string;
  meaning: string;
  vietnamese: string;
  strokes: number;
  on: string;
  kun: string;
  mnemonic: string;
  formula: string;
}

export interface QuizQuestion {
  id: number;
  category: string;
  q: string;
  options: string[];
  correct: number;
  explain: string;
}

export interface LessonSummary {
  level: 'A2-1' | 'A2-2';
  number: number;
  topic: string;
  title: string;
  subtitle: string;
  quote: string;
  icon: string;
  vocab: VocabEntry[];
  grammar: GrammarEntry[];
  kanji: KanjiEntry[];
  quiz: QuizQuestion[];
}

export interface ExamItem {
  id: number;
  type: string;
  prompt: string;
  promptVi?: string;
  targetWord?: string;
  options?: string[];
  correct?: number;
  parts?: string[];
  explain?: string;
}

export interface ExamGroup {
  groupTitle: string;
  groupInstruction?: string;
  items: ExamItem[];
}

export interface ExamSection {
  id: string;
  partNumber: number;
  partTitle: string;
  partDesc?: string;
  badge?: string;
  groups: ExamGroup[];
}

export interface ExamSet {
  code: string;
  name: string;
  tag?: string;
  desc?: string;
  timeLimit: number;
  sections: ExamSection[];
}
