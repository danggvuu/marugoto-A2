import { Button } from '@astryxdesign/core/Button';
import { Volume2 } from 'lucide-react';
import { speakJapanese } from '../../services/speech';

export function AudioButton({ text, label = 'Nghe phát âm' }: { text: string; label?: string }) {
  return <Button label={label} variant="ghost" size="sm" isIconOnly icon={<Volume2 size={17} />} onClick={() => speakJapanese(text)} />;
}
