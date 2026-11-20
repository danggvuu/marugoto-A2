import { Collapsible } from '@astryxdesign/core/Collapsible';
import { AudioButton } from '../common/AudioButton';
import type { GrammarEntry } from '../../types/study';
import * as stylex from '@stylexjs/stylex';
import { common } from '../../styles/tokens.stylex';
const s = stylex.create({ stack: { display: 'grid', gap: 12 }, formula: { borderInlineStartWidth: 4, borderInlineStartStyle: 'solid', borderInlineStartColor: 'var(--color-accent)', padding: '12px 16px', backgroundColor: 'var(--color-background-muted)', borderRadius: 10, fontWeight: 700, overflowWrap: 'anywhere' }, item: { display: 'flex', justifyContent: 'space-between', alignItems: 'start', gap: 12, borderTopWidth: 1, borderTopStyle: 'solid', borderTopColor: 'rgba(127,127,127,.18)', paddingBlock: 12 }, jp: { fontSize: 18, fontWeight: 650 } });
function plainText(html: string) { const element = document.createElement('div'); element.innerHTML = html; return element.textContent ?? ''; }
export function GrammarSection({ entries }: { entries: GrammarEntry[] }) {
  if (!entries.length) return <div {...stylex.props(common.card)} style={{ padding: 22 }}><p>Phần dữ liệu ngữ pháp theo bài đang được bổ sung. Nội dung sẽ không thay thế tài liệu bài học gốc.</p></div>;
  return <div {...stylex.props(s.stack)}>{entries.map(entry => <Collapsible key={entry.id} trigger={entry.title}><div {...stylex.props(s.stack)}><div {...stylex.props(s.formula)}>{plainText(entry.formula)}</div><p>{entry.meaning}</p>{entry.notes && <p {...stylex.props(common.muted)}>{entry.notes}</p>}{entry.examples.map((example, index) => <div key={`${entry.id}-${index}`} {...stylex.props(s.item)}><div><div {...stylex.props(s.jp)}>{example.jp}</div><div {...stylex.props(common.muted)}>{example.vi}</div></div><AudioButton text={example.jp} label={`Nghe ví dụ ${index + 1}`} /></div>)}</div></Collapsible>)}</div>;
}
