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
const s=stylex.create({page:{maxWidth:1320,margin:'0 auto',padding:'32px 36px 60px'},hero:{padding:26,borderRadius:20,backgroundColor:'#38383d',color:'white'},controls:{display:'flex',gap:9,flexWrap:'wrap',alignItems:'center',marginBlock:'18px'},search:{display:'flex',alignItems:'center',gap:8,borderWidth: 1, borderStyle: 'solid', borderColor: 'rgba(127,127,127,.25)',borderRadius:10,padding:'9px 12px',minWidth:240},input:{borderWidth: 0,outline:0,backgroundColor:'transparent',color:'var(--color-text-primary)'},grid:{display:'grid',gridTemplateColumns:'repeat(auto-fill,minmax(270px,1fr))',gap:14},empty:{padding:24}});
export function KanjiHubPage(){
 const[scope,setScope]=useState<'all'|'A2-1'|'A2-2'>('all'),[lesson,setLesson]=useState('all'),[query,setQuery]=useState(''),[flashcards,setFlashcards]=useState(false),[round,setRound]=useState(0);const{markKanji}=useStudyProgress();
 const visible=useMemo(()=>allKanji.filter(entry=>(scope==='all'||entry.level===scope)&&(lesson==='all'||entry.lesson===Number(lesson))&&(!query||`${entry.word} ${entry.kana} ${entry.meaning}`.toLowerCase().includes(query.toLowerCase()))),[scope,lesson,query]);
 const deck=useMemo(()=>visible.map(entry=>({id:entry.id,level:entry.level,lesson:entry.lesson,jp:entry.word,kana:entry.kana,kanji:entry.word,romaji:'',meaning:entry.meaning})),[visible]);
 return <div {...stylex.props(s.page)}><section {...stylex.props(s.hero)}><Badge label="KANJI HUB · A2-1 + A2-2"/><h1>Trung tâm Kanji</h1><p>Tra cứu từ ghép theo bài, mở chi tiết chữ Hán và tập viết tự do.</p><strong>{visible.length} mục đang hiển thị</strong></section><div {...stylex.props(s.controls)}>{(['all','A2-1','A2-2'] as const).map(item=><Button key={item} label={item==='all'?'Tất cả cấp độ':item} variant={scope===item?'primary':'secondary'} size="sm" onClick={()=>{setScope(item);setLesson('all');}}/>)}<select aria-label="Lọc bài" value={lesson} onChange={e=>setLesson(e.target.value)}><option value="all">Tất cả bài</option>{Array.from({length:18},(_,i)=><option key={i+1} value={i+1}>Bài {i+1}</option>)}</select><label {...stylex.props(s.search)}><Search size={16}/><input {...stylex.props(s.input)} value={query} onChange={e=>setQuery(e.target.value)} placeholder="Tìm Kanji, kana, nghĩa"/></label><Button label={flashcards?'Đóng chế độ ôn thẻ':'Ôn flashcard Kanji'} variant={flashcards?'primary':'secondary'} onClick={()=>{setFlashcards(v=>!v);setRound(v=>v+1);}}/></div>{flashcards&&<p {...stylex.props(common.muted)}>Chế độ ôn thẻ · {deck.length} mục trong bộ lọc</p>}{flashcards?<FlashcardDeck key={round} cards={deck} onLearned={markKanji}/>:<div {...stylex.props(s.grid)}>{visible.map(entry=><KanjiCard key={entry.id} entry={entry} onLearned={markKanji}/>)}</div>}{!deck.length&&<div {...stylex.props(s.empty)}>Không tìm thấy kết quả phù hợp.</div>}</div>;
}
