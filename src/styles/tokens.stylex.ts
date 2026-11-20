import * as stylex from '@stylexjs/stylex';

export const tokens = stylex.defineVars({
  accent: 'var(--color-accent)',
  accentMuted: 'var(--color-accent-muted)',
  pageBackground: 'var(--color-background-body)',
  surface: 'var(--color-background-surface)',
  card: 'var(--color-background-card)',
  text: 'var(--color-text-primary)',
  muted: 'var(--color-text-secondary)',
  border: 'var(--color-border)',
  success: 'var(--color-success)',
  danger: 'var(--color-error)',
  radius: '16px',
  shadow: '0 12px 36px rgba(15, 23, 42, 0.08)',
});

export const common = stylex.create({
  page: { maxWidth: '1320px', marginInline: 'auto', padding: '32px 36px 72px', width: '100%' },
  section: { marginBlock: '28px' },
  sectionTitle: { fontSize: '22px', fontWeight: 700, letterSpacing: '-0.03em', marginBlockEnd: '14px' },
  muted: { color: tokens.muted },
  grid: { display: 'grid', gap: '16px' },
  card: { backgroundColor: tokens.card, borderWidth: 1, borderStyle: 'solid', borderColor: 'rgba(127,127,127,.18)', borderRadius: tokens.radius, boxShadow: tokens.shadow },
  eyebrow: { color: tokens.muted, fontSize: '12px', fontWeight: 700, letterSpacing: '.1em', textTransform: 'uppercase' },
  pill: { borderRadius: '999px', padding: '5px 10px', backgroundColor: tokens.accentMuted, color: tokens.text, fontSize: '12px', fontWeight: 700 },
});
