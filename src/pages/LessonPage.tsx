import { useEffect, useState } from 'react';
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
const s=stylex.create({page:{maxWidth:1320,margin:'0 auto',padding:'30px 36px 60px'},hero:{padding:28,borderRadius:22,backgroundColor:'#383838',color:'#fff'},crumb:{display:'flex',alignItems:'center',gap:7,color:'#ddd',fontSize:13},title:{fontSize:'clamp(30px,4vw,48px)',lineHeight:1.1,marginBlock:'14px 8px'},quote:{fontSize:19,color:'#eee'},stats:{display:'flex',gap:8,flexWrap:'wrap',marginTop:22},tabs:{display:'flex',gap:7,flexWrap:'wrap',marginBlock:'22px'},section:{marginBlock:'30px'},grid:{display:'grid',gridTemplateColumns:'repeat(auto-fill,minmax(260px,1fr))',gap:14},heading:{display:'flex',justifyContent:'space-between',alignItems:'center',gap:12}});
export function LessonPage(){
 const{level='a2-1',id='1'}=useParams();
 return <LessonContent key={`${level}/${id}`} level={level} number={Number(id)}/>;
}
function LessonContent({level,number}:{level:string;number:number}){
 const lesson=getLesson(level,number);const[tab,setTab]=useState('flashcards');const{markVocab,markKanji,recordQuiz,setLastLesson}=useStudyProgress();const navigate=useNavigate();
 const key=`${lesson?.level.toLowerCase()??level}/${number}`;
 useEffect(()=>{if(lesson)setLastLesson(key);},[lesson,key,setLastLesson]);
 const next=lessonCatalog.find(x=>x.level===lesson?.level&&x.number===number+1);
 if(!lesson)return <div {...stylex.props(common.page)}><h1>Không tìm thấy bài học</h1><p>Hãy quay về dashboard và chọn bài khác.</p></div>;
 const tabs=[['flashcards','Từ vựng'],['grammar','Ngữ pháp'],['kanji','Kanji'],['quiz','Mini test'],['typing','Luyện gõ']];
 return <div {...stylex.props(s.page)}><section {...stylex.props(s.hero)}><div {...stylex.props(s.crumb)}><span>{lesson.level}</span><ChevronRight size={15}/><span>{lesson.topic}</span></div><h1 {...stylex.props(s.title)}>{lesson.icon} Bài {number}: {lesson.title}</h1><p {...stylex.props(s.quote)}>{lesson.quote}<Button label="Nghe câu chủ đề" variant="ghost" size="sm" isIconOnly icon={<Volume2 size={17}/>} onClick={()=>speakJapanese(lesson.quote)}/></p><p>{lesson.subtitle}</p><div {...stylex.props(s.stats)}><Badge label={`${lesson.vocab.length} từ`}/><Badge label={`${lesson.grammar.length} mẫu ngữ pháp`}/><Badge label={`${lesson.kanji.length} mục Kanji`}/><Badge label={`${lesson.quiz.length} câu quiz`}/></div></section>
  <nav {...stylex.props(s.tabs)} aria-label="Mục bài học">{tabs.map(([id,label])=><Button key={id} label={label} size="sm" variant={tab===id?'primary':'secondary'} onClick={()=>setTab(id)}/>)}</nav>
  {tab==='flashcards'&&<section {...stylex.props(s.section)}><div {...stylex.props(s.heading)}><h2 {...stylex.props(common.sectionTitle)}><BookOpen size={20}/> Flashcard studio</h2><Badge label="Lật · Nghe · Xáo"/></div><FlashcardDeck cards={lesson.vocab} onLearned={markVocab}/></section>}
  {tab==='grammar'&&<section {...stylex.props(s.section)}><div {...stylex.props(s.heading)}><h2 {...stylex.props(common.sectionTitle)}>Cẩm nang ngữ pháp</h2><Badge label={`${lesson.grammar.length} mục nguồn`}/></div><GrammarSection entries={lesson.grammar}/></section>}
  {tab==='kanji'&&<section {...stylex.props(s.section)}><div {...stylex.props(s.heading)}><h2 {...stylex.props(common.sectionTitle)}><Languages size={20}/> Kho chữ Hán của bài</h2><Badge label={`${lesson.kanji.length} mục`}/></div><div {...stylex.props(s.grid)}>{lesson.kanji.map(entry=><KanjiCard key={entry.id} entry={entry} onLearned={markKanji}/>)}</div></section>}
  {tab==='quiz'&&<section {...stylex.props(s.section)}><h2 {...stylex.props(common.sectionTitle)}>Đấu trường trắc nghiệm</h2><QuizEngine questions={lesson.quiz} onComplete={score=>recordQuiz(score,key)}/></section>}
  {tab==='typing'&&<section {...stylex.props(s.section)}><h2 {...stylex.props(common.sectionTitle)}><PenLine size={20}/> Typing Studio</h2><TypingPractice words={lesson.vocab}/></section>}
  <section {...stylex.props(s.stats)}><Button label="Về dashboard" variant="secondary" onClick={()=>navigate('/')}/>{next&&<Link to={`/lessons/${next.level.toLowerCase()}/${next.number}`}><Button label={`Bài tiếp: ${next.title}`} variant="primary"/></Link>}</section>
 </div>;
}
