import { useEffect, useMemo, useState } from 'react';
import { Link, useNavigate, useParams } from 'react-router-dom';
import { Badge } from '@astryxdesign/core/Badge';
import { Button } from '@astryxdesign/core/Button';
import { BookOpen, ChevronRight, Languages, PenLine, Volume2 } from 'lucide-react';
import * as stylex from '@stylexjs/stylex';
import { common } from '../styles/tokens.stylex';
import { getLesson } from '../services/dataLoader';
import { useStudyProgress } from '../services/progress';
import { speakJapanese } from '../services/speech';
import { FlashcardDeck } from '../components/flashcard/FlashcardDeck';
import { GrammarSection } from '../components/grammar/GrammarSection';
import { QuizEngine } from '../components/quiz/QuizEngine';
import { TypingPractice } from '../components/typing/TypingPractice';
import { KanjiCard } from '../components/kanji/KanjiCard';
import { lessonCatalog } from '../services/lessonCatalog';

const s = stylex.create({
 page: { maxWidth: 1320, margin: '0 auto', padding: '30px 36px 60px' },
 hero: { padding: 34, borderRadius: 24, backgroundColor: '#1e1b4b', backgroundImage: 'linear-gradient(135deg, #1e1b4b 0%, #312e81 40%, #4338ca 100%)', color: '#ffffff', boxShadow: '0 20px 45px -12px rgba(30, 27, 75, 0.35)', borderWidth: 1, borderStyle: 'solid', borderColor: 'rgba(255, 255, 255, 0.12)' },
 crumb: { display: 'flex', alignItems: 'center', gap: 7, color: '#c7d2fe', fontSize: 13, fontWeight: 600 },
 title: { fontSize: 'clamp(28px, 4vw, 44px)', fontWeight: 850, lineHeight: 1.15, marginBlock: '14px 8px', color: '#ffffff' },
 quote: { fontSize: 20, color: '#e0e7ff', display: 'flex', alignItems: 'center', gap: 10, fontWeight: 600 },
 stats: { display: 'flex', gap: 8, flexWrap: 'wrap', marginTop: 22 },
 tabs: { display: 'flex', gap: 8, flexWrap: 'wrap', marginBlock: '24px' },
 section: { marginBlock: '30px' },
 grid: { display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(260px, 1fr))', gap: 14 },
 heading: { display: 'flex', justifyItems: 'space-between', justifyContent: 'space-between', alignItems: 'center', gap: 12, marginBottom: 16 }
});

export function LessonPage() {
 const { level = 'a2-1', id = '1' } = useParams();
 const number = Number(id);
 const lesson = getLesson(level, number);
 const [tab, setTab] = useState('flashcards');
 const { markVocab, markKanji, recordQuiz, setLastLesson } = useStudyProgress();
 const navigate = useNavigate();
 const key = `${lesson?.level.toLowerCase() ?? level}/${number}`;

 useEffect(() => { if (lesson) setLastLesson(key); }, [lesson, key, setLastLesson]);
 const next = useMemo(() => lessonCatalog.find(x => x.level === lesson?.level && x.number === number + 1), [lesson, number]);

 if (!lesson) return <div {...stylex.props(common.page)}><h1>Không tìm thấy bài học</h1><p>Hãy quay về dashboard và chọn bài khác.</p></div>;

 const tabs = [
  ['flashcards', '🎴 Flashcard Từ Vựng'],
  ['grammar', '📖 Ngữ Pháp'],
  ['kanji', '⛩️ Chữ Hán'],
  ['quiz', '📝 Mini Test'],
  ['typing', '⌨️ Luyện Gõ']
 ];

 return <div {...stylex.props(s.page)}>
  <section {...stylex.props(s.hero)}>
   <div {...stylex.props(s.crumb)}>
    <span>{lesson.level}</span>
    <ChevronRight size={15}/>
    <span>{lesson.topic}</span>
   </div>
   <h1 {...stylex.props(s.title)}>{lesson.icon} Bài {number}: {lesson.title}</h1>
   <div {...stylex.props(s.quote)}>
    <span>「{lesson.quote}」</span>
    <Button label="Nghe câu chủ đề" variant="secondary" size="sm" isIconOnly icon={<Volume2 size={17}/>} onClick={() => speakJapanese(lesson.quote)}/>
   </div>
   <p style={{ color: '#e0e7ff', marginTop: 8, fontSize: 15 }}>{lesson.subtitle}</p>
   <div {...stylex.props(s.stats)}>
    <Badge label={`${lesson.vocab.length} từ vựng`}/>
    <Badge label={`${lesson.grammar.length} mẫu ngữ pháp`}/>
    <Badge label={`${lesson.kanji.length} chữ Hán`}/>
    <Badge label={`${lesson.quiz.length} câu trắc nghiệm`}/>
   </div>
  </section>

  <nav {...stylex.props(s.tabs)} aria-label="Mục bài học">
   {tabs.map(([tabId, label]) => (
    <Button key={tabId} label={label} size="sm" variant={tab === tabId ? 'primary' : 'secondary'} onClick={() => setTab(tabId)}/>
   ))}
  </nav>

  {tab === 'flashcards' && (
   <section {...stylex.props(s.section)}>
    <div {...stylex.props(s.heading)}>
     <h2 {...stylex.props(common.sectionTitle)} style={{ margin: 0, display: 'flex', alignItems: 'center', gap: 8 }}>
      <BookOpen size={22} color="#e11d48"/> 3D Flashcard Studio
     </h2>
     <Badge label="Lật thẻ · Âm thanh · Xáo trộn"/>
    </div>
    <FlashcardDeck key={key} cards={lesson.vocab} onLearned={markVocab}/>
   </section>
  )}

  {tab === 'grammar' && (
   <section {...stylex.props(s.section)}>
    <div {...stylex.props(s.heading)}>
     <h2 {...stylex.props(common.sectionTitle)} style={{ margin: 0 }}>Cẩm nang chuyên đề ngữ pháp</h2>
     <Badge label={`${lesson.grammar.length} chủ điểm`}/>
    </div>
    <GrammarSection entries={lesson.grammar}/>
   </section>
  )}

  {tab === 'kanji' && (
   <section {...stylex.props(s.section)}>
    <div {...stylex.props(s.heading)}>
     <h2 {...stylex.props(common.sectionTitle)} style={{ margin: 0, display: 'flex', alignItems: 'center', gap: 8 }}>
      <Languages size={22} color="#4f46e5"/> Kho chữ Hán trong bài
     </h2>
     <Badge label={`${lesson.kanji.length} mục Kanji`}/>
    </div>
    <div {...stylex.props(s.grid)}>
     {lesson.kanji.map(entry => (
      <KanjiCard key={entry.id} entry={entry} onLearned={markKanji}/>
     ))}
    </div>
   </section>
  )}

  {tab === 'quiz' && (
   <section {...stylex.props(s.section)}>
    <h2 {...stylex.props(common.sectionTitle)}>Đấu trường Mini Test trắc nghiệm</h2>
    <QuizEngine key={key} questions={lesson.quiz} onComplete={score => recordQuiz(score, key)}/>
   </section>
  )}

  {tab === 'typing' && (
   <section {...stylex.props(s.section)}>
    <h2 {...stylex.props(common.sectionTitle)} style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
     <PenLine size={22} color="#059669"/> Typing Studio Luyện Gõ
    </h2>
    <TypingPractice key={key} words={lesson.vocab}/>
   </section>
  )}

  <section style={{ display: 'flex', gap: 12, marginTop: 32, flexWrap: 'wrap' }}>
   <Button label="Quay về Dashboard" variant="secondary" onClick={() => navigate('/')}/>
   {next && (
    <Link to={`/lessons/${next.level.toLowerCase()}/${next.number}`} style={{ textDecoration: 'none' }}>
     <Button label={`Học tiếp: Bài ${next.number} - ${next.title}`} variant="primary"/>
    </Link>
   )}
  </section>
 </div>;
}
