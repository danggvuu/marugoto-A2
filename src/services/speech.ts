export function speakJapanese(text: string) {
 if (!('speechSynthesis' in window)) return false;
 const clean = text.replace(/<[^>]*>/g, '').trim();
 if (!clean) return false;
 const utterance = new SpeechSynthesisUtterance(clean);
 utterance.lang = 'ja-JP';
 utterance.rate = 0.88;
 const voice = window.speechSynthesis.getVoices().find(item => /^ja(?:-|$)/i.test(item.lang));
 if (voice) utterance.voice = voice;
 window.speechSynthesis.cancel();
 window.speechSynthesis.speak(utterance);
 return true;
}
