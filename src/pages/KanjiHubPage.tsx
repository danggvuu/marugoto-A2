import { useMemo, useState } from 'react';
import { Badge } from '@astryxdesign/core/Badge';
import { Button } from '@astryxdesign/core/Button';
import { Search } from 'lucide-react';
import * as stylex from '@stylexjs/stylex';
import { allKanji } from '../services/dataLoader';
import { useStudyProgress } from '../services/progress';
import { FlashcardDeck } from '../components/flashcard/FlashcardDeck';
import { KanjiCard } from '../components/kanji/KanjiCard';
import { common } from '../styles/tokens.stylex';

const s = stylex.create({
 page: { maxWidth: 1320, margin: '0 auto', padding: '32px 36px 60px' },
 hero: { padding: 32, borderRadius: 24, backgroundColor: '#1e1b4b', backgroundImage: 'linear-gradient(135deg, #1e1b4b 0%, #312e81 40%, #4338ca 100%)', color: '#ffffff', boxShadow: '0 20px 45px -12px rgba(30, 27, 75, 0.35)', borderWidth: 1, borderStyle: 'solid', borderColor: 'rgba(255, 255, 255, 0.12)' },
 controls: { display: 'flex', gap: 10, flexWrap: 'wrap', alignItems: 'center', marginBlock: '22px' },
 search: { display: 'flex', alignItems: 'center', gap: 8, borderWidth: 1.5, borderStyle: 'solid', borderColor: 'var(--color-border)', borderRadius: 12, padding: '9px 12px', minWidth: 260, backgroundColor: 'var(--color-background-card)' },
 input: { borderWidth: 0, outline: 0, backgroundColor: 'transparent', color: 'var(--color-text-primary)' },
 grid: { display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(270px, 1fr))', gap: 16 },
 empty: { padding: 24 }
});

export function KanjiHubPage() {
 const [scope, setScope] = useState<'all' | 'A2-1' | 'A2-2'>('all');
 const [lesson, setLesson] = useState('all');
 const [query, setQuery] = useState('');
 const [flashcards, setFlashcards] = useState(false);
 const [round, setRound] = useState(0);
 const { markKanji } = useStudyProgress();

 const visible = useMemo(() => allKanji.filter(entry => (scope === 'all' || entry.level === scope) && (lesson === 'all' || entry.lesson === Number(lesson)) && (!query || `${entry.word} ${entry.kana} ${entry.meaning}`.toLowerCase().includes(query.toLowerCase()))), [scope, lesson, query]);
 const deck = useMemo(() => visible.map(entry => ({ id: entry.id, level: entry.level, lesson: entry.lesson, jp: entry.word, kana: entry.kana, kanji: entry.word, romaji: '', meaning: entry.meaning })), [visible]);

 return <div {...stylex.props(s.page)}>
  <section {...stylex.props(s.hero)}>
   <Badge label="KANJI HUB · A2-1 + A2-2 TOÀN DIỆN"/>
   <h1 style={{ fontSize: 'clamp(28px, 4vw, 42px)', fontWeight: 850, marginBlock: '12px 6px', color: '#ffffff' }}>⛩️ Trung tâm Chữ Hán Kanji</h1>
   <p style={{ color: '#e0e7ff', fontSize: 16, maxWidth: 640 }}>Tra cứu toàn bộ 291 từ ghép Kanji chuẩn giáo trình, nghe phát âm On/Kun và luyện nhớ nhanh bằng thẻ lật tương tác.</p>
   <div style={{ marginTop: 14 }}>
    <Badge label={`${visible.length} mục Kanji đang hiển thị`}/>
   </div>
  </section>

  <div {...stylex.props(s.controls)}>
   {(['all', 'A2-1', 'A2-2'] as const).map(item => (
    <Button key={item} label={item === 'all' ? 'Tất cả cấp độ' : `Marugoto ${item}`} variant={scope === item ? 'primary' : 'secondary'} size="sm" onClick={() => { setScope(item); setLesson('all'); }}/>
   ))}
   <select aria-label="Lọc bài" value={lesson} onChange={e => setLesson(e.target.value)} style={{ padding: '8px 12px', borderRadius: 10, border: '1.5px solid var(--color-border)', backgroundColor: 'var(--color-background-card)', color: 'var(--color-text-primary)', font: 'inherit' }}>
    <option value="all">Tất cả 18 bài</option>
    {Array.from({ length: 18 }, (_, i) => <option key={i + 1} value={i + 1}>Bài {i + 1}</option>)}
   </select>
   <label {...stylex.props(s.search)}>
    <Search size={16} color="#64748b"/>
    <input {...stylex.props(s.input)} value={query} onChange={e => setQuery(e.target.value)} placeholder="Tìm chữ Hán, Hiragana, âm Hán Việt…"/>
   </label>
   <Button label={flashcards ? 'Đóng chế độ Flashcard' : '🎴 Ôn Flashcard Kanji'} variant={flashcards ? 'primary' : 'secondary'} onClick={() => { setFlashcards(v => !v); setRound(v => v + 1); }}/>
  </div>

  {flashcards && <p {...stylex.props(common.muted)} style={{ marginBottom: 16 }}>Đang ôn thẻ Flashcard · {deck.length} mục trong bộ lọc</p>}
  {flashcards ? <FlashcardDeck key={round} cards={deck} onLearned={markKanji}/> : <div {...stylex.props(s.grid)}>{visible.map(entry => <KanjiCard key={entry.id} entry={entry} onLearned={markKanji}/>)}</div>}
  {!deck.length && <div {...stylex.props(s.empty)}>Không tìm thấy kết quả phù hợp.</div>}
 </div>;
}
