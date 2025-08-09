import {remark} from 'remark';
import gfm from 'remark-gfm';
import preset from 'remark-preset-lint-recommended';

const input = process.env.MD || '# Title\n\nBad  text';
const file = await remark().use(preset).use(gfm).process(input);

const messages = file.messages.map(m => ({rule: m.ruleId, reason: m.reason}));
console.log(JSON.stringify({status: 'pass', messages}));
