import { useEffect, useMemo, useState } from 'react';
import { Badge } from '@astryxdesign/core/Badge';
import { Button } from '@astryxdesign/core/Button';
import { Card } from '@astryxdesign/core/Card';
import { AudioButton } from '../components/common/AudioButton';
import kaiwaData from '../../data/kaiwa_topics.json';
import * as stylex from '@stylexjs/stylex';
import { common } from '../styles/tokens.stylex';

interface KaiwaSample { level: string; tag: string; jp: string; vi: string; keyPoints: string; }
interface KaiwaQuestion { id: number; qJp: string; qVi: string; intent: string; sampleAnswers: KaiwaSample[]; vocab: Array<{ jp: string; vi: string }>; }
interface KaiwaTopic { id: string; num: number; title: string; titleJp: string; badge: string; desc: string; coreQuestions: KaiwaQuestion[]; }

const topics = kaiwaData as KaiwaTopic[];

const s = stylex.create({
 page: { maxWidth: 1120, margin: '0 auto', padding: '32px 36px 60px' },
 hero: { padding: 32, borderRadius: 24, backgroundColor: '#1e1b4b', backgroundImage: 'linear-gradient(135deg, #1e1b4b 0%, #312e81 40%, #4338ca 100%)', color: '#ffffff', boxShadow: '0 20px 45px -12px rgba(30, 27, 75, 0.35)', borderWidth: 1, borderStyle: 'solid', borderColor: 'rgba(255, 255, 255, 0.12)' },
 topics: { display: 'flex', gap: 10, flexWrap: 'wrap', marginBlock: 20 },
 question: { padding: 22, display: 'grid', gap: 14, marginBlock: 16, borderRadius: 16, backgroundColor: 'var(--color-background-card)', borderWidth: 1.5, borderStyle: 'solid', borderColor: 'var(--color-border)', boxShadow: '0 4px 16px -2px rgba(15, 23, 42, 0.04)' },
 jp: { fontSize: 21, fontWeight: 700, display: 'flex', alignItems: 'center', gap: 10, color: 'var(--color-text-primary)' },
 answer: { padding: 16, borderRadius: 12, backgroundColor: 'var(--color-background-body)', borderWidth: 1, borderStyle: 'solid', borderColor: 'var(--color-border)', display: 'grid', gap: 8 }
});

export function KaiwaPage() {
 const [remaining, setRemaining] = useState(300);
 const [running, setRunning] = useState(false);

 useEffect(() => {
  if (!running) return;
  const deadline = Date.now() + remaining * 1000;
  const timer = window.setInterval(() => {
   const left = Math.max(0, Math.ceil((deadline - Date.now()) / 1000));
   setRemaining(left);
   if (!left) setRunning(false);
  }, 250);
  return () => clearInterval(timer);
 }, [running]);

 const [topicId, setTopicId] = useState(topics[0]?.id ?? '');
 const [questionId, setQuestionId] = useState<number | null>(null);
 const [showHints, setShowHints] = useState(true);
 const topic = topics.find(item => item.id === topicId);
 const questions = useMemo(() => topic?.coreQuestions ?? [], [topic]);

 return (
  <div {...stylex.props(s.page)}>
   <section {...stylex.props(s.hero)}>
    <Badge label="KAIWA PHẢN XẠ · PHÒNG THI VẤN ĐÁP 5 PHÚT"/>
    <h1 style={{ fontSize: 'clamp(28px, 4vw, 42px)', fontWeight: 850, marginBlock: '12px 6px', color: '#ffffff' }}>🎙️ Luyện Nói Kaiwa 5 Phút</h1>
    <p style={{ color: '#e0e7ff', fontSize: 16, maxWidth: 640 }}>Thực hành vấn đáp với 4 chủ đề phỏng vấn: Sức khỏe, Thăm hỏi, Tiệc mừng và Chuyến đi Nhật kèm câu trả lời mẫu có audio phát âm chuẩn.</p>
    <div style={{ display: 'flex', alignItems: 'center', gap: 14, marginTop: 18, flexWrap: 'wrap' }}>
     <div style={{ fontSize: 24, fontWeight: 850, color: '#38bdf8', background: 'rgba(255,255,255,0.1)', padding: '6px 16px', borderRadius: 10 }}>
      ⏱️ {Math.floor(remaining / 60)}:{String(remaining % 60).padStart(2, '0')}
     </div>
     <Button label={running ? 'Tạm dừng đồng hồ' : 'Bắt đầu 5 phút'} isDisabled={remaining === 0} variant="primary" onClick={() => setRunning(v => !v)}/>
     <Button label="Đặt lại 5:00" variant="secondary" onClick={() => { setRunning(false); setRemaining(300); }}/>
    </div>
    {remaining === 0 && <p role="status" style={{ color: '#f43f5e', fontWeight: 700, marginTop: 8 }}>Hết thời gian luyện nói 5 phút!</p>}
   </section>

   <div {...stylex.props(s.topics)}>
    {topics.map(item => (
     <Button key={item.id} label={`${item.num}. ${item.title}`} variant={topicId === item.id ? 'primary' : 'secondary'} size="sm" onClick={() => { setTopicId(item.id); setQuestionId(null); }}/>
    ))}
    <Button label={showHints ? 'Ẩn gợi ý ngữ pháp' : 'Hiện gợi ý ngữ pháp'} variant="ghost" size="sm" onClick={() => setShowHints(v => !v)}/>
   </div>

   {topic && (
    <div style={{ marginTop: 24 }}>
     <div style={{ marginBottom: 18 }}>
      <Badge label={topic.badge}/>
      <h2 style={{ fontSize: 24, fontWeight: 800, marginBlock: '8px 4px' }}>{topic.title} · {topic.titleJp}</h2>
      <p {...stylex.props(common.muted)}>{topic.desc}</p>
     </div>
     {questions.map(question => (
      <Card key={`${topic.id}-${question.id}`} {...stylex.props(s.question)}>
       <div {...stylex.props(s.jp)}>
        <span>{question.qJp}</span>
        <AudioButton text={question.qJp} label="Nghe câu hỏi"/>
       </div>
       <p style={{ color: 'var(--color-text-secondary)', fontSize: 15, margin: 0 }}>{question.qVi}</p>
       <div {...stylex.props(common.muted)} style={{ fontSize: 13 }}>Mục đích câu hỏi: {question.intent}</div>
       <div>
        <Button label={questionId === question.id ? 'Đóng câu trả lời mẫu' : 'Xem câu trả lời mẫu'} variant="secondary" size="sm" onClick={() => setQuestionId(id => id === question.id ? null : question.id)}/>
       </div>
       {questionId === question.id && question.sampleAnswers.map((answer, index) => (
        <div key={`${question.id}-${index}`} {...stylex.props(s.answer)}>
         <Badge label={answer.tag}/>
         <div {...stylex.props(s.jp)}>
          <span>{answer.jp}</span>
          <AudioButton text={answer.jp} label="Nghe câu trả lời"/>
         </div>
         <span style={{ color: 'var(--color-text-secondary)', fontSize: 14 }}>{answer.vi}</span>
         {showHints && <small {...stylex.props(common.muted)} style={{ color: '#6366f1' }}>{answer.keyPoints}</small>}
        </div>
       ))}
       {showHints && question.vocab.length > 0 && (
        <p {...stylex.props(common.muted)} style={{ fontSize: 13, borderTop: '1px solid var(--color-border)', paddingTop: 10, margin: 0 }}>
         Từ vựng gợi ý: {question.vocab.map(v => `${v.jp} - ${v.vi}`).join(' · ')}
        </p>
       )}
      </Card>
     ))}
    </div>
   )}
  </div>
 );
}
