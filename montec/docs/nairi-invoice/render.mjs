import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs'
const D = '/tmp/claude-0/-home-user-memorycare/a7d25ab7-e8fd-5eb0-a214-0111f2d2bb64/scratchpad/invoice/'
const name = process.argv[2]
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' })
const p = await b.newPage()
await p.goto('file://' + D + name + '.html', { waitUntil: 'networkidle' })
await p.waitForTimeout(700)
await p.pdf({ path: D + name + '.pdf', width: '210mm', height: '297mm', printBackground: true })
await b.close()
console.log('pdf ok')
