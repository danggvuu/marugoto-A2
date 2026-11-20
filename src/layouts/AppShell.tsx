import { useEffect, useState, type ReactNode } from 'react';
import { Theme } from '@astryxdesign/core/theme';
import { neutralTheme } from '@astryxdesign/theme-neutral/built';
import { Button } from '@astryxdesign/core/Button';
import { BookOpen, GraduationCap, Home, Menu, Moon, Search, Sun, Target, X } from 'lucide-react';
import { Link, NavLink, Outlet, useLocation } from 'react-router-dom';
import * as stylex from '@stylexjs/stylex';
import { lessonCatalog } from '../services/lessonCatalog';
import { common } from '../styles/tokens.stylex';

const s = stylex.create({
 root: { minHeight: '100vh' },
 header: { position: 'sticky', top: 0, zIndex: 50, display: 'flex', alignItems: 'center', gap: 18, minHeight: 68, paddingInline: 24, borderBottomWidth: 1, borderBottomStyle: 'solid', borderBottomColor: 'var(--color-border)', backgroundColor: 'var(--color-background-surface)', '@media (max-width: 820px)': { paddingInline: 12, gap: 10, flexWrap: 'wrap', paddingBlock: 10 } },
 brand: { display: 'flex', alignItems: 'center', gap: 10, fontWeight: 800 },
 brandText: { '@media (max-width: 430px)': { fontSize: 13 } },
 logo: { width: 36, height: 36, borderRadius: 12, display: 'grid', placeItems: 'center', backgroundColor: 'var(--color-accent-muted)', fontSize: 18 },
 search: { height: 40, flex: 1, minWidth: 150, maxWidth: 520, display: 'flex', alignItems: 'center', gap: 10, paddingInline: 12, borderRadius: 12, borderWidth: 1, borderStyle: 'solid', borderColor: 'var(--color-border)', color: 'var(--color-text-secondary)', '@media (max-width: 820px)': { order: 4, flexBasis: '100%', maxWidth: '100%' } },
 input: { flex: 1, minWidth: 0, borderWidth: 0, backgroundColor: 'transparent', color: 'var(--color-text-primary)' },
 headerRight: { marginInlineStart: 'auto' },
 menu: { display: 'none', '@media (max-width: 820px)': { display: 'block' } },
 layout: { display: 'grid', gridTemplateColumns: '248px minmax(0,1fr)', '@media (max-width: 820px)': { gridTemplateColumns: 'minmax(0,1fr)' } },
 rail: { position: 'sticky', top: 68, height: 'calc(100dvh - 68px)', overflowY: 'auto', padding: 18, borderInlineEndWidth: 1, borderInlineEndStyle: 'solid', borderInlineEndColor: 'var(--color-border)', backgroundColor: 'var(--color-background-surface)', '@media (max-width: 820px)': { display: 'none' } },
 railOpen: { '@media (max-width: 820px)': { display: 'block', position: 'fixed', top: 118, bottom: 0, left: 0, width: 'min(320px, 90vw)', height: 'calc(100dvh - 118px)', zIndex: 40, boxShadow: '8px 0 24px rgba(0,0,0,.18)' } },
 railSection: { display: 'grid', gap: 5, marginBlockEnd: 22 },
 railTitle: { padding: '8px 10px', fontSize: 11, fontWeight: 800, color: 'var(--color-text-secondary)', letterSpacing: '.1em', textTransform: 'uppercase' },
 navLink: { display: 'flex', alignItems: 'center', gap: 10, borderRadius: 10, padding: '9px 10px', color: 'var(--color-text-secondary)', fontSize: 14 },
 navActive: { backgroundColor: 'var(--color-neutral)', color: 'var(--color-text-primary)', fontWeight: 700 },
 main: { minWidth: 0 },
 footer: { maxWidth: 1320, marginInline: 'auto', padding: '24px 24px 34px', color: 'var(--color-text-secondary)', fontSize: 12 },
});

export function AppShell() {
 const [mode, setMode] = useState<'light' | 'dark'>(() => { try { return localStorage.getItem('marugoto_theme') === 'dark' ? 'dark' : 'light'; } catch { return 'light'; } });
 const [query, setQuery] = useState('');
 const [menuOpen, setMenuOpen] = useState(false);
 const location = useLocation();
 useEffect(() => { try { localStorage.setItem('marugoto_theme', mode); } catch { /* storage may be blocked */ } }, [mode]);
 useEffect(() => { setMenuOpen(false); window.scrollTo(0, 0); }, [location.pathname]);
 useEffect(() => {
  const key = (event: KeyboardEvent) => {
   if (event.key === 'Escape') setMenuOpen(false);
   if (event.key === '/' && !(event.target instanceof HTMLInputElement) && !(event.target instanceof HTMLTextAreaElement) && !(event.target instanceof HTMLElement && event.target.isContentEditable)) {
    event.preventDefault(); document.getElementById('quick-search')?.focus();
   }
  };
  window.addEventListener('keydown', key); return () => window.removeEventListener('keydown', key);
 }, []);
 const filtered = lessonCatalog.filter(item => !query || `${item.title} ${item.topic} ${item.quote} ${item.level}`.toLowerCase().includes(query.toLowerCase()));
 return <Theme theme={neutralTheme} mode={mode}><div {...stylex.props(s.root)}>
  <a className="skip-link" href="#main-content">Đến nội dung chính</a>
  <header {...stylex.props(s.header)}>
   <div {...stylex.props(s.menu)}><Button label={menuOpen ? 'Đóng điều hướng' : 'Mở điều hướng'} variant="ghost" size="sm" isIconOnly icon={menuOpen ? <X size={19}/> : <Menu size={19}/>} onClick={() => setMenuOpen(v => !v)} aria-expanded={menuOpen} aria-controls="study-navigation"/></div>
   <Link to="/" {...stylex.props(s.brand)}><span {...stylex.props(s.logo)}>日</span><span {...stylex.props(s.brandText)}>Marugoto <span {...stylex.props(common.muted)}>Study Hub</span></span></Link>
   <div {...stylex.props(s.search)}><Search size={17}/><input id="quick-search" {...stylex.props(s.input)} value={query} onChange={e => { setQuery(e.target.value); if(e.target.value) setMenuOpen(true); }} placeholder="Tìm bài học tiếng Nhật hoặc tiếng Việt…" aria-label="Tìm kiếm nhanh"/><kbd>/</kbd></div>
   <div {...stylex.props(s.headerRight)}><Button label={mode === 'light' ? 'Bật chế độ tối' : 'Bật chế độ sáng'} variant="ghost" size="sm" isIconOnly icon={mode === 'light' ? <Moon size={17}/> : <Sun size={17}/>} onClick={() => setMode(v => v === 'light' ? 'dark' : 'light')}/></div>
  </header>
  <div {...stylex.props(s.layout)}>
   <aside id="study-navigation" {...stylex.props(s.rail, menuOpen && s.railOpen)}><nav aria-label="Điều hướng chính">
    <div {...stylex.props(s.railSection)}><span {...stylex.props(s.railTitle)}>Không gian học</span><ShellNav to="/" icon={<Home size={17}/>} label="Dashboard"/><ShellNav to="/kanji" icon={<GraduationCap size={17}/>} label="Trung tâm Kanji"/><ShellNav to="/tests" icon={<Target size={17}/>} label="Phòng thi & Mini test"/><ShellNav to="/kaiwa" icon={<BookOpen size={17}/>} label="Kaiwa 5 phút"/></div>
    {(['A2-1', 'A2-2'] as const).map(level => <div key={level} {...stylex.props(s.railSection)}><span {...stylex.props(s.railTitle)}>Marugoto {level}</span>{filtered.filter(item => item.level === level).map(item => <ShellNav key={`${level}-${item.number}`} to={`/lessons/${level.toLowerCase()}/${item.number}`} icon={<span>{item.icon}</span>} label={`${item.number}. ${item.title}`}/>)}</div>)}
    {!filtered.length && <p role="status">Không có bài phù hợp.</p>}
    <a href="/legacy_html/index.html" {...stylex.props(s.navLink)}>Kho tài liệu cũ (A1 và chuyên đề)</a>
   </nav></aside>
   <main id="main-content" tabIndex={-1} {...stylex.props(s.main)}><Outlet/><footer {...stylex.props(s.footer)}>Nội dung học tập Marugoto · Tiến độ lưu trong trình duyệt · Các bộ đề là tài liệu tự luyện, không phải đề JLPT chính thức.</footer></main>
  </div>
 </div></Theme>;
}
function ShellNav({to, icon, label}: {to: string; icon: ReactNode; label: string}) {
 return <NavLink end={to === '/'} to={to} className={({isActive}) => stylex.props(s.navLink, isActive && s.navActive).className}><span>{icon}</span><span>{label}</span></NavLink>;
}
