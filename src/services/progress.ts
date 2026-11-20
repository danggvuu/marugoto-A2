import { useCallback, useSyncExternalStore } from 'react';

const PROGRESS_KEY = 'marugoto_astryx_progress_v1';
const CHANGE_EVENT = 'marugoto-progress-change';
export interface StudyProgress {
 vocab: string[];
 kanji: string[];
 quizAttempts: number;
 bestScore: number;
 completedLessons: string[];
 lastLesson?: string;
}
const EMPTY: StudyProgress = { vocab: [], kanji: [], quizAttempts: 0, bestScore: 0, completedLessons: [] };
let storageBlocked = false;
let cachedRaw: string | null | undefined;
let cachedProgress = EMPTY;
const strings = (value: unknown): string[] => Array.isArray(value) ? [...new Set(value.filter((item): item is string => typeof item === 'string'))] : [];
export function readProgress(): StudyProgress {
 if(storageBlocked) return cachedProgress;
 try {
  const raw = localStorage.getItem(PROGRESS_KEY);
  if (raw === cachedRaw) return cachedProgress;
  cachedRaw = raw;
  if (!raw) return cachedProgress = EMPTY;
  const parsed = JSON.parse(raw);
  if (!parsed || typeof parsed !== 'object') return cachedProgress = EMPTY;
  return cachedProgress = {
   vocab: strings(parsed.vocab), kanji: strings(parsed.kanji), completedLessons: strings(parsed.completedLessons),
   quizAttempts: Number.isFinite(parsed.quizAttempts) ? Math.max(0, Math.floor(parsed.quizAttempts)) : 0,
   bestScore: Number.isFinite(parsed.bestScore) ? Math.max(0, Math.min(100, parsed.bestScore)) : 0,
   lastLesson: typeof parsed.lastLesson === 'string' && /^a2-[12]\/(?:[1-9]|1[0-8])$/.test(parsed.lastLesson) ? parsed.lastLesson : undefined,
  };
 } catch { storageBlocked = true; return cachedProgress; }
}
function subscribe(listener: () => void) {
 window.addEventListener(CHANGE_EVENT, listener);
 window.addEventListener('storage', listener);
 return () => { window.removeEventListener(CHANGE_EVENT, listener); window.removeEventListener('storage', listener); };
}
function updateProgress(recipe: (current: StudyProgress) => StudyProgress) {
 const next = recipe(readProgress());
 cachedProgress = next;
 try { cachedRaw = JSON.stringify(next); localStorage.setItem(PROGRESS_KEY, cachedRaw); } catch { storageBlocked = true; /* retain in-memory progress when storage is blocked */ }
 window.dispatchEvent(new Event(CHANGE_EVENT));
}
export function useStudyProgress() {
 const progress = useSyncExternalStore(subscribe, readProgress, () => EMPTY);
 const markVocab = useCallback((id: string) => updateProgress(p => ({ ...p, vocab: p.vocab.includes(id) ? p.vocab : [...p.vocab, id] })), []);
 const markKanji = useCallback((id: string) => updateProgress(p => ({ ...p, kanji: p.kanji.includes(id) ? p.kanji : [...p.kanji, id] })), []);
 const recordQuiz = useCallback((score: number, lessonKey: string) => updateProgress(p => ({
  ...p, quizAttempts: p.quizAttempts + 1, bestScore: Math.max(p.bestScore, score), lastLesson: lessonKey,
  completedLessons: score >= 70 && !p.completedLessons.includes(lessonKey) ? [...p.completedLessons, lessonKey] : p.completedLessons,
 })), []);
 const setLastLesson = useCallback((lessonKey: string) => updateProgress(p => p.lastLesson === lessonKey ? p : ({ ...p, lastLesson: lessonKey })), []);
 return { progress, markVocab, markKanji, recordQuiz, setLastLesson };
}
