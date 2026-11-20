import { useEffect, useMemo, useState } from 'react';
import { Badge } from '@astryxdesign/core/Badge';
import { Button } from '@astryxdesign/core/Button';
import { Card } from '@astryxdesign/core/Card';
import { ArrowLeft, ArrowRight, Dices, Volume2 } from 'lucide-react';
import * as stylex from '@stylexjs/stylex';
import type { VocabEntry } from '../../types/study';
import { speakJapanese } from '../../services/speech';
import { tokens } from '../../styles/tokens.stylex';

const s = stylex.create({
  wrap: { display: 'grid', gridTemplateColumns: 'minmax(0, 1fr) 300px', gap: 22, alignItems: 'stretch', '@media (max-width: 760px)': { gridTemplateColumns: '1fr' } },
  card: { minHeight: 280, display: 'grid', placeItems: 'center', cursor: 'pointer', position: 'relative', overflow: 'hidden' },
  inner: { display: 'grid', placeItems: 'center', textAlign: 'center', gap: 14, width: '100%', minHeight: 245, padding: 28 },
  flipped: { },
  face: { display: 'grid', gap: 10, justifyItems: 'center' },
  back: { display: 'grid', alignContent: 'center', justifyItems: 'center', gap: 10 },
  jp: { fontSize: 'clamp(36px, 7vw, 58px)', lineHeight: 1.25, fontWeight: 750, letterSpacing: '.025em' },
  meaning: { fontSize: 22, fontWeight: 700 },
  aside: { display: 'grid', alignContent: 'start', gap: 12 },
  controls: { display: 'flex', gap: 8, flexWrap: 'wrap', alignItems: 'center' },
  progress: { height: 7, backgroundColor: 'var(--color-neutral)', borderRadius: 99, overflow: 'hidden' },
  fill: { height: '100%', backgroundColor: tokens.text, borderRadius: 99 },
  muted: { color: tokens.muted },
});

export function FlashcardDeck({ cards, onLearned }: { cards: VocabEntry[]; onLearned?: (id: string) => void }) {
  const [index, setIndex] = useState(0);
  const [flipped, setFlipped] = useState(false);
  const [autoPlay, setAutoPlay] = useState(false);
  const [shuffleKey, setShuffleKey] = useState(0);
  const ordered = useMemo(() => {
    if (!shuffleKey) return cards;
    const copy = [...cards];
    for (let i = copy.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [copy[i], copy[j]] = [copy[j], copy[i]]; }
    return copy;
  }, [cards, shuffleKey]);
  const card = ordered[index];
  useEffect(() => { setIndex(0); setFlipped(false); }, [cards]);
  useEffect(() => {
    if (!autoPlay || !card) return;
    speakJapanese(card.kana || card.jp);
    const flipTimer = window.setTimeout(() => setFlipped(true), 1800);
    const timer = window.setTimeout(() => { onLearned?.(card.id); setFlipped(false); setIndex(current => (current + 1) % ordered.length); }, 4000);
    return () => { window.clearTimeout(flipTimer); window.clearTimeout(timer); window.speechSynthesis?.cancel(); };
  }, [autoPlay, index, card, ordered.length, onLearned]);
  if (!card) return <Card padding={5}><p>Chưa có thẻ từ vựng cho bài này.</p></Card>;
  const next = () => { const following = (index + 1) % ordered.length; setIndex(following); setFlipped(false); onLearned?.(card.id); };
  const previous = () => { setIndex((index - 1 + ordered.length) % ordered.length); setFlipped(false); };
  return <div {...stylex.props(s.wrap)}>
    <Card {...stylex.props(s.card)} padding={4} onClick={() => setFlipped(value => !value)} role="button" tabIndex={0} onKeyDown={event => { if(event.key === 'Enter' || event.key === ' ') { event.preventDefault(); setFlipped(value => !value); } }} aria-pressed={flipped} aria-label={`Thẻ ${index + 1}: ${card.jp}. Bấm để lật`}>
      <div className={flipped ? 'flashcard-surface is-flipped' : 'flashcard-surface'}>
        <div className="flashcard-face" aria-hidden={flipped}><Badge label={`${index + 1} / ${ordered.length}`} />{card.icon&&<span aria-hidden="true">{card.icon}</span>}<span {...stylex.props(s.jp)}>{card.jp}</span><span {...stylex.props(s.muted)}>{card.kana}</span><small>Chạm để xem nghĩa</small></div>
        <div className="flashcard-face flashcard-back" aria-hidden={!flipped}><span {...stylex.props(s.meaning)}>{card.meaning}</span><span {...stylex.props(s.jp)}>{card.kanji}</span><span {...stylex.props(s.muted)}>{card.romaji}{card.hv ? ` · ${card.hv}` : ''}</span></div>
      </div>
    </Card>
    <div {...stylex.props(s.aside)}>
      <div><small {...stylex.props(s.muted)}>Tiến độ bộ thẻ</small><div {...stylex.props(s.progress)}><div {...stylex.props(s.fill)} style={{ width: `${((index + 1) / ordered.length) * 100}%` }} /></div></div>
      <div {...stylex.props(s.controls)}><Button label="Trước" size="sm" variant="secondary" icon={<ArrowLeft size={15} />} onClick={previous} /><Button label="Tiếp" size="sm" variant="primary" icon={<ArrowRight size={15} />} onClick={next} /><Button label="Nghe" size="sm" variant="ghost" isIconOnly icon={<Volume2 size={16} />} onClick={() => speakJapanese(card.kana || card.jp)} /><Button label="Xáo" size="sm" variant="ghost" isIconOnly icon={<Dices size={16} />} onClick={() => { setShuffleKey(k => k + 1); setIndex(0); setFlipped(false); }} /></div>
      <Button label={autoPlay ? 'Dừng tự động phát' : 'Tự động phát'} variant="secondary" onClick={() => setAutoPlay(value => !value)} />
      <div><strong>{card.meaning}</strong><p {...stylex.props(s.muted)}>{card.kana} · {card.romaji}</p></div>
      <span {...stylex.props(s.muted)}>Bài {card.lesson} · {card.level}</span>
    </div>
  </div>;
}
