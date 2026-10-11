#!/usr/bin/env python3
"""Rebuild index.html from apps.json:  python3 build.py"""
import json, html, os
H=os.path.dirname(os.path.abspath(__file__))
d=json.load(open(os.path.join(H,'apps.json')))
e=html.escape
cards=[]
for a in d['apps']:
    note='' if a.get('phone_ready',True) else '<span class="badge">Private · Google Drive</span>'
    cards.append(f'''<a class="card" href="{e(a['url'])}" target="_blank" rel="noopener">
  <div class="icon">{e(a.get('emoji','🔗'))}</div>
  <div class="body"><div class="name">{e(a['name'])}</div>
  <div class="bot">by {e(a['bot'])} bot</div>
  <div class="desc">{e(a['description'])}</div>{note}</div>
  <div class="go">›</div></a>''')
page=f'''<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(d['title'])}</title>
<meta name="robots" content="noindex, nofollow">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Joe's Hub">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="theme-color" content="#0f172a">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="icon" type="image/png" href="apple-touch-icon.png">
<style>
*{{box-sizing:border-box}}
body{{margin:0;font-family:-apple-system,BlinkMacSystemFont,"SF Pro Text",Segoe UI,Roboto,sans-serif;background:#0f172a;color:#e2e8f0;
padding:calc(env(safe-area-inset-top) + 28px) 18px calc(env(safe-area-inset-bottom) + 28px)}}
.wrap{{max-width:560px;margin:0 auto}}
h1{{font-size:34px;margin:0 0 4px;letter-spacing:-.5px;color:#fff}}
.sub{{color:#94a3b8;margin:0 0 24px;font-size:15px}}
.card{{display:flex;align-items:center;gap:14px;background:#1e293b;border-radius:18px;padding:18px 16px;margin-bottom:14px;
text-decoration:none;color:inherit;min-height:96px;box-shadow:0 1px 0 rgba(255,255,255,.04) inset;-webkit-tap-highlight-color:transparent;transition:transform .08s}}
.card:active{{transform:scale(.98);background:#273449}}
.icon{{font-size:30px;width:56px;height:56px;flex:none;display:flex;align-items:center;justify-content:center;background:#334155;border-radius:14px}}
.body{{flex:1;min-width:0}}
.name{{font-size:18px;font-weight:650;color:#fff}}
.bot{{font-size:13px;color:#38bdf8;margin:2px 0 6px}}
.desc{{font-size:14px;line-height:1.35;color:#cbd5e1}}
.badge{{display:inline-block;margin-top:8px;font-size:12px;padding:3px 8px;border-radius:999px;background:#422006;color:#fbbf24}}
.go{{font-size:30px;color:#64748b;flex:none}}
footer{{color:#64748b;font-size:12px;text-align:center;margin-top:22px}}
</style></head><body><div class="wrap">
<h1>{e(d['title'])}</h1>
<p class="sub">Everything your bots have built, in one place.</p>
{chr(10).join(cards)}
<footer>Updated {e(d['updated'])} · Ask Grok Bot for “hub” to refresh</footer>
</div></body></html>
'''
open(os.path.join(H,'index.html'),'w').write(page)
print('ok', len(d['apps']))
