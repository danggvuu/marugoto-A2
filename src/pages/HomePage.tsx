import { useEffect, useMemo, useState } from 'react';
import { Link } from 'react-router-dom';
import { Badge } from '@astryxdesign/core/Badge';
import { Button } from '@astryxdesign/core/Button';
import { Card } from '@astryxdesign/core/Card';
import { BarChart3, BookOpen, Brain, Clock3, Languages, Search, Sparkles, Target, Trophy } from 'lucide-react';
import * as stylex from '@stylexjs/stylex';
import { lessonCatalog } from '../services/lessonCatalog';
import { a2_1VocabularyTotal, a2_2VocabularyTotal, allKanji, lessonSummaries } from '../services/dataLoader';
import { useStudyProgress } from '../services/progress';
import { common } from '../styles/tokens.stylex';

const s = stylex.create({
 page: { maxWidth: 1320, margin: '0 auto', padding: '32px 36px 52px' },
 hero: { position: 'relative', overflow: 'hidden', padding: 38, borderRadius: 24, backgroundColor: '#1e1b4b', backgroundImage: 'linear-gradient(135deg, #1e1b4b 0%, #312e81 45%, #4338ca 100%)', color: '#ffffff', boxShadow: '0 20px 45px -12px rgba(30, 27, 75, 0.35)', borderWidth: 1, borderStyle: 'solid', borderColor: 'rgba(255, 255, 255, 0.12)' },
 heroTitle: { fontSize: 'clamp(32px, 5vw, 52px)', fontWeight: 850, lineHeight: 1.12, maxWidth: 760, marginBlock: '14px', letterSpacing: '-.03em', color: '#ffffff' },
 heroText: { maxWidth: 660, color: '#e0e7ff', fontSize: 16, lineHeight: 1.65 },
 heroActions: { display: 'flex', gap: 12, flexWrap: 'wrap', marginTop: 26 },
 stats: { display: 'grid', gridTemplateColumns: 'repeat(4, minmax(0, 1fr))', gap: 14, marginBlock: '24px', '@media (max-width: 760px)': { gridTemplateColumns: 'repeat(2, minmax(0, 1fr))' } },
 stat: { padding: 20, borderRadius: 18, backgroundColor: 'var(--color-background-card)', borderWidth: 1.5, borderStyle: 'solid', borderColor: 'var(--color-border)', boxShadow: '0 4px 20px -2px rgba(15, 23, 42, 0.05)' },
 statValue: { fontSize: 30, fontWeight: 850, color: '#4f46e5', marginTop: 6 },
 controls: { display: 'flex', gap: 10, flexWrap: 'wrap', alignItems: 'center', justifyContent: 'space-between' },
 search: { display: 'flex', gap: 8, alignItems: 'center', borderWidth: 1.5, borderStyle: 'solid', borderColor: 'var(--color-border)', borderRadius: 12, padding: '9px 12px', minWidth: 260, backgroundColor: 'var(--color-background-card)' },
 input: { backgroundColor: 'transparent', borderWidth: 0, outline: 0, color: 'var(--color-text-primary)' },
 grid: { display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(245px, 1fr))', gap: 16, marginTop: 18 },
 lesson: { padding: 20, display: 'grid', gap: 12, borderRadius: 16, backgroundColor: 'var(--color-background-card)', borderWidth: 1.5, borderStyle: 'solid', borderColor: 'var(--color-border)', borderLeftWidth: 4, borderLeftStyle: 'solid', borderLeftColor: '#6366f1', boxShadow: '0 4px 16px -2px rgba(15, 23, 42, 0.04)' },
 lessonTitle: { fontWeight: 800, fontSize: 17, color: 'var(--color-text-primary)' },
 topic: { fontSize: 12, fontWeight: 700, color: '#6366f1' },
 progress: { display: 'flex', gap: 8, flexWrap: 'wrap', marginBlock: '12px' },
 shortcut: { padding: 18, display: 'grid', gap: 10, borderRadius: 16, backgroundColor: 'var(--color-background-card)', borderWidth: 1.5, borderStyle: 'solid', borderColor: 'var(--color-border)', borderLeftWidth: 4, borderLeftStyle: 'solid', borderLeftColor: '#ec4899', boxShadow: '0 4px 16px -2px rgba(15, 23, 42, 0.04)' }
});

export function HomePage() {
 const [scope, setScope] = useState<'A2-1' | 'A2-2' | 'all'>('all');
 const [query, setQuery] = useState('');
 const { progress, setLastLesson } = useStudyProgress();
 const lessons = useMemo(() => lessonCatalog.filter(item => (scope === 'all' || item.level === scope) && (!query || `${item.title} ${item.topic} ${item.quote}`.toLowerCase().includes(query.toLowerCase()))), [scope, query]);
 const resume = progress.lastLesson ? `/lessons/${progress.lastLesson}` : '/lessons/a2-1/1';
 useEffect(() => { if (!progress.lastLesson) setLastLesson('a2-1/1'); }, [progress.lastLesson, setLastLesson]);

 return <div {...stylex.props(s.page)}>
  <section {...stylex.props(s.hero)}>
   <Badge label="MARUGOTO · A1—A2 TỔNG HỢP"/>
   <h1 {...stylex.props(s.heroTitle)}>Học tiếng Nhật,<br/>từng bước chắc chắn.</h1>
   <p {...stylex.props(s.heroText)}>Học theo giáo trình chuẩn Marugoto bằng tiếng Việt với Flashcard 3D, âm thanh giọng đọc Tokyo, Kanji bút thuận và bộ đề thi thực chiến có giải thích chi tiết.</p>
   <div {...stylex.props(s.heroActions)}>
    <Link to={resume}><Button label="Tiếp tục học bài gần nhất" variant="primary"/></Link>
    <Link to="/tests"><Button label="Mở phòng luyện thi" variant="secondary"/></Link>
    <Link to="/kanji"><Button label="Tra cứu chữ Hán" variant="secondary"/></Link>
   </div>
  </section>

  <section {...stylex.props(s.stats)}>
   <Stat icon={<BookOpen color="#4f46e5"/>} label={`Từ vựng A2-1 (${a2_1VocabularyTotal}) + A2-2 (${a2_2VocabularyTotal})`} value={(a2_1VocabularyTotal + a2_2VocabularyTotal).toLocaleString('vi-VN')}/>
   <Stat icon={<Brain color="#e11d48"/>} label={`Mục từ ghép Kanji (${allKanji.length})`} value={allKanji.length}/>
   <Stat icon={<Target color="#059669"/>} label="Bài đã hoàn thành" value={progress.completedLessons.length}/>
   <Stat icon={<Trophy color="#d97706"/>} label="Lượt làm đề thi" value={progress.quizAttempts}/>
  </section>

  <section {...stylex.props(s.progress)} aria-label="Tiến độ cá nhân">
   <Badge label={`${progress.vocab.length} từ đã học`}/>
   <Badge label={`${progress.kanji.length} mục Kanji đã nhớ`}/>
   <Badge label={`Điểm quiz cao nhất: ${progress.bestScore}%`}/>
  </section>

  <section style={{ marginTop: 24 }}>
   <div {...stylex.props(s.controls)}>
    <div>
     <span {...stylex.props(common.eyebrow)}>Lộ trình học tập</span>
     <h2 {...stylex.props(common.sectionTitle)}>Chọn một bài để bắt đầu học</h2>
    </div>
    <label {...stylex.props(s.search)}>
     <Search size={17} color="#64748b"/>
     <input {...stylex.props(s.input)} value={query} onChange={e => setQuery(e.target.value)} placeholder="Tìm kiếm bài học…"/>
    </label>
   </div>

   <div {...stylex.props(s.progress)}>
    {(['all', 'A2-1', 'A2-2'] as const).map(item => (
     <Button key={item} label={item === 'all' ? 'Tất cả 36 bài' : `Marugoto ${item}`} variant={scope === item ? 'primary' : 'secondary'} size="sm" onClick={() => setScope(item)}/>
    ))}
   </div>

   {(['A2-1', 'A2-2'] as const).filter(group => scope === 'all' || scope === group).map(group => (
    <div key={group} style={{ marginTop: 20 }}>
     <h3 {...stylex.props(common.sectionTitle)} style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
      {group === 'A2-1' ? '🌸 Marugoto A2-1 (Tập 1)' : '🌺 Marugoto A2-2 (Tập 2)'}
      <Badge label={`${lessonCatalog.filter(x => x.level === group).length} bài`}/>
     </h3>
     <div {...stylex.props(s.grid)}>
      {lessons.filter(item => item.level === group).map(item => {
       const lesson = lessonSummaries.find(x => x.level === group && x.number === item.number);
       const borderColor = group === 'A2-1' ? '#6366f1' : '#ec4899';
       return (
        <Card key={`${item.level}-${item.number}`} {...stylex.props(s.lesson)} style={{ borderLeftColor: borderColor }}>
         <div {...stylex.props(s.controls)}>
          <Badge label={`Bài ${item.number}`}/>
          <span style={{ fontSize: 20 }}>{item.icon}</span>
         </div>
         <div>
          <div {...stylex.props(s.topic)} style={{ color: borderColor }}>{item.topic}</div>
          <div {...stylex.props(s.lessonTitle)}>{item.title}</div>
          <p {...stylex.props(common.muted)} style={{ marginTop: 4, fontSize: 13 }}>{item.quote}</p>
         </div>
         <small style={{ color: 'var(--color-text-secondary)', fontWeight: 600 }}>
          {lesson?.vocab.length ?? 0} từ · {lesson?.grammar.length ?? 0} ngữ pháp · {lesson?.kanji.length ?? 0} Kanji
         </small>
         <Link to={`/lessons/${group.toLowerCase()}/${item.number}`}>
          <Button label="Vào học ngay" variant="secondary" width="100%"/>
         </Link>
        </Card>
       );
      })}
     </div>
    </div>
   ))}
  </section>

  <section style={{ marginTop: 36, padding: 24, borderRadius: 20, backgroundColor: 'var(--color-background-card)', borderWidth: 1.5, borderStyle: 'solid', borderColor: 'var(--color-border)' }}>
   <h2 {...stylex.props(common.sectionTitle)}>Marugoto A1 · Khởi động căn bản</h2>
   <p {...stylex.props(common.muted)}>Ôn lại toàn bộ nền tảng A1 trước khi bắt đầu A2. Kho bài học A1 và chuyên đề được lưu trữ đầy đủ trong thư viện tài liệu.</p>
   <a href="/legacy_html/Tu_Vung_Marugoto_A1_16_A2_1_10.html" style={{ display: 'inline-block', marginTop: 12 }}>
    <Button label="Mở kho tài liệu nền tảng A1" variant="secondary"/>
   </a>
  </section>

  <section style={{ marginTop: 36 }}>
   <h2 {...stylex.props(common.sectionTitle)}>Lối tắt ôn tập nhanh</h2>
   <div {...stylex.props(s.grid)}>
    <Shortcut to="/kanji" icon={<Languages color="#e11d48"/>} title="Trung tâm Kanji" text="Tra cứu theo bài, nghe âm On/Kun và luyện viết nét."/>
    <Shortcut to="/tests" icon={<Target color="#4f46e5"/>} title="Phòng luyện thi" text="Làm đề thi thử tổng hợp có tính giờ và xem giải thích."/>
    <Shortcut to="/kaiwa" icon={<Sparkles color="#d97706"/>} title="Kaiwa 5 phút" text="Luyện phản xạ hội thoại theo các chủ đề thực chiến."/>
    <Shortcut to="/lessons/a2-2/1" icon={<Clock3 color="#059669"/>} title="Bài học A2-2 mới" text="Khám phá ngay 18 bài học A2-2 với 439 từ vựng."/>
   </div>
  </section>
  <span hidden><BarChart3/></span>
 </div>;
}

function Stat({ icon, label, value }: { icon: React.ReactNode; label: string; value: string | number }) {
 return (
  <Card {...stylex.props(s.stat)}>
   <div {...stylex.props(s.controls)}>
    {icon}
    <span style={{ fontSize: 13, fontWeight: 600, color: 'var(--color-text-secondary)' }}>{label}</span>
   </div>
   <div {...stylex.props(s.statValue)}>{value}</div>
  </Card>
 );
}

function Shortcut({ to, icon, title, text }: { to: string; icon: React.ReactNode; title: string; text: string }) {
 return (
  <Link to={to} style={{ textDecoration: 'none' }}>
   <Card {...stylex.props(s.shortcut)}>
    <div {...stylex.props(s.controls)}>
     {icon}
     <strong style={{ fontSize: 15, color: 'var(--color-text-primary)' }}>{title}</strong>
    </div>
    <span {...stylex.props(common.muted)} style={{ fontSize: 13, lineHeight: 1.5 }}>{text}</span>
   </Card>
  </Link>
 );
}
