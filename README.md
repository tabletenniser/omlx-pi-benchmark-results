# Pi CLI + oMLX: local model benchmark results

**Ten models × ten daily tasks × 3 trials = 300 scored observations.** Public, compact results repository. No credentials or model weights. Earlier benchmark results are included as compressed downloads.

All benchmarks were run locally on an **Apple M1 Max machine with 64 GB of RAM (unified memory)**. macOS 26.6.2, Pi 1.4.0, GWS 0.22.5. Collected October 26–27, 2026 (America/Los_Angeles). All models/questions ran sequentially.

## Model summary

Both tables are sorted by **combined score across all 3 trials, out of 30**, highest first. Ties use Trial #3 score descending, then collection order. Trial #1 retains the original six questions plus four additions. Subsequent trials are fresh runs of all ten. Scores require all task checks and normal completion within **600 seconds / 12 model requests**. Score links open each trial’s failures.

**All 3 trials total E2E** sums all 30 case runtimes per model. Each trial’s **total E2E** sums its ten cases. Both include failures and repairs and exclude model load/warmup/grading. Rates are weighted native engine measurements: input excludes cached tokens; output includes thinking.

*Scroll horizontally within each table to see all columns.*

<table>
<thead>
<tr>
<th nowrap scope="col">Model</th>
<th nowrap scope="col">Combined<br>score /30</th>
<th nowrap scope="col">All 3 trials<br>total E2E (m:ss)</th>
<th nowrap scope="col">Trial #1<br>score /10</th>
<th nowrap scope="col">Trial #1<br>total E2E (m:ss)</th>
<th nowrap scope="col">Trial #1<br>input tok/s</th>
<th nowrap scope="col">Trial #1<br>output tok/s</th>
<th nowrap scope="col">Trial #2<br>score /10</th>
<th nowrap scope="col">Trial #2<br>total E2E (m:ss)</th>
<th nowrap scope="col">Trial #2<br>input tok/s</th>
<th nowrap scope="col">Trial #2<br>output tok/s</th>
<th nowrap scope="col">Trial #3<br>score /10</th>
<th nowrap scope="col">Trial #3<br>total E2E (m:ss)</th>
<th nowrap scope="col">Trial #3<br>input tok/s</th>
<th nowrap scope="col">Trial #3<br>output tok/s</th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap><a href="cases/qwen3-8-27b-oq4e-mtp.md">Qwen3.8 Jundot</a></td>
<td nowrap align="right">25/30</td>
<td nowrap align="right">141:31</td>
<td nowrap align="right"><a href="cases/qwen3-8-27b-oq4e-mtp.md#trial-1-failures">9/10</a></td>
<td nowrap align="right">39:22</td>
<td nowrap align="right">70.88</td>
<td nowrap align="right">18.51</td>
<td nowrap align="right"><a href="cases/qwen3-8-27b-oq4e-mtp.md#trial-2-failures">7/10</a></td>
<td nowrap align="right">53:52</td>
<td nowrap align="right">49.96</td>
<td nowrap align="right">13.76</td>
<td nowrap align="right"><a href="cases/qwen3-8-27b-oq4e-mtp.md#trial-3-failures">9/10</a></td>
<td nowrap align="right">48:17</td>
<td nowrap align="right">52.42</td>
<td nowrap align="right">14.74</td>
</tr>
<tr>
<td nowrap><a href="cases/qwen3-8-27b-mtplx-optimized-speed.md">Qwen3.8 Youssofal</a></td>
<td nowrap align="right">24/30</td>
<td nowrap align="right">170:30</td>
<td nowrap align="right"><a href="cases/qwen3-8-27b-mtplx-optimized-speed.md#trial-1-failures">9/10</a></td>
<td nowrap align="right">48:33</td>
<td nowrap align="right">66.28</td>
<td nowrap align="right">14.83</td>
<td nowrap align="right"><a href="cases/qwen3-8-27b-mtplx-optimized-speed.md#trial-2-failures">8/10</a></td>
<td nowrap align="right">60:06</td>
<td nowrap align="right">47.83</td>
<td nowrap align="right">10.81</td>
<td nowrap align="right"><a href="cases/qwen3-8-27b-mtplx-optimized-speed.md#trial-3-failures">7/10</a></td>
<td nowrap align="right">61:51</td>
<td nowrap align="right">52.42</td>
<td nowrap align="right">11.45</td>
</tr>
<tr>
<td nowrap><a href="cases/qwen3-8-27b-4bit.md">Qwen3.8 stock</a></td>
<td nowrap align="right">21/30</td>
<td nowrap align="right">169:28</td>
<td nowrap align="right"><a href="cases/qwen3-8-27b-4bit.md#trial-1-failures">8/10</a></td>
<td nowrap align="right">47:53</td>
<td nowrap align="right">66.63</td>
<td nowrap align="right">12.96</td>
<td nowrap align="right"><a href="cases/qwen3-8-27b-4bit.md#trial-2-failures">6/10</a></td>
<td nowrap align="right">65:20</td>
<td nowrap align="right">48.86</td>
<td nowrap align="right">9.50</td>
<td nowrap align="right"><a href="cases/qwen3-8-27b-4bit.md#trial-3-failures">7/10</a></td>
<td nowrap align="right">56:14</td>
<td nowrap align="right">54.55</td>
<td nowrap align="right">11.62</td>
</tr>
<tr>
<td nowrap><a href="cases/ornith-1-5-35b-a3b-vision-mtplx-4bit.md">Ornith Vision 4-bit</a></td>
<td nowrap align="right">20/30</td>
<td nowrap align="right">44:06</td>
<td nowrap align="right"><a href="cases/ornith-1-5-35b-a3b-vision-mtplx-4bit.md#trial-1-failures">6/10</a></td>
<td nowrap align="right">13:16</td>
<td nowrap align="right">417.80</td>
<td nowrap align="right">55.47</td>
<td nowrap align="right"><a href="cases/ornith-1-5-35b-a3b-vision-mtplx-4bit.md#trial-2-failures">8/10</a></td>
<td nowrap align="right">14:01</td>
<td nowrap align="right">444.46</td>
<td nowrap align="right">58.68</td>
<td nowrap align="right"><a href="cases/ornith-1-5-35b-a3b-vision-mtplx-4bit.md#trial-3-failures">6/10</a></td>
<td nowrap align="right">16:49</td>
<td nowrap align="right">360.22</td>
<td nowrap align="right">48.89</td>
</tr>
<tr>
<td nowrap><a href="cases/qwen3-6-35b-a3b-ud-mlx-4bit.md">Qwen3.6 UD</a></td>
<td nowrap align="right">19/30</td>
<td nowrap align="right">53:55</td>
<td nowrap align="right"><a href="cases/qwen3-6-35b-a3b-ud-mlx-4bit.md#trial-1-failures">5/10</a></td>
<td nowrap align="right">15:02</td>
<td nowrap align="right">443.42</td>
<td nowrap align="right">49.13</td>
<td nowrap align="right"><a href="cases/qwen3-6-35b-a3b-ud-mlx-4bit.md#trial-2-failures">8/10</a></td>
<td nowrap align="right">17:47</td>
<td nowrap align="right">464.27</td>
<td nowrap align="right">53.10</td>
<td nowrap align="right"><a href="cases/qwen3-6-35b-a3b-ud-mlx-4bit.md#trial-3-failures">6/10</a></td>
<td nowrap align="right">21:06</td>
<td nowrap align="right">362.32</td>
<td nowrap align="right">36.87</td>
</tr>
<tr>
<td nowrap><a href="cases/ornith-1-5-35b-a3b-oq6-gs128-mtp-vision.md">Ruka Ornith oQ6</a></td>
<td nowrap align="right">17/30</td>
<td nowrap align="right">34:15</td>
<td nowrap align="right"><a href="cases/ornith-1-5-35b-a3b-oq6-gs128-mtp-vision.md#trial-1-failures">4/10</a></td>
<td nowrap align="right">11:43</td>
<td nowrap align="right">544.51</td>
<td nowrap align="right">51.38</td>
<td nowrap align="right"><a href="cases/ornith-1-5-35b-a3b-oq6-gs128-mtp-vision.md#trial-2-failures">6/10</a></td>
<td nowrap align="right">10:10</td>
<td nowrap align="right">599.93</td>
<td nowrap align="right">52.53</td>
<td nowrap align="right"><a href="cases/ornith-1-5-35b-a3b-oq6-gs128-mtp-vision.md#trial-3-failures">7/10</a></td>
<td nowrap align="right">12:22</td>
<td nowrap align="right">509.35</td>
<td nowrap align="right">43.29</td>
</tr>
<tr>
<td nowrap><a href="cases/ornith-1-5-35b-a3b-mlx-6bit.md">Ornith 6-bit</a></td>
<td nowrap align="right">14/30</td>
<td nowrap align="right">50:25</td>
<td nowrap align="right"><a href="cases/ornith-1-5-35b-a3b-mlx-6bit.md#trial-1-failures">4/10</a></td>
<td nowrap align="right">16:28</td>
<td nowrap align="right">446.16</td>
<td nowrap align="right">36.67</td>
<td nowrap align="right"><a href="cases/ornith-1-5-35b-a3b-mlx-6bit.md#trial-2-failures">5/10</a></td>
<td nowrap align="right">15:21</td>
<td nowrap align="right">449.48</td>
<td nowrap align="right">38.32</td>
<td nowrap align="right"><a href="cases/ornith-1-5-35b-a3b-mlx-6bit.md#trial-3-failures">5/10</a></td>
<td nowrap align="right">18:36</td>
<td nowrap align="right">373.35</td>
<td nowrap align="right">31.42</td>
</tr>
<tr>
<td nowrap><a href="cases/qwen3-6-35b-a3b-nvfp4.md">Qwen3.6 nvfp4</a></td>
<td nowrap align="right">10/30</td>
<td nowrap align="right">68:31</td>
<td nowrap align="right"><a href="cases/qwen3-6-35b-a3b-nvfp4.md#trial-1-failures">3/10</a></td>
<td nowrap align="right">21:37</td>
<td nowrap align="right">421.73</td>
<td nowrap align="right">43.25</td>
<td nowrap align="right"><a href="cases/qwen3-6-35b-a3b-nvfp4.md#trial-2-failures">5/10</a></td>
<td nowrap align="right">21:16</td>
<td nowrap align="right">429.54</td>
<td nowrap align="right">42.69</td>
<td nowrap align="right"><a href="cases/qwen3-6-35b-a3b-nvfp4.md#trial-3-failures">2/10</a></td>
<td nowrap align="right">25:38</td>
<td nowrap align="right">373.62</td>
<td nowrap align="right">36.63</td>
</tr>
<tr>
<td nowrap><a href="cases/gemma-4-31b-it-mlx-4bit.md">Gemma 4</a></td>
<td nowrap align="right">9/30</td>
<td nowrap align="right">267:46</td>
<td nowrap align="right"><a href="cases/gemma-4-31b-it-mlx-4bit.md#trial-1-failures">3/10</a></td>
<td nowrap align="right">85:56</td>
<td nowrap align="right">55.27</td>
<td nowrap align="right">9.66</td>
<td nowrap align="right"><a href="cases/gemma-4-31b-it-mlx-4bit.md#trial-2-failures">4/10</a></td>
<td nowrap align="right">90:16</td>
<td nowrap align="right">41.68</td>
<td nowrap align="right">7.24</td>
<td nowrap align="right"><a href="cases/gemma-4-31b-it-mlx-4bit.md#trial-3-failures">2/10</a></td>
<td nowrap align="right">91:34</td>
<td nowrap align="right">44.28</td>
<td nowrap align="right">8.29</td>
</tr>
<tr>
<td nowrap><a href="cases/muse-glimmer-30b-4bit.md">Muse Glimmer</a></td>
<td nowrap align="right">6/30</td>
<td nowrap align="right">199:03</td>
<td nowrap align="right"><a href="cases/muse-glimmer-30b-4bit.md#trial-1-failures">2/10</a></td>
<td nowrap align="right">60:56</td>
<td nowrap align="right">66.95</td>
<td nowrap align="right">12.74</td>
<td nowrap align="right"><a href="cases/muse-glimmer-30b-4bit.md#trial-2-failures">2/10</a></td>
<td nowrap align="right">65:40</td>
<td nowrap align="right">51.86</td>
<td nowrap align="right">9.76</td>
<td nowrap align="right"><a href="cases/muse-glimmer-30b-4bit.md#trial-3-failures">2/10</a></td>
<td nowrap align="right">72:27</td>
<td nowrap align="right">54.75</td>
<td nowrap align="right">11.01</td>
</tr>
</tbody>
</table>

[Summary CSV](results/summary.csv) · [Methodology](docs/methodology.md)

## Question correctness and runtime

Each cell shows all 3 trials separately: **correctness /2 · E2E seconds**. **2/2** = all verification checks passed; **1/2** = at least one required content check passed; **0/2** = none. **⚠** = verified correct but completion failed, earning no /10 point. These are descriptive categories, not equal-weight partial-credit grades. Every entry links to the case explanation and full raw records.

<table>
<thead>
<tr>
<th nowrap scope="col">Model</th>
<th nowrap scope="col"><a href="docs/questions.md#q01">Q01</a></th>
<th nowrap scope="col"><a href="docs/questions.md#q02">Q02</a></th>
<th nowrap scope="col"><a href="docs/questions.md#q03">Q03</a></th>
<th nowrap scope="col"><a href="docs/questions.md#q04">Q04</a></th>
<th nowrap scope="col"><a href="docs/questions.md#q05">Q05</a></th>
<th nowrap scope="col"><a href="docs/questions.md#q06">Q06</a></th>
<th nowrap scope="col"><a href="docs/questions.md#q07">Q07</a></th>
<th nowrap scope="col"><a href="docs/questions.md#q08">Q08</a></th>
<th nowrap scope="col"><a href="docs/questions.md#q09">Q09</a></th>
<th nowrap scope="col"><a href="docs/questions.md#q10">Q10</a></th>
</tr>
</thead>
<tbody>
<tr>
<td nowrap><a href="cases/qwen3-8-27b-oq4e-mtp.md">Qwen3.8 Jundot</a></td>
<td nowrap>T1: <a href="cases/qwen3-8-27b-oq4e-mtp.md#q01-trial-1">2/2 · 94.95s</a><br>T2: <a href="cases/qwen3-8-27b-oq4e-mtp.md#q01-trial-2">2/2 · 155.32s</a><br>T3: <a href="cases/qwen3-8-27b-oq4e-mtp.md#q01-trial-3">2/2 · 161.34s</a></td>
<td nowrap>T1: <a href="cases/qwen3-8-27b-oq4e-mtp.md#q02-trial-1">2/2 · 196.07s</a><br>T2: <a href="cases/qwen3-8-27b-oq4e-mtp.md#q02-trial-2">2/2 · 159.58s</a><br>T3: <a href="cases/qwen3-8-27b-oq4e-mtp.md#q02-trial-3">2/2 · 142.25s</a></td>
<td nowrap>T1: <a href="cases/qwen3-8-27b-oq4e-mtp.md#q03-trial-1">2/2 · 98.20s</a><br>T2: <a href="cases/qwen3-8-27b-oq4e-mtp.md#q03-trial-2">2/2 · 127.10s</a><br>T3: <a href="cases/qwen3-8-27b-oq4e-mtp.md#q03-trial-3">1/2 · 208.22s</a></td>
<td nowrap>T1: <a href="cases/qwen3-8-27b-oq4e-mtp.md#q04-trial-1">2/2 · 263.33s</a><br>T2: <a href="cases/qwen3-8-27b-oq4e-mtp.md#q04-trial-2">2/2 · 349.53s</a><br>T3: <a href="cases/qwen3-8-27b-oq4e-mtp.md#q04-trial-3">2/2 · 355.59s</a></td>
<td nowrap>T1: <a href="cases/qwen3-8-27b-oq4e-mtp.md#q05-trial-1">2/2 · 180.31s</a><br>T2: <a href="cases/qwen3-8-27b-oq4e-mtp.md#q05-trial-2">2/2 · 164.62s</a><br>T3: <a href="cases/qwen3-8-27b-oq4e-mtp.md#q05-trial-3">2/2 · 170.66s</a></td>
<td nowrap>T1: <a href="cases/qwen3-8-27b-oq4e-mtp.md#q06-trial-1">2/2 · 141.82s</a><br>T2: <a href="cases/qwen3-8-27b-oq4e-mtp.md#q06-trial-2">2/2 · 294.58s</a><br>T3: <a href="cases/qwen3-8-27b-oq4e-mtp.md#q06-trial-3">2/2 · 264.63s</a></td>
<td nowrap>T1: <a href="cases/qwen3-8-27b-oq4e-mtp.md#q07-trial-1">1/2 · 214.95s</a><br>T2: <a href="cases/qwen3-8-27b-oq4e-mtp.md#q07-trial-2">1/2 · 309.85s</a><br>T3: <a href="cases/qwen3-8-27b-oq4e-mtp.md#q07-trial-3">2/2 · 393.28s</a></td>
<td nowrap>T1: <a href="cases/qwen3-8-27b-oq4e-mtp.md#q08-trial-1">2/2 · 599.99s</a><br>T2: <a href="cases/qwen3-8-27b-oq4e-mtp.md#q08-trial-2">2/2 ⚠ · 559.44s</a><br>T3: <a href="cases/qwen3-8-27b-oq4e-mtp.md#q08-trial-3">2/2 · 515.21s</a></td>
<td nowrap>T1: <a href="cases/qwen3-8-27b-oq4e-mtp.md#q09-trial-1">2/2 · 200.70s</a><br>T2: <a href="cases/qwen3-8-27b-oq4e-mtp.md#q09-trial-2">2/2 ⚠ · 600.33s</a><br>T3: <a href="cases/qwen3-8-27b-oq4e-mtp.md#q09-trial-3">2/2 · 340.47s</a></td>
<td nowrap>T1: <a href="cases/qwen3-8-27b-oq4e-mtp.md#q10-trial-1">2/2 · 372.15s</a><br>T2: <a href="cases/qwen3-8-27b-oq4e-mtp.md#q10-trial-2">2/2 · 511.16s</a><br>T3: <a href="cases/qwen3-8-27b-oq4e-mtp.md#q10-trial-3">2/2 · 345.47s</a></td>
</tr>
<tr>
<td nowrap><a href="cases/qwen3-8-27b-mtplx-optimized-speed.md">Qwen3.8 Youssofal</a></td>
<td nowrap>T1: <a href="cases/qwen3-8-27b-mtplx-optimized-speed.md#q01-trial-1">2/2 · 128.76s</a><br>T2: <a href="cases/qwen3-8-27b-mtplx-optimized-speed.md#q01-trial-2">2/2 · 123.57s</a><br>T3: <a href="cases/qwen3-8-27b-mtplx-optimized-speed.md#q01-trial-3">2/2 · 166.32s</a></td>
<td nowrap>T1: <a href="cases/qwen3-8-27b-mtplx-optimized-speed.md#q02-trial-1">2/2 · 259.60s</a><br>T2: <a href="cases/qwen3-8-27b-mtplx-optimized-speed.md#q02-trial-2">2/2 · 288.16s</a><br>T3: <a href="cases/qwen3-8-27b-mtplx-optimized-speed.md#q02-trial-3">2/2 · 141.84s</a></td>
<td nowrap>T1: <a href="cases/qwen3-8-27b-mtplx-optimized-speed.md#q03-trial-1">2/2 · 151.10s</a><br>T2: <a href="cases/qwen3-8-27b-mtplx-optimized-speed.md#q03-trial-2">2/2 · 181.69s</a><br>T3: <a href="cases/qwen3-8-27b-mtplx-optimized-speed.md#q03-trial-3">2/2 · 177.61s</a></td>
<td nowrap>T1: <a href="cases/qwen3-8-27b-mtplx-optimized-speed.md#q04-trial-1">2/2 · 313.01s</a><br>T2: <a href="cases/qwen3-8-27b-mtplx-optimized-speed.md#q04-trial-2">2/2 · 408.43s</a><br>T3: <a href="cases/qwen3-8-27b-mtplx-optimized-speed.md#q04-trial-3">0/2 · 600.50s</a></td>
<td nowrap>T1: <a href="cases/qwen3-8-27b-mtplx-optimized-speed.md#q05-trial-1">2/2 · 154.89s</a><br>T2: <a href="cases/qwen3-8-27b-mtplx-optimized-speed.md#q05-trial-2">2/2 · 171.31s</a><br>T3: <a href="cases/qwen3-8-27b-mtplx-optimized-speed.md#q05-trial-3">2/2 · 186.86s</a></td>
<td nowrap>T1: <a href="cases/qwen3-8-27b-mtplx-optimized-speed.md#q06-trial-1">2/2 · 172.06s</a><br>T2: <a href="cases/qwen3-8-27b-mtplx-optimized-speed.md#q06-trial-2">2/2 · 264.05s</a><br>T3: <a href="cases/qwen3-8-27b-mtplx-optimized-speed.md#q06-trial-3">2/2 · 402.98s</a></td>
<td nowrap>T1: <a href="cases/qwen3-8-27b-mtplx-optimized-speed.md#q07-trial-1">1/2 · 422.12s</a><br>T2: <a href="cases/qwen3-8-27b-mtplx-optimized-speed.md#q07-trial-2">2/2 · 398.51s</a><br>T3: <a href="cases/qwen3-8-27b-mtplx-optimized-speed.md#q07-trial-3">1/2 · 392.75s</a></td>
<td nowrap>T1: <a href="cases/qwen3-8-27b-mtplx-optimized-speed.md#q08-trial-1">2/2 · 452.28s</a><br>T2: <a href="cases/qwen3-8-27b-mtplx-optimized-speed.md#q08-trial-2">2/2 · 569.28s</a><br>T3: <a href="cases/qwen3-8-27b-mtplx-optimized-speed.md#q08-trial-3">2/2 · 581.16s</a></td>
<td nowrap>T1: <a href="cases/qwen3-8-27b-mtplx-optimized-speed.md#q09-trial-1">2/2 · 419.22s</a><br>T2: <a href="cases/qwen3-8-27b-mtplx-optimized-speed.md#q09-trial-2">2/2 ⚠ · 600.32s</a><br>T3: <a href="cases/qwen3-8-27b-mtplx-optimized-speed.md#q09-trial-3">1/2 · 564.07s</a></td>
<td nowrap>T1: <a href="cases/qwen3-8-27b-mtplx-optimized-speed.md#q10-trial-1">2/2 · 439.96s</a><br>T2: <a href="cases/qwen3-8-27b-mtplx-optimized-speed.md#q10-trial-2">1/2 · 600.46s</a><br>T3: <a href="cases/qwen3-8-27b-mtplx-optimized-speed.md#q10-trial-3">2/2 · 496.86s</a></td>
</tr>
<tr>
<td nowrap><a href="cases/qwen3-8-27b-4bit.md">Qwen3.8 stock</a></td>
<td nowrap>T1: <a href="cases/qwen3-8-27b-4bit.md#q01-trial-1">2/2 · 124.49s</a><br>T2: <a href="cases/qwen3-8-27b-4bit.md#q01-trial-2">2/2 · 128.62s</a><br>T3: <a href="cases/qwen3-8-27b-4bit.md#q01-trial-3">2/2 · 137.91s</a></td>
<td nowrap>T1: <a href="cases/qwen3-8-27b-4bit.md#q02-trial-1">2/2 · 148.82s</a><br>T2: <a href="cases/qwen3-8-27b-4bit.md#q02-trial-2">2/2 · 223.81s</a><br>T3: <a href="cases/qwen3-8-27b-4bit.md#q02-trial-3">2/2 · 176.35s</a></td>
<td nowrap>T1: <a href="cases/qwen3-8-27b-4bit.md#q03-trial-1">2/2 · 159.97s</a><br>T2: <a href="cases/qwen3-8-27b-4bit.md#q03-trial-2">2/2 · 248.42s</a><br>T3: <a href="cases/qwen3-8-27b-4bit.md#q03-trial-3">2/2 · 208.86s</a></td>
<td nowrap>T1: <a href="cases/qwen3-8-27b-4bit.md#q04-trial-1">2/2 · 360.29s</a><br>T2: <a href="cases/qwen3-8-27b-4bit.md#q04-trial-2">2/2 · 490.35s</a><br>T3: <a href="cases/qwen3-8-27b-4bit.md#q04-trial-3">2/2 · 437.27s</a></td>
<td nowrap>T1: <a href="cases/qwen3-8-27b-4bit.md#q05-trial-1">2/2 · 137.34s</a><br>T2: <a href="cases/qwen3-8-27b-4bit.md#q05-trial-2">2/2 · 238.79s</a><br>T3: <a href="cases/qwen3-8-27b-4bit.md#q05-trial-3">2/2 · 154.12s</a></td>
<td nowrap>T1: <a href="cases/qwen3-8-27b-4bit.md#q06-trial-1">2/2 · 238.85s</a><br>T2: <a href="cases/qwen3-8-27b-4bit.md#q06-trial-2">2/2 · 321.94s</a><br>T3: <a href="cases/qwen3-8-27b-4bit.md#q06-trial-3">2/2 · 196.73s</a></td>
<td nowrap>T1: <a href="cases/qwen3-8-27b-4bit.md#q07-trial-1">1/2 · 324.73s</a><br>T2: <a href="cases/qwen3-8-27b-4bit.md#q07-trial-2">1/2 · 465.86s</a><br>T3: <a href="cases/qwen3-8-27b-4bit.md#q07-trial-3">1/2 · 326.85s</a></td>
<td nowrap>T1: <a href="cases/qwen3-8-27b-4bit.md#q08-trial-1">2/2 · 368.43s</a><br>T2: <a href="cases/qwen3-8-27b-4bit.md#q08-trial-2">1/2 · 600.87s</a><br>T3: <a href="cases/qwen3-8-27b-4bit.md#q08-trial-3">0/2 · 600.57s</a></td>
<td nowrap>T1: <a href="cases/qwen3-8-27b-4bit.md#q09-trial-1">2/2 · 409.85s</a><br>T2: <a href="cases/qwen3-8-27b-4bit.md#q09-trial-2">1/2 · 600.87s</a><br>T3: <a href="cases/qwen3-8-27b-4bit.md#q09-trial-3">0/2 · 600.57s</a></td>
<td nowrap>T1: <a href="cases/qwen3-8-27b-4bit.md#q10-trial-1">2/2 ⚠ · 600.71s</a><br>T2: <a href="cases/qwen3-8-27b-4bit.md#q10-trial-2">0/2 · 600.95s</a><br>T3: <a href="cases/qwen3-8-27b-4bit.md#q10-trial-3">2/2 · 535.16s</a></td>
</tr>
<tr>
<td nowrap><a href="cases/ornith-1-5-35b-a3b-vision-mtplx-4bit.md">Ornith Vision 4-bit</a></td>
<td nowrap>T1: <a href="cases/ornith-1-5-35b-a3b-vision-mtplx-4bit.md#q01-trial-1">2/2 · 34.34s</a><br>T2: <a href="cases/ornith-1-5-35b-a3b-vision-mtplx-4bit.md#q01-trial-2">2/2 · 55.73s</a><br>T3: <a href="cases/ornith-1-5-35b-a3b-vision-mtplx-4bit.md#q01-trial-3">2/2 · 50.76s</a></td>
<td nowrap>T1: <a href="cases/ornith-1-5-35b-a3b-vision-mtplx-4bit.md#q02-trial-1">2/2 · 57.70s</a><br>T2: <a href="cases/ornith-1-5-35b-a3b-vision-mtplx-4bit.md#q02-trial-2">2/2 · 87.34s</a><br>T3: <a href="cases/ornith-1-5-35b-a3b-vision-mtplx-4bit.md#q02-trial-3">1/2 · 68.06s</a></td>
<td nowrap>T1: <a href="cases/ornith-1-5-35b-a3b-vision-mtplx-4bit.md#q03-trial-1">1/2 · 35.39s</a><br>T2: <a href="cases/ornith-1-5-35b-a3b-vision-mtplx-4bit.md#q03-trial-2">2/2 · 36.59s</a><br>T3: <a href="cases/ornith-1-5-35b-a3b-vision-mtplx-4bit.md#q03-trial-3">2/2 · 41.65s</a></td>
<td nowrap>T1: <a href="cases/ornith-1-5-35b-a3b-vision-mtplx-4bit.md#q04-trial-1">1/2 · 88.96s</a><br>T2: <a href="cases/ornith-1-5-35b-a3b-vision-mtplx-4bit.md#q04-trial-2">2/2 · 65.87s</a><br>T3: <a href="cases/ornith-1-5-35b-a3b-vision-mtplx-4bit.md#q04-trial-3">1/2 · 96.32s</a></td>
<td nowrap>T1: <a href="cases/ornith-1-5-35b-a3b-vision-mtplx-4bit.md#q05-trial-1">2/2 · 30.35s</a><br>T2: <a href="cases/ornith-1-5-35b-a3b-vision-mtplx-4bit.md#q05-trial-2">2/2 · 29.43s</a><br>T3: <a href="cases/ornith-1-5-35b-a3b-vision-mtplx-4bit.md#q05-trial-3">2/2 · 46.67s</a></td>
<td nowrap>T1: <a href="cases/ornith-1-5-35b-a3b-vision-mtplx-4bit.md#q06-trial-1">2/2 · 98.02s</a><br>T2: <a href="cases/ornith-1-5-35b-a3b-vision-mtplx-4bit.md#q06-trial-2">2/2 · 71.94s</a><br>T3: <a href="cases/ornith-1-5-35b-a3b-vision-mtplx-4bit.md#q06-trial-3">2/2 · 85.22s</a></td>
<td nowrap>T1: <a href="cases/ornith-1-5-35b-a3b-vision-mtplx-4bit.md#q07-trial-1">1/2 · 73.80s</a><br>T2: <a href="cases/ornith-1-5-35b-a3b-vision-mtplx-4bit.md#q07-trial-2">2/2 · 57.88s</a><br>T3: <a href="cases/ornith-1-5-35b-a3b-vision-mtplx-4bit.md#q07-trial-3">2/2 · 77.18s</a></td>
<td nowrap>T1: <a href="cases/ornith-1-5-35b-a3b-vision-mtplx-4bit.md#q08-trial-1">1/2 · 149.81s</a><br>T2: <a href="cases/ornith-1-5-35b-a3b-vision-mtplx-4bit.md#q08-trial-2">1/2 · 194.11s</a><br>T3: <a href="cases/ornith-1-5-35b-a3b-vision-mtplx-4bit.md#q08-trial-3">1/2 · 237.26s</a></td>
<td nowrap>T1: <a href="cases/ornith-1-5-35b-a3b-vision-mtplx-4bit.md#q09-trial-1">2/2 · 97.30s</a><br>T2: <a href="cases/ornith-1-5-35b-a3b-vision-mtplx-4bit.md#q09-trial-2">1/2 · 113.36s</a><br>T3: <a href="cases/ornith-1-5-35b-a3b-vision-mtplx-4bit.md#q09-trial-3">1/2 · 114.83s</a></td>
<td nowrap>T1: <a href="cases/ornith-1-5-35b-a3b-vision-mtplx-4bit.md#q10-trial-1">2/2 · 130.71s</a><br>T2: <a href="cases/ornith-1-5-35b-a3b-vision-mtplx-4bit.md#q10-trial-2">2/2 · 128.87s</a><br>T3: <a href="cases/ornith-1-5-35b-a3b-vision-mtplx-4bit.md#q10-trial-3">2/2 · 190.89s</a></td>
</tr>
<tr>
<td nowrap><a href="cases/qwen3-6-35b-a3b-ud-mlx-4bit.md">Qwen3.6 UD</a></td>
<td nowrap>T1: <a href="cases/qwen3-6-35b-a3b-ud-mlx-4bit.md#q01-trial-1">2/2 · 51.63s</a><br>T2: <a href="cases/qwen3-6-35b-a3b-ud-mlx-4bit.md#q01-trial-2">2/2 · 29.41s</a><br>T3: <a href="cases/qwen3-6-35b-a3b-ud-mlx-4bit.md#q01-trial-3">2/2 · 84.08s</a></td>
<td nowrap>T1: <a href="cases/qwen3-6-35b-a3b-ud-mlx-4bit.md#q02-trial-1">2/2 · 44.61s</a><br>T2: <a href="cases/qwen3-6-35b-a3b-ud-mlx-4bit.md#q02-trial-2">2/2 · 117.46s</a><br>T3: <a href="cases/qwen3-6-35b-a3b-ud-mlx-4bit.md#q02-trial-3">2/2 · 77.07s</a></td>
<td nowrap>T1: <a href="cases/qwen3-6-35b-a3b-ud-mlx-4bit.md#q03-trial-1">2/2 · 38.51s</a><br>T2: <a href="cases/qwen3-6-35b-a3b-ud-mlx-4bit.md#q03-trial-2">2/2 · 38.40s</a><br>T3: <a href="cases/qwen3-6-35b-a3b-ud-mlx-4bit.md#q03-trial-3">2/2 · 62.90s</a></td>
<td nowrap>T1: <a href="cases/qwen3-6-35b-a3b-ud-mlx-4bit.md#q04-trial-1">0/2 · 105.45s</a><br>T2: <a href="cases/qwen3-6-35b-a3b-ud-mlx-4bit.md#q04-trial-2">2/2 · 114.40s</a><br>T3: <a href="cases/qwen3-6-35b-a3b-ud-mlx-4bit.md#q04-trial-3">2/2 · 129.99s</a></td>
<td nowrap>T1: <a href="cases/qwen3-6-35b-a3b-ud-mlx-4bit.md#q05-trial-1">2/2 · 56.77s</a><br>T2: <a href="cases/qwen3-6-35b-a3b-ud-mlx-4bit.md#q05-trial-2">2/2 · 107.12s</a><br>T3: <a href="cases/qwen3-6-35b-a3b-ud-mlx-4bit.md#q05-trial-3">2/2 · 86.33s</a></td>
<td nowrap>T1: <a href="cases/qwen3-6-35b-a3b-ud-mlx-4bit.md#q06-trial-1">0/2 · 106.47s</a><br>T2: <a href="cases/qwen3-6-35b-a3b-ud-mlx-4bit.md#q06-trial-2">2/2 · 128.43s</a><br>T3: <a href="cases/qwen3-6-35b-a3b-ud-mlx-4bit.md#q06-trial-3">0/2 · 144.36s</a></td>
<td nowrap>T1: <a href="cases/qwen3-6-35b-a3b-ud-mlx-4bit.md#q07-trial-1">1/2 · 94.10s</a><br>T2: <a href="cases/qwen3-6-35b-a3b-ud-mlx-4bit.md#q07-trial-2">1/2 · 122.37s</a><br>T3: <a href="cases/qwen3-6-35b-a3b-ud-mlx-4bit.md#q07-trial-3">1/2 · 160.56s</a></td>
<td nowrap>T1: <a href="cases/qwen3-6-35b-a3b-ud-mlx-4bit.md#q08-trial-1">1/2 · 130.72s</a><br>T2: <a href="cases/qwen3-6-35b-a3b-ud-mlx-4bit.md#q08-trial-2">0/2 · 49.69s</a><br>T3: <a href="cases/qwen3-6-35b-a3b-ud-mlx-4bit.md#q08-trial-3">1/2 · 185.20s</a></td>
<td nowrap>T1: <a href="cases/qwen3-6-35b-a3b-ud-mlx-4bit.md#q09-trial-1">2/2 · 110.55s</a><br>T2: <a href="cases/qwen3-6-35b-a3b-ud-mlx-4bit.md#q09-trial-2">2/2 · 134.04s</a><br>T3: <a href="cases/qwen3-6-35b-a3b-ud-mlx-4bit.md#q09-trial-3">2/2 · 176.02s</a></td>
<td nowrap>T1: <a href="cases/qwen3-6-35b-a3b-ud-mlx-4bit.md#q10-trial-1">0/2 · 163.63s</a><br>T2: <a href="cases/qwen3-6-35b-a3b-ud-mlx-4bit.md#q10-trial-2">2/2 · 225.45s</a><br>T3: <a href="cases/qwen3-6-35b-a3b-ud-mlx-4bit.md#q10-trial-3">0/2 · 159.54s</a></td>
</tr>
<tr>
<td nowrap><a href="cases/ornith-1-5-35b-a3b-oq6-gs128-mtp-vision.md">Ruka Ornith oQ6</a></td>
<td nowrap>T1: <a href="cases/ornith-1-5-35b-a3b-oq6-gs128-mtp-vision.md#q01-trial-1">2/2 · 36.48s</a><br>T2: <a href="cases/ornith-1-5-35b-a3b-oq6-gs128-mtp-vision.md#q01-trial-2">2/2 · 43.52s</a><br>T3: <a href="cases/ornith-1-5-35b-a3b-oq6-gs128-mtp-vision.md#q01-trial-3">2/2 · 47.72s</a></td>
<td nowrap>T1: <a href="cases/ornith-1-5-35b-a3b-oq6-gs128-mtp-vision.md#q02-trial-1">0/2 · 54.67s</a><br>T2: <a href="cases/ornith-1-5-35b-a3b-oq6-gs128-mtp-vision.md#q02-trial-2">1/2 · 58.65s</a><br>T3: <a href="cases/ornith-1-5-35b-a3b-oq6-gs128-mtp-vision.md#q02-trial-3">2/2 · 46.80s</a></td>
<td nowrap>T1: <a href="cases/ornith-1-5-35b-a3b-oq6-gs128-mtp-vision.md#q03-trial-1">2/2 · 33.45s</a><br>T2: <a href="cases/ornith-1-5-35b-a3b-oq6-gs128-mtp-vision.md#q03-trial-2">1/2 · 33.39s</a><br>T3: <a href="cases/ornith-1-5-35b-a3b-oq6-gs128-mtp-vision.md#q03-trial-3">2/2 · 35.52s</a></td>
<td nowrap>T1: <a href="cases/ornith-1-5-35b-a3b-oq6-gs128-mtp-vision.md#q04-trial-1">1/2 · 101.51s</a><br>T2: <a href="cases/ornith-1-5-35b-a3b-oq6-gs128-mtp-vision.md#q04-trial-2">1/2 · 74.87s</a><br>T3: <a href="cases/ornith-1-5-35b-a3b-oq6-gs128-mtp-vision.md#q04-trial-3">1/2 · 80.28s</a></td>
<td nowrap>T1: <a href="cases/ornith-1-5-35b-a3b-oq6-gs128-mtp-vision.md#q05-trial-1">2/2 · 32.39s</a><br>T2: <a href="cases/ornith-1-5-35b-a3b-oq6-gs128-mtp-vision.md#q05-trial-2">2/2 · 32.37s</a><br>T3: <a href="cases/ornith-1-5-35b-a3b-oq6-gs128-mtp-vision.md#q05-trial-3">2/2 · 43.67s</a></td>
<td nowrap>T1: <a href="cases/ornith-1-5-35b-a3b-oq6-gs128-mtp-vision.md#q06-trial-1">2/2 · 75.95s</a><br>T2: <a href="cases/ornith-1-5-35b-a3b-oq6-gs128-mtp-vision.md#q06-trial-2">2/2 · 63.75s</a><br>T3: <a href="cases/ornith-1-5-35b-a3b-oq6-gs128-mtp-vision.md#q06-trial-3">2/2 · 49.94s</a></td>
<td nowrap>T1: <a href="cases/ornith-1-5-35b-a3b-oq6-gs128-mtp-vision.md#q07-trial-1">1/2 · 68.82s</a><br>T2: <a href="cases/ornith-1-5-35b-a3b-oq6-gs128-mtp-vision.md#q07-trial-2">2/2 · 54.59s</a><br>T3: <a href="cases/ornith-1-5-35b-a3b-oq6-gs128-mtp-vision.md#q07-trial-3">2/2 · 58.96s</a></td>
<td nowrap>T1: <a href="cases/ornith-1-5-35b-a3b-oq6-gs128-mtp-vision.md#q08-trial-1">2/2 ⚠ · 106.25s</a><br>T2: <a href="cases/ornith-1-5-35b-a3b-oq6-gs128-mtp-vision.md#q08-trial-2">0/2 · 80.95s</a><br>T3: <a href="cases/ornith-1-5-35b-a3b-oq6-gs128-mtp-vision.md#q08-trial-3">2/2 ⚠ · 179.81s</a></td>
<td nowrap>T1: <a href="cases/ornith-1-5-35b-a3b-oq6-gs128-mtp-vision.md#q09-trial-1">1/2 · 97.39s</a><br>T2: <a href="cases/ornith-1-5-35b-a3b-oq6-gs128-mtp-vision.md#q09-trial-2">2/2 · 83.34s</a><br>T3: <a href="cases/ornith-1-5-35b-a3b-oq6-gs128-mtp-vision.md#q09-trial-3">2/2 · 80.23s</a></td>
<td nowrap>T1: <a href="cases/ornith-1-5-35b-a3b-oq6-gs128-mtp-vision.md#q10-trial-1">0/2 · 96.14s</a><br>T2: <a href="cases/ornith-1-5-35b-a3b-oq6-gs128-mtp-vision.md#q10-trial-2">2/2 · 84.28s</a><br>T3: <a href="cases/ornith-1-5-35b-a3b-oq6-gs128-mtp-vision.md#q10-trial-3">0/2 · 119.21s</a></td>
</tr>
<tr>
<td nowrap><a href="cases/ornith-1-5-35b-a3b-mlx-6bit.md">Ornith 6-bit</a></td>
<td nowrap>T1: <a href="cases/ornith-1-5-35b-a3b-mlx-6bit.md#q01-trial-1">2/2 · 53.57s</a><br>T2: <a href="cases/ornith-1-5-35b-a3b-mlx-6bit.md#q01-trial-2">2/2 · 25.29s</a><br>T3: <a href="cases/ornith-1-5-35b-a3b-mlx-6bit.md#q01-trial-3">2/2 · 60.92s</a></td>
<td nowrap>T1: <a href="cases/ornith-1-5-35b-a3b-mlx-6bit.md#q02-trial-1">1/2 · 51.54s</a><br>T2: <a href="cases/ornith-1-5-35b-a3b-mlx-6bit.md#q02-trial-2">2/2 · 102.07s</a><br>T3: <a href="cases/ornith-1-5-35b-a3b-mlx-6bit.md#q02-trial-3">2/2 · 105.21s</a></td>
<td nowrap>T1: <a href="cases/ornith-1-5-35b-a3b-mlx-6bit.md#q03-trial-1">2/2 · 45.57s</a><br>T2: <a href="cases/ornith-1-5-35b-a3b-mlx-6bit.md#q03-trial-2">2/2 · 49.51s</a><br>T3: <a href="cases/ornith-1-5-35b-a3b-mlx-6bit.md#q03-trial-3">2/2 · 47.56s</a></td>
<td nowrap>T1: <a href="cases/ornith-1-5-35b-a3b-mlx-6bit.md#q04-trial-1">1/2 · 108.20s</a><br>T2: <a href="cases/ornith-1-5-35b-a3b-mlx-6bit.md#q04-trial-2">1/2 · 89.06s</a><br>T3: <a href="cases/ornith-1-5-35b-a3b-mlx-6bit.md#q04-trial-3">1/2 · 163.94s</a></td>
<td nowrap>T1: <a href="cases/ornith-1-5-35b-a3b-mlx-6bit.md#q05-trial-1">2/2 · 38.43s</a><br>T2: <a href="cases/ornith-1-5-35b-a3b-mlx-6bit.md#q05-trial-2">2/2 · 53.60s</a><br>T3: <a href="cases/ornith-1-5-35b-a3b-mlx-6bit.md#q05-trial-3">2/2 · 49.70s</a></td>
<td nowrap>T1: <a href="cases/ornith-1-5-35b-a3b-mlx-6bit.md#q06-trial-1">2/2 · 140.49s</a><br>T2: <a href="cases/ornith-1-5-35b-a3b-mlx-6bit.md#q06-trial-2">2/2 · 65.72s</a><br>T3: <a href="cases/ornith-1-5-35b-a3b-mlx-6bit.md#q06-trial-3">2/2 · 104.19s</a></td>
<td nowrap>T1: <a href="cases/ornith-1-5-35b-a3b-mlx-6bit.md#q07-trial-1">1/2 · 55.51s</a><br>T2: <a href="cases/ornith-1-5-35b-a3b-mlx-6bit.md#q07-trial-2">0/2 · 145.81s</a><br>T3: <a href="cases/ornith-1-5-35b-a3b-mlx-6bit.md#q07-trial-3">1/2 · 154.99s</a></td>
<td nowrap>T1: <a href="cases/ornith-1-5-35b-a3b-mlx-6bit.md#q08-trial-1">1/2 · 158.78s</a><br>T2: <a href="cases/ornith-1-5-35b-a3b-mlx-6bit.md#q08-trial-2">0/2 · 92.09s</a><br>T3: <a href="cases/ornith-1-5-35b-a3b-mlx-6bit.md#q08-trial-3">0/2 · 161.04s</a></td>
<td nowrap>T1: <a href="cases/ornith-1-5-35b-a3b-mlx-6bit.md#q09-trial-1">1/2 · 86.91s</a><br>T2: <a href="cases/ornith-1-5-35b-a3b-mlx-6bit.md#q09-trial-2">1/2 · 83.94s</a><br>T3: <a href="cases/ornith-1-5-35b-a3b-mlx-6bit.md#q09-trial-3">1/2 · 68.87s</a></td>
<td nowrap>T1: <a href="cases/ornith-1-5-35b-a3b-mlx-6bit.md#q10-trial-1">1/2 · 248.81s</a><br>T2: <a href="cases/ornith-1-5-35b-a3b-mlx-6bit.md#q10-trial-2">1/2 · 213.75s</a><br>T3: <a href="cases/ornith-1-5-35b-a3b-mlx-6bit.md#q10-trial-3">0/2 · 199.64s</a></td>
</tr>
<tr>
<td nowrap><a href="cases/qwen3-6-35b-a3b-nvfp4.md">Qwen3.6 nvfp4</a></td>
<td nowrap>T1: <a href="cases/qwen3-6-35b-a3b-nvfp4.md#q01-trial-1">1/2 · 81.10s</a><br>T2: <a href="cases/qwen3-6-35b-a3b-nvfp4.md#q01-trial-2">2/2 · 43.58s</a><br>T3: <a href="cases/qwen3-6-35b-a3b-nvfp4.md#q01-trial-3">2/2 · 84.11s</a></td>
<td nowrap>T1: <a href="cases/qwen3-6-35b-a3b-nvfp4.md#q02-trial-1">2/2 ⚠ · 150.03s</a><br>T2: <a href="cases/qwen3-6-35b-a3b-nvfp4.md#q02-trial-2">0/2 · 78.07s</a><br>T3: <a href="cases/qwen3-6-35b-a3b-nvfp4.md#q02-trial-3">1/2 · 149.00s</a></td>
<td nowrap>T1: <a href="cases/qwen3-6-35b-a3b-nvfp4.md#q03-trial-1">1/2 · 45.56s</a><br>T2: <a href="cases/qwen3-6-35b-a3b-nvfp4.md#q03-trial-2">2/2 · 85.04s</a><br>T3: <a href="cases/qwen3-6-35b-a3b-nvfp4.md#q03-trial-3">2/2 · 82.09s</a></td>
<td nowrap>T1: <a href="cases/qwen3-6-35b-a3b-nvfp4.md#q04-trial-1">0/2 · 119.49s</a><br>T2: <a href="cases/qwen3-6-35b-a3b-nvfp4.md#q04-trial-2">2/2 · 121.31s</a><br>T3: <a href="cases/qwen3-6-35b-a3b-nvfp4.md#q04-trial-3">1/2 · 150.98s</a></td>
<td nowrap>T1: <a href="cases/qwen3-6-35b-a3b-nvfp4.md#q05-trial-1">2/2 · 59.75s</a><br>T2: <a href="cases/qwen3-6-35b-a3b-nvfp4.md#q05-trial-2">2/2 · 86.92s</a><br>T3: <a href="cases/qwen3-6-35b-a3b-nvfp4.md#q05-trial-3">0/2 · 111.61s</a></td>
<td nowrap>T1: <a href="cases/qwen3-6-35b-a3b-nvfp4.md#q06-trial-1">1/2 · 142.67s</a><br>T2: <a href="cases/qwen3-6-35b-a3b-nvfp4.md#q06-trial-2">2/2 · 154.88s</a><br>T3: <a href="cases/qwen3-6-35b-a3b-nvfp4.md#q06-trial-3">0/2 · 207.85s</a></td>
<td nowrap>T1: <a href="cases/qwen3-6-35b-a3b-nvfp4.md#q07-trial-1">2/2 · 112.45s</a><br>T2: <a href="cases/qwen3-6-35b-a3b-nvfp4.md#q07-trial-2">1/2 · 115.36s</a><br>T3: <a href="cases/qwen3-6-35b-a3b-nvfp4.md#q07-trial-3">1/2 · 151.04s</a></td>
<td nowrap>T1: <a href="cases/qwen3-6-35b-a3b-nvfp4.md#q08-trial-1">0/2 · 153.16s</a><br>T2: <a href="cases/qwen3-6-35b-a3b-nvfp4.md#q08-trial-2">0/2 · 104.29s</a><br>T3: <a href="cases/qwen3-6-35b-a3b-nvfp4.md#q08-trial-3">0/2 · 197.62s</a></td>
<td nowrap>T1: <a href="cases/qwen3-6-35b-a3b-nvfp4.md#q09-trial-1">2/2 · 225.42s</a><br>T2: <a href="cases/qwen3-6-35b-a3b-nvfp4.md#q09-trial-2">2/2 ⚠ · 175.49s</a><br>T3: <a href="cases/qwen3-6-35b-a3b-nvfp4.md#q09-trial-3">1/2 · 140.22s</a></td>
<td nowrap>T1: <a href="cases/qwen3-6-35b-a3b-nvfp4.md#q10-trial-1">0/2 · 207.66s</a><br>T2: <a href="cases/qwen3-6-35b-a3b-nvfp4.md#q10-trial-2">2/2 ⚠ · 310.60s</a><br>T3: <a href="cases/qwen3-6-35b-a3b-nvfp4.md#q10-trial-3">1/2 · 263.68s</a></td>
</tr>
<tr>
<td nowrap><a href="cases/gemma-4-31b-it-mlx-4bit.md">Gemma 4</a></td>
<td nowrap>T1: <a href="cases/gemma-4-31b-it-mlx-4bit.md#q01-trial-1">1/2 · 539.50s</a><br>T2: <a href="cases/gemma-4-31b-it-mlx-4bit.md#q01-trial-2">2/2 · 417.54s</a><br>T3: <a href="cases/gemma-4-31b-it-mlx-4bit.md#q01-trial-3">0/2 · 600.56s</a></td>
<td nowrap>T1: <a href="cases/gemma-4-31b-it-mlx-4bit.md#q02-trial-1">2/2 · 431.04s</a><br>T2: <a href="cases/gemma-4-31b-it-mlx-4bit.md#q02-trial-2">2/2 · 559.56s</a><br>T3: <a href="cases/gemma-4-31b-it-mlx-4bit.md#q02-trial-3">2/2 · 537.53s</a></td>
<td nowrap>T1: <a href="cases/gemma-4-31b-it-mlx-4bit.md#q03-trial-1">2/2 · 378.06s</a><br>T2: <a href="cases/gemma-4-31b-it-mlx-4bit.md#q03-trial-2">2/2 · 506.63s</a><br>T3: <a href="cases/gemma-4-31b-it-mlx-4bit.md#q03-trial-3">2/2 · 465.86s</a></td>
<td nowrap>T1: <a href="cases/gemma-4-31b-it-mlx-4bit.md#q04-trial-1">0/2 · 600.89s</a><br>T2: <a href="cases/gemma-4-31b-it-mlx-4bit.md#q04-trial-2">0/2 · 601.01s</a><br>T3: <a href="cases/gemma-4-31b-it-mlx-4bit.md#q04-trial-3">0/2 · 600.24s</a></td>
<td nowrap>T1: <a href="cases/gemma-4-31b-it-mlx-4bit.md#q05-trial-1">2/2 · 301.70s</a><br>T2: <a href="cases/gemma-4-31b-it-mlx-4bit.md#q05-trial-2">2/2 · 417.05s</a><br>T3: <a href="cases/gemma-4-31b-it-mlx-4bit.md#q05-trial-3">1/2 · 287.39s</a></td>
<td nowrap>T1: <a href="cases/gemma-4-31b-it-mlx-4bit.md#q06-trial-1">2/2 ⚠ · 600.06s</a><br>T2: <a href="cases/gemma-4-31b-it-mlx-4bit.md#q06-trial-2">2/2 ⚠ · 601.03s</a><br>T3: <a href="cases/gemma-4-31b-it-mlx-4bit.md#q06-trial-3">2/2 ⚠ · 600.45s</a></td>
<td nowrap>T1: <a href="cases/gemma-4-31b-it-mlx-4bit.md#q07-trial-1">1/2 · 502.65s</a><br>T2: <a href="cases/gemma-4-31b-it-mlx-4bit.md#q07-trial-2">1/2 · 510.86s</a><br>T3: <a href="cases/gemma-4-31b-it-mlx-4bit.md#q07-trial-3">1/2 · 600.61s</a></td>
<td nowrap>T1: <a href="cases/gemma-4-31b-it-mlx-4bit.md#q08-trial-1">0/2 · 600.54s</a><br>T2: <a href="cases/gemma-4-31b-it-mlx-4bit.md#q08-trial-2">0/2 · 600.94s</a><br>T3: <a href="cases/gemma-4-31b-it-mlx-4bit.md#q08-trial-3">0/2 · 600.93s</a></td>
<td nowrap>T1: <a href="cases/gemma-4-31b-it-mlx-4bit.md#q09-trial-1">0/2 · 600.78s</a><br>T2: <a href="cases/gemma-4-31b-it-mlx-4bit.md#q09-trial-2">0/2 · 600.17s</a><br>T3: <a href="cases/gemma-4-31b-it-mlx-4bit.md#q09-trial-3">0/2 · 600.36s</a></td>
<td nowrap>T1: <a href="cases/gemma-4-31b-it-mlx-4bit.md#q10-trial-1">0/2 · 600.75s</a><br>T2: <a href="cases/gemma-4-31b-it-mlx-4bit.md#q10-trial-2">0/2 · 600.95s</a><br>T3: <a href="cases/gemma-4-31b-it-mlx-4bit.md#q10-trial-3">0/2 · 600.48s</a></td>
</tr>
<tr>
<td nowrap><a href="cases/muse-glimmer-30b-4bit.md">Muse Glimmer</a></td>
<td nowrap>T1: <a href="cases/muse-glimmer-30b-4bit.md#q01-trial-1">2/2 ⚠ · 350.51s</a><br>T2: <a href="cases/muse-glimmer-30b-4bit.md#q01-trial-2">2/2 ⚠ · 373.67s</a><br>T3: <a href="cases/muse-glimmer-30b-4bit.md#q01-trial-3">2/2 · 452.62s</a></td>
<td nowrap>T1: <a href="cases/muse-glimmer-30b-4bit.md#q02-trial-1">2/2 · 505.37s</a><br>T2: <a href="cases/muse-glimmer-30b-4bit.md#q02-trial-2">2/2 ⚠ · 439.09s</a><br>T3: <a href="cases/muse-glimmer-30b-4bit.md#q02-trial-3">2/2 ⚠ · 600.96s</a></td>
<td nowrap>T1: <a href="cases/muse-glimmer-30b-4bit.md#q03-trial-1">0/2 · 265.93s</a><br>T2: <a href="cases/muse-glimmer-30b-4bit.md#q03-trial-2">2/2 · 229.45s</a><br>T3: <a href="cases/muse-glimmer-30b-4bit.md#q03-trial-3">1/2 · 223.50s</a></td>
<td nowrap>T1: <a href="cases/muse-glimmer-30b-4bit.md#q04-trial-1">0/2 · 287.53s</a><br>T2: <a href="cases/muse-glimmer-30b-4bit.md#q04-trial-2">0/2 · 360.67s</a><br>T3: <a href="cases/muse-glimmer-30b-4bit.md#q04-trial-3">0/2 · 326.99s</a></td>
<td nowrap>T1: <a href="cases/muse-glimmer-30b-4bit.md#q05-trial-1">2/2 · 316.06s</a><br>T2: <a href="cases/muse-glimmer-30b-4bit.md#q05-trial-2">2/2 · 512.17s</a><br>T3: <a href="cases/muse-glimmer-30b-4bit.md#q05-trial-3">2/2 · 382.27s</a></td>
<td nowrap>T1: <a href="cases/muse-glimmer-30b-4bit.md#q06-trial-1">2/2 ⚠ · 600.98s</a><br>T2: <a href="cases/muse-glimmer-30b-4bit.md#q06-trial-2">0/2 · 421.59s</a><br>T3: <a href="cases/muse-glimmer-30b-4bit.md#q06-trial-3">0/2 · 380.75s</a></td>
<td nowrap>T1: <a href="cases/muse-glimmer-30b-4bit.md#q07-trial-1">0/2 · 245.13s</a><br>T2: <a href="cases/muse-glimmer-30b-4bit.md#q07-trial-2">1/2 · 551.61s</a><br>T3: <a href="cases/muse-glimmer-30b-4bit.md#q07-trial-3">1/2 · 451.12s</a></td>
<td nowrap>T1: <a href="cases/muse-glimmer-30b-4bit.md#q08-trial-1">0/2 · 333.19s</a><br>T2: <a href="cases/muse-glimmer-30b-4bit.md#q08-trial-2">0/2 · 425.46s</a><br>T3: <a href="cases/muse-glimmer-30b-4bit.md#q08-trial-3">0/2 · 560.55s</a></td>
<td nowrap>T1: <a href="cases/muse-glimmer-30b-4bit.md#q09-trial-1">0/2 · 418.71s</a><br>T2: <a href="cases/muse-glimmer-30b-4bit.md#q09-trial-2">0/2 · 363.28s</a><br>T3: <a href="cases/muse-glimmer-30b-4bit.md#q09-trial-3">0/2 · 600.97s</a></td>
<td nowrap>T1: <a href="cases/muse-glimmer-30b-4bit.md#q10-trial-1">0/2 · 332.58s</a><br>T2: <a href="cases/muse-glimmer-30b-4bit.md#q10-trial-2">0/2 · 263.34s</a><br>T3: <a href="cases/muse-glimmer-30b-4bit.md#q10-trial-3">0/2 · 367.35s</a></td>
</tr>
</tbody>
</table>

[All 300 per-question results CSV](results/per-question.csv) · [Exact questions and CLI guides](docs/questions.md)

## Interpretation

- Between Trials #1 and #2, full-pass outcomes matched on **72/100** pairs; those results are **not fully reproducible** at the per-question completion level.
- Thirty expected references changed (file inventory, duplicates, Drive storage). Among 70 pairs with unchanged expected answers, **24 full-pass outcomes flipped**. Matching expected answers does not prove identical source/context inputs.
- In Trials #1 and #2, all three Qwen3.8 variants repeated **6/6 full passes** on the original six questions. Jundot verified **9/10** in both, but two correct Trial #2 artifacts hit completion limits, reducing its full score from **9 to 7**.
- Several mathematically optimal backup plans failed the candidate inventory/metadata requirements. See case explanations before interpreting these as optimization failures.
- These are small repeated samples. Existing model-specific MTP/engine/cache settings and shared laptop workload limit generalization.

## Data and documentation

- [Trial #3 collection, audit, and comparison](docs/trial-3.md)
- [Data layout, raw-data commands, and the size limit](docs/data.md)
- [Methodology, scoring, timing, safety controls, and corrections](docs/methodology.md)
- [Earlier benchmark suites and downloads](docs/history.md)
- [Exact prompts, CLI guides, and both calendar windows](docs/questions.md)
- [Environment](metadata/environment.json), [completion audit](metadata/completion-audit.json), [reproducibility summary](metadata/reproducibility-summary.json)
- [Credential review and artifact hashes](metadata/publication.json)

The owner authorized public release of filenames and logs. Scored records retain local filenames and account/home-related answer metadata. Credentials and credential stores are excluded. Full duplicated tool/provider transcripts, scratch directories, runtime caches, source media, and model weights are omitted to keep this new repository below **3,000,000 bytes including local Git history**. Original scored result records remain available as lossless gzip downloads.

## Regenerate or validate offline

```sh
python3 scripts/report.py --render
python3 scripts/report.py --validate
```

These use Python’s standard library, saved files only, no inference/network calls, and no model-authored program execution. The archived benchmark harness is machine-specific experimental code. No license is assigned to personal data, third-party models, or model outputs by this repository.
