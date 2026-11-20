import { readFileSync, writeFileSync } from 'node:fs';
import { runInNewContext } from 'node:vm';
// Evaluate repository-owned data assignments only at regeneration time, never in the browser.
for(const [source,target,key] of [
 ['mini_11_14_data.js','mini_11_14.json','MINI_11_14_DATA'],
 ['mini_15_18_data.js','mini_15_18.json','MINI_15_18_DATA'],
]) {
 const context={window:{}};
 runInNewContext(readFileSync(new URL(`../assets/data/${source}`,import.meta.url),'utf8'),context,{timeout:1000});
 if(!context.window[key]) throw new Error(`Missing ${key}`);
 writeFileSync(new URL(`../data/${target}`,import.meta.url),JSON.stringify(context.window[key],null,2)+'\n');
}
console.log('Extracted both Mini Test datasets');
