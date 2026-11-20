import { useState } from 'react';
import { Button } from '@astryxdesign/core/Button';
import { Card } from '@astryxdesign/core/Card';
import type { VocabEntry } from '../../types/study';
import * as stylex from '@stylexjs/stylex';
const s=stylex.create({card:{padding:20,display:'grid',gap:14},prompt:{fontSize:22,fontWeight:700},input:{borderWidth: 1, borderStyle: 'solid', borderColor: 'rgba(127,127,127,.3)',borderRadius:10,backgroundColor:'transparent',color:'var(--color-text-primary)',padding:'12px 14px',width:'100%'}});
export function TypingPractice({words}:{words:VocabEntry[]}) {
 const[index,setIndex]=useState(0),[value,setValue]=useState(''),[checked,setChecked]=useState(false);const item=words[index];
 if(!item)return <Card padding={5}><p>Chưa có từ để luyện gõ.</p></Card>;
 const normalize=(text:string)=>text.trim().normalize('NFKC');const correct=normalize(value)===normalize(item.kana)||normalize(value)===normalize(item.jp);
 return <div {...stylex.props(s.card)}><span>{index+1}/{words.length} · Romaji</span><div {...stylex.props(s.prompt)}>{item.romaji}</div><p>{item.meaning}</p><input {...stylex.props(s.input)} value={value} onChange={e=>{setValue(e.target.value);setChecked(false);}} onKeyDown={e=>{if(e.key==='Enter')setChecked(true);}} placeholder="Gõ bằng kana/kanji…" aria-label="Đáp án kana hoặc kanji"/>{checked&&<strong>{correct?'Chính xác!':`Đáp án: ${item.kana}`}</strong>}<div><Button label="Kiểm tra" onClick={()=>setChecked(true)}/><Button label="Bỏ qua" variant="secondary" onClick={()=>{setIndex(i=>(i+1)%words.length);setValue('');setChecked(false);}}/></div></div>;
}
