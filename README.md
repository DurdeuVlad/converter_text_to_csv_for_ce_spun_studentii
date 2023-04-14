
<h1>Project Title: Converter Text to CSV for "Ce spun studentii?" show</h1>
<h2>Introduction</h2><p>This is a python solution implemented in Visual Studio Code to convert a text file containing questions and up to 8 answers with points, into a CSV file. The solution takes an <code>input.txt</code> file as input and generates an <code>output.csv</code> file with the questions, answers, and their points.</p><h2>Requirements:</h2><ul><li>Python 3.6 or higher</li><li>Visual Studio Code (or any other code editor)</li></ul><h2>Problem Statement</h2><p>The problem is to convert a text file with questions and answers into a CSV file. The text file contains questions and up to 8 answers with points. Each question is followed by up to 8 answers, each of which has a point value associated with it. The input file is in the following format:</p><pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs">1.Cum le spui parintiilor ca esti insarcinata?
—fdsfsft 39
—fsdfdsfsdfgfd 28
—wefdvxe 15
—sefeacveb 11
—fdsfghtesd 7

2.Ce scuza ii bagi la proful ca nu ai fost la ore?
—sdgsnwffsdfsd 34
—bsgeacasdfsdf 22
—sgsgewrafsdfsdf 34
—fdaefadfsfwefsdfs 55
—sdgbgdacewvfges 10
</code></div></div></pre><p>The output file should be a CSV file in the following format:</p><pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs">question,answer,points,answer,points,answer,points,answer,points,answer,points,answer,points,answer,points,answer,points
1.Cum le spui parintiilor ca esti insarcinata?,fdsfsft,39,fsdfdsfsdfgfd,28,wefdvxe,15,sefeacveb,11,fdsfghtesd,7
2.Ce scuza ii bagi la proful ca nu ai fost la ore?,sdgsnwffsdfsd,34,bsgeacasdfsdf,22,sgsgewrafsdfsdf,34,fdaefadfsfwefsdfs,55,sdgbgdacewvfges,10
</code></div></div></pre><h2>How to Run</h2><ol><li>Clone the repository to your local machine using the following command:</li></ol><pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">git <span class="hljs-built_in">clone</span> https://github.com/&lt;your-username&gt;/&lt;repository-name&gt;.git
</code></div></div></pre><ol start="2"><li>Navigate to the project directory using the following command:</li></ol><pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash"><span class="hljs-built_in">cd</span> &lt;repository-name&gt;
</code></div></div></pre><ol start="3"><li><p>Place your input text file in the project directory and update the <code>input_filename</code> variable in the <code>txttocsv.py</code> file with the name of your input text file.</p></li><li><p>Run the python script using the following command:</p></li></ol><pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs">python txttocsv.py
</code></div></div></pre><ol start="5"><li>The output CSV file will be generated in the project directory with the name <code>output.csv</code>.</li></ol><h2>Dependencies</h2><p>This solution requires Python version 3 or higher and the <code>csv</code> module, which is included in the standard Python library.</p><h2>Conclusion</h2><p>This solution provides an easy and efficient way to convert a text file with questions and answers into a CSV file. The implementation is done in Python in Visual Studio Code, making it easy to modify and extend as needed.</p>