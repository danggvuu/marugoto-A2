import { useEffect, useMemo, useState } from 'react';
import { Badge } from '@astryxdesign/core/Badge';
import { Button } from '@astryxdesign/core/Button';
import { Clock3, Trophy } from 'lucide-react';
import * as stylex from '@stylexjs/stylex';
import { examSets } from '../services/dataLoader';
import type { ExamItem, ExamSet } from '../types/study';
import { common } from '../styles/tokens.stylex';

const s = stylex.create({
 page: { maxWidth: 1120, margin: '0 auto', padding: '32px 36px 60px' },
 hero: { padding: 32, borderRadius: 24, backgroundColor: '#1e1b4b', backgroundImage: 'linear-gradient(135deg, #1e1b4b 0%, #312e81 40%, #4338ca 100%)', color: '#ffffff', boxShadow: '0 20px 45px -12px rgba(30, 27, 75, 0.35)', borderWidth: 1, borderStyle: 'solid', borderColor: 'rgba(255, 255, 255, 0.12)' },
 sets: { display: 'flex', gap: 10, flexWrap: 'wrap', marginBlock: '22px' },
 test: { display: 'grid', gap: 18 },
 section: { padding: 20, borderRadius: 16, borderWidth: 1.5, borderStyle: 'solid', borderColor: 'var(--color-border)', backgroundColor: 'var(--color-background-card)' },
 question: { padding: 18, borderRadius: 14, borderWidth: 1.5, borderStyle: 'solid', borderColor: 'var(--color-border)', marginBlock: 14, backgroundColor: 'var(--color-background-body)' },
 option: { display: 'flex', alignItems: 'center', gap: 10, padding: 10, borderRadius: 10, cursor: 'pointer' },
 correct: { backgroundColor: 'var(--color-success-muted)', color: 'var(--color-success)', fontWeight: 700 },
 wrong: { backgroundColor: 'var(--color-error-muted)', color: 'var(--color-error)' },
 controls: { display: 'flex', alignItems: 'center', gap: 12, flexWrap: 'wrap', marginTop: 14 },
 score: { fontSize: 36, fontWeight: 850, color: '#4f46e5', marginBlock: 12 },
 sticky: { position: 'sticky', top: 76, zIndex: 10, display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '12px 18px', backgroundColor: 'var(--color-background-surface)', backdropFilter: 'blur(16px)', borderRadius: 16, borderWidth: 1.5, borderStyle: 'solid', borderColor: 'var(--color-border)', boxShadow: '0 10px 25px -5px rgba(15, 23, 42, 0.08)' }
});

export function ExamPage() {
 const [code, setCode] = useState('');
 const [answers, setAnswers] = useState<Record<string, number>>({});
 const [submitted, setSubmitted] = useState(false);
 const [seconds, setSeconds] = useState(0);

 const exam = examSets.find(item => item.code === code);
 const items = useMemo(() => exam ? exam.sections.flatMap(section => section.groups.flatMap(group => group.items)) : [], [exam]);
 const answerableItems = items.filter(item => Number.isInteger(item.correct) && Number(item.correct) >= 0 && Number(item.correct) < (item.options?.length ?? 0));
 const score = answerableItems.length ? Math.round(answerableItems.filter(item => answers[String(item.id)] === item.correct).length / answerableItems.length * 100) : 0;
 const [startedAt, setStartedAt] = useState<number | null>(null);
 const bestKey = exam ? `marugoto-exam-best:${exam.code}` : '';
 const [bestScore, setBestScore] = useState(0);

 useEffect(() => {
  try {
   const stored = exam ? Number(localStorage.getItem(`marugoto-exam-best:${exam.code}`) ?? 0) : 0;
   setBestScore(Number.isFinite(stored) ? Math.max(0, Math.min(100, stored)) : 0);
  } catch {
   setBestScore(0);
  }
 }, [exam?.code]);

 useEffect(() => {
  if (submitted && exam && score > bestScore) {
   try { localStorage.setItem(bestKey, String(score)); } catch { /* storage may be blocked */ }
   setBestScore(score);
  }
 }, [submitted, exam, score, bestScore, bestKey]);

 const begin = (set: ExamSet) => {
  setCode(set.code);
  setAnswers({});
  setSubmitted(false);
  setSeconds(0);
  setStartedAt(Date.now());
 };

 const retry = () => { if (exam) begin(exam); };

 return <div {...stylex.props(s.page)}>
  <section {...stylex.props(s.hero)}>
   <Badge label="PHÒNG THI THỰC CHIẾN · MARUGOTO A2-1"/>
   <h1 style={{ fontSize: 'clamp(28px, 4vw, 42px)', fontWeight: 850, marginBlock: '12px 6px', color: '#ffffff' }}>🎯 Bộ Đề Ôn Tập & Đề Thi Thử</h1>
   <p style={{ color: '#e0e7ff', fontSize: 16, maxWidth: 640 }}>Luyện đề có tính giờ, kiểm tra phản xạ chọn đáp án đúng và mở khóa lời giải chi tiết ngay sau khi nộp bài.</p>
   <div {...stylex.props(s.controls)}>
    <span style={{ display: 'flex', alignItems: 'center', gap: 6, color: '#c7d2fe', fontWeight: 600 }}>
     <Clock3 size={17}/> {exam ? `${Math.floor(seconds / 60)}:${String(seconds % 60).padStart(2, '0')} / ${exam.timeLimit} phút` : `${examSets.length} bộ mã đề`}
    </span>
    <span style={{ display: 'flex', alignItems: 'center', gap: 6, color: '#c7d2fe', fontWeight: 600 }}>
     <Trophy size={17}/> Điểm cao nhất lưu trên máy
    </span>
   </div>
  </section>

  {!exam ? (
   <>
    <h2 {...stylex.props(common.sectionTitle)} style={{ marginTop: 28 }}>Chọn một mã đề để bắt đầu bấm giờ thi</h2>
    <div {...stylex.props(s.sets)}>
     {examSets.map(set => (
      <Button key={set.code} label={`${set.code} · ${set.name}`} variant="secondary" onClick={() => begin(set)}/>
     ))}
    </div>
   </>
  ) : (
   <>
    <p style={{ marginBlock: 16, color: 'var(--color-text-secondary)', fontWeight: 600 }}>Điểm tính trên {answerableItems.length} câu trắc nghiệm. Câu hỏi tự luận dùng để tự đối chiếu sau khi nộp bài.</p>
    <div {...stylex.props(s.controls)} style={{ marginBottom: 18 }}>
     <Button label="Chọn mã đề khác" variant="secondary" onClick={() => { setCode(''); setStartedAt(null); setSubmitted(false); }}/>
     {submitted && <Button label="Làm lại đề này" variant="primary" onClick={retry}/>}
    </div>
    <ExamRunner key={`${code}-${startedAt}`} exam={exam} items={items} answers={answers} setAnswers={setAnswers} submitted={submitted} setSubmitted={setSubmitted} seconds={seconds} setSeconds={setSeconds} score={score} startedAt={startedAt} bestScore={bestScore}/>
   </>
  )}
 </div>;
}

function ExamRunner({ exam, items, answers, setAnswers, submitted, setSubmitted, seconds, setSeconds, score, startedAt, bestScore }: { exam: ExamSet; items: ExamItem[]; answers: Record<string, number>; setAnswers: (value: Record<string, number>) => void; submitted: boolean; setSubmitted: (value: boolean) => void; seconds: number; setSeconds: (value: number | ((previous: number) => number)) => void; score: number; startedAt: number | null; bestScore: number }) {
 useEffect(() => {
  if (submitted || startedAt === null) return;
  const tick = () => {
   const elapsed = Math.floor((Date.now() - startedAt) / 1000);
   setSeconds(Math.min(elapsed, exam.timeLimit * 60));
   if (elapsed >= exam.timeLimit * 60) setSubmitted(true);
  };
  tick();
  const timer = window.setInterval(tick, 500);
  return () => window.clearInterval(timer);
 }, [startedAt, submitted, exam.timeLimit, setSeconds, setSubmitted]);

 const passages = exam.sections.flatMap(section => section.groups.map(group => group.groupInstruction).filter((text): text is string => Boolean(text)));

 return (
  <div {...stylex.props(s.test)}>
   <div {...stylex.props(s.sticky)}>
    <strong>{exam.code} · {items.filter(item => answers[String(item.id)] !== undefined).length}/{items.length} câu đã trả lời</strong>
    <span style={{ fontSize: 16, fontWeight: 750, color: '#4f46e5' }}>{Math.floor(seconds / 60)}:{String(seconds % 60).padStart(2, '0')}</span>
    {submitted ? (
     <Badge label={`${score}% · Điểm cao nhất: ${bestScore}%`} variant={score >= 70 ? 'success' : 'neutral'}/>
    ) : (
     <Button label="Nộp bài chấm điểm" variant="primary" onClick={() => setSubmitted(true)}/>
    )}
   </div>
   {submitted && <div {...stylex.props(s.score)}>Kết quả: {score}%</div>}
   {passages.length > 0 && (
    <section {...stylex.props(s.section)}>
     <h2>Đoạn đọc và hướng dẫn</h2>
     {passages.map((passage, index) => <p key={index} dangerouslySetInnerHTML={{ __html: passage }} style={{ lineHeight: 1.6 }}/>)}
    </section>
   )}
   {exam.sections.map(section => (
    <section key={section.id} {...stylex.props(s.section)}>
     <h2 style={{ color: '#4f46e5' }}>{section.partTitle}</h2>
     {section.groups.map((group, gi) => (
      <div key={`${section.id}-${gi}`} style={{ marginTop: 14 }}>
       <h3>{group.groupTitle}</h3>
       {group.items.map(item => (
        <ExamQuestion key={`${section.id}-${item.id}`} item={item} answer={answers[String(item.id)]} submitted={submitted} onSelect={selected => setAnswers({ ...answers, [String(item.id)]: selected })}/>
       ))}
      </div>
     ))}
    </section>
   ))}
  </div>
 );
}

function ExamQuestion({ item, answer, submitted, onSelect }: { item: ExamItem; answer?: number; submitted: boolean; onSelect: (choice: number) => void }) {
 const hasOptions = (item.options?.length ?? 0) > 0 && Number.isInteger(item.correct) && Number(item.correct) >= 0 && Number(item.correct) < (item.options?.length ?? 0);
 return (
  <article {...stylex.props(s.question)}>
   <strong dangerouslySetInnerHTML={{ __html: item.prompt }} style={{ fontSize: 15, lineHeight: 1.5 }}/>
   {item.promptVi && <p style={{ color: 'var(--color-text-secondary)', marginTop: 4, fontSize: 13.5 }}>{item.promptVi}</p>}
   {item.parts?.length === 4 && <p style={{ color: '#6366f1', fontSize: 13, fontWeight: 600 }}>Đặt mảnh câu vào vị trí ★, chọn mảnh phù hợp.</p>}
   {hasOptions ? item.options?.map((option, index) => {
    const correct = submitted && index === item.correct;
    const wrong = submitted && answer === index && index !== item.correct;
    return (
     <label key={index} {...stylex.props(s.option, correct && s.correct, wrong && s.wrong)}>
      <input type="radio" checked={answer === index} disabled={submitted} onChange={() => onSelect(index)}/>
      <span>{item.parts?.length === 4 ? `${index + 1}. ${option}` : option}</span>
     </label>
    );
   }) : (
    <div style={{ marginTop: 8 }}>
     <p style={{ fontSize: 13, color: 'var(--color-text-secondary)' }}>Câu hỏi tự luận, tự đối chiếu sau khi nộp bài.</p>
     <textarea aria-label={`Câu tự luyện ${item.id}`} placeholder="Nhập câu trả lời để tự đối chiếu sau khi nộp" disabled={submitted} style={{ width: '100%', minHeight: 70, borderRadius: 8, padding: 8, border: '1px solid var(--color-border)', backgroundColor: 'var(--color-background-surface)', font: 'inherit', color: 'var(--color-text-primary)' }}/>
    </div>
   )}
   {submitted && item.explain && (
    <p dangerouslySetInnerHTML={{ __html: item.explain }} style={{ marginTop: 10, padding: 10, borderRadius: 8, background: '#f0fdf4', color: '#166534', fontSize: 13.5 }}/>
   )}
  </article>
 );
}
