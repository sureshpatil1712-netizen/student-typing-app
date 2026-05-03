<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bombay High Court Typing Test</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        /* Custom scrollbar for reference text */
        .custom-scrollbar::-webkit-scrollbar { width: 8px; }
        .custom-scrollbar::-webkit-scrollbar-track { background: #f1f1f1; }
        .custom-scrollbar::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 4px; }
        .custom-scrollbar::-webkit-scrollbar-thumb:hover { background: #94a3b8; }
    </style>
</head>
<body class="bg-slate-50 font-sans text-slate-800 min-h-screen p-4 md:p-8">

    <div class="max-w-6xl mx-auto space-y-6">
        <!-- Header & Controls -->
        <div class="bg-white p-6 rounded-xl shadow-sm border border-slate-200">
            <div class="flex flex-col lg:flex-row justify-between items-start lg:items-center gap-6">
                <div>
                    <h1 class="text-2xl font-bold text-slate-800 flex items-center gap-2">
                        <i class="fa-solid fa-scale-balanced text-blue-600"></i>
                        Bombay High Court Typing Test
                    </h1>
                    <p class="text-slate-500 text-sm mt-1">Target: 40 WPM • Duration: 10 Minutes</p>
                </div>

                <div class="flex flex-wrap items-center gap-4 w-full lg:w-auto">
                    <!-- Paper vs Screen Toggle -->
                    <div class="flex bg-slate-100 p-1 rounded-lg border border-slate-200">
                        <button id="btn-screen-mode" onclick="setMode(false)" class="flex items-center gap-2 px-4 py-2 rounded-md text-sm font-medium transition-all bg-white shadow text-blue-600">
                            <i class="fa-solid fa-desktop"></i> Screen Mode
                        </button>
                        <button id="btn-paper-mode" onclick="setMode(true)" class="flex items-center gap-2 px-4 py-2 rounded-md text-sm font-medium transition-all text-slate-500 hover:text-slate-700">
                            <i class="fa-regular fa-file-lines"></i> Paper Mode
                        </button>
                    </div>

                    <!-- Print Button -->
                    <button onclick="printPassagesToPDF()" class="flex items-center gap-2 px-4 py-2.5 bg-slate-800 hover:bg-slate-900 text-white rounded-lg transition-colors text-sm font-medium">
                        <i class="fa-solid fa-print"></i> Print Passages
                    </button>
                </div>
            </div>

            <hr class="my-5 border-slate-100" />

            <div class="flex flex-col md:flex-row items-center gap-4">
                <div class="flex-grow w-full md:w-auto">
                    <label class="block text-xs font-semibold text-slate-500 uppercase mb-1">Select Passage Number</label>
                    <select id="passage-select" onchange="handlePassageChange()" class="bg-slate-50 border border-slate-300 text-slate-700 font-medium rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5">
                        <!-- Options injected by JS -->
                    </select>
                </div>
                <div class="pt-5 hidden md:block">
                    <!-- Restart Button -->
                    <button onclick="resetTest()" class="flex items-center gap-2 px-6 py-2.5 bg-red-50 hover:bg-red-100 text-red-600 border border-red-200 rounded-lg transition-colors font-medium whitespace-nowrap">
                        <i class="fa-solid fa-arrow-rotate-right"></i> Restart
                    </button>
                </div>
            </div>
        </div>

        <!-- Live Status Bar -->
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
            <div class="bg-white p-4 rounded-xl shadow-sm border border-slate-200 flex flex-col items-center justify-center">
                <span class="text-slate-500 text-xs font-semibold uppercase tracking-wider mb-1">Time Left</span>
                <div id="time-display" class="text-3xl font-mono font-bold flex items-center gap-2 text-slate-700">
                    <i class="fa-regular fa-clock"></i> 10:00
                </div>
            </div>
            <div class="bg-white p-4 rounded-xl shadow-sm border border-slate-200 flex flex-col items-center justify-center">
                <span class="text-slate-500 text-xs font-semibold uppercase tracking-wider mb-1">Live Gross WPM</span>
                <div id="wpm-display" class="text-3xl font-bold text-blue-600">0</div>
            </div>
            <div class="bg-white p-4 rounded-xl shadow-sm border border-slate-200 flex flex-col items-center justify-center">
                <span class="text-slate-500 text-xs font-semibold uppercase tracking-wider mb-1">Total Keystrokes</span>
                <div id="keystrokes-display" class="text-3xl font-bold text-slate-700">0</div>
            </div>
            <div class="bg-white p-4 rounded-xl shadow-sm border border-slate-200 flex flex-col items-center justify-center">
                <span class="text-slate-500 text-xs font-semibold uppercase tracking-wider mb-1">Backspaces Used</span>
                <div id="backspaces-display" class="text-3xl font-bold text-amber-500">0</div>
            </div>
        </div>

        <!-- Typing Area -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6" id="typing-container">
            
            <!-- Reference Text (Left) -->
            <div id="reference-panel" class="bg-white rounded-xl shadow-sm border border-slate-200 flex flex-col h-[500px]">
                <div class="px-4 py-3 border-b border-slate-100 flex items-center justify-between bg-slate-50 rounded-t-xl">
                    <div class="flex items-center gap-2">
                        <i class="fa-regular fa-file-text text-slate-500"></i>
                        <h2 class="font-semibold text-slate-700">On-Screen Reference</h2>
                    </div>
                    <span id="ref-id-display" class="text-xs text-slate-400 font-mono">ID: 1</span>
                </div>
                <div id="reference-text" class="p-6 overflow-y-auto custom-scrollbar text-[17px] leading-relaxed font-mono select-none flex-grow">
                    <!-- Text injected by JS -->
                </div>
            </div>

            <!-- User Input (Right) -->
            <div id="input-panel" class="bg-white rounded-xl shadow-sm border border-slate-200 flex flex-col h-[500px]">
                <div class="px-4 py-3 border-b border-slate-100 bg-slate-50 rounded-t-xl flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2">
                    <div class="flex items-center gap-2">
                        <h2 class="font-semibold text-slate-700">Type Here</h2>
                        <span id="paper-mode-badge" class="hidden text-xs bg-amber-100 text-amber-800 px-2 py-1 rounded font-medium flex items-center gap-1">
                            <i class="fa-solid fa-file-arrow-down"></i> Analyzing Passage No. <span id="badge-id">1</span>
                        </span>
                    </div>
                    <span id="start-prompt" class="text-xs bg-blue-100 text-blue-700 px-2 py-1 rounded font-medium animate-pulse">
                        Start typing to begin timer
                    </span>
                </div>
                
                <div id="paper-mode-instruction" class="hidden bg-blue-50 p-4 border-b border-blue-100 text-blue-800 text-center text-sm font-medium">
                    Look at your printed sheet for <strong id="instruction-id">Passage No. 1</strong>. Type directly below.
                </div>

                <textarea id="typing-input" class="flex-grow p-6 text-lg leading-relaxed font-mono resize-none focus:outline-none focus:ring-inset focus:ring-2 focus:ring-blue-100 rounded-b-xl disabled:bg-slate-50 disabled:text-slate-500" placeholder="Start typing here..." spellcheck="false" autocomplete="off" autocorrect="off" autocapitalize="off"></textarea>
            </div>
        </div>

        <!-- Results Modal -->
        <div id="results-modal" class="hidden fixed inset-0 bg-slate-900/60 backdrop-blur-sm flex items-center justify-center p-4 z-50">
            <div class="bg-white rounded-2xl shadow-2xl w-full max-w-3xl overflow-hidden transform transition-all flex flex-col max-h-[90vh]">
                <div class="bg-slate-800 p-6 text-center text-white border-b-4 border-blue-500 flex-shrink-0">
                    <h2 class="text-3xl font-bold mb-2">Performance Report</h2>
                    <p class="text-slate-300" id="report-subtitle">Passage 1 • Screen Mode</p>
                </div>
                
                <div class="p-8 overflow-y-auto custom-scrollbar flex-grow">
                    <div class="grid grid-cols-2 gap-6 mb-8">
                        <div id="net-speed-card" class="p-6 rounded-xl border text-center">
                            <p class="text-slate-500 text-sm font-semibold uppercase tracking-wider mb-2">Final Net Speed</p>
                            <div class="text-6xl font-black mb-1" id="final-net-wpm">
                                0 <span class="text-2xl font-bold text-slate-400">WPM</span>
                            </div>
                            <p id="qualification-status" class="text-sm font-medium"></p>
                        </div>
                        
                        <div class="bg-slate-50 p-6 rounded-xl border border-slate-200 text-center">
                            <p class="text-slate-500 text-sm font-semibold uppercase tracking-wider mb-2">Gross Speed</p>
                            <div class="text-6xl font-black text-slate-700 mb-1" id="final-gross-wpm">
                                0 <span class="text-2xl font-bold text-slate-400">WPM</span>
                            </div>
                            <p class="text-sm font-medium text-slate-500">Total speed including errors</p>
                        </div>
                    </div>

                    <div class="bg-white rounded-xl border border-slate-200 overflow-hidden shadow-sm mb-8">
                        <table class="w-full text-left text-sm">
                            <tbody class="divide-y divide-slate-100">
                                <tr>
                                    <th class="px-6 py-4 font-semibold text-slate-600 bg-slate-50 w-1/2">Total Keystrokes Logged</th>
                                    <td class="px-6 py-4 text-right font-mono text-lg font-bold text-slate-800" id="modal-keystrokes">0</td>
                                </tr>
                                <tr>
                                    <th class="px-6 py-4 font-semibold text-slate-600 w-1/2">Backspaces Used</th>
                                    <td class="px-6 py-4 text-right font-mono text-lg font-bold text-amber-600" id="modal-backspaces">0</td>
                                </tr>
                                <tr>
                                    <th class="px-6 py-4 font-semibold text-slate-600 bg-slate-50 w-1/2">Word Errors / Skips</th>
                                    <td class="px-6 py-4 text-right font-mono text-lg font-bold text-red-500" id="modal-errors">0</td>
                                </tr>
                                <tr>
                                    <th class="px-6 py-4 font-semibold text-slate-600 w-1/2">Accuracy Score</th>
                                    <td class="px-6 py-4 text-right font-mono text-lg font-bold text-slate-800" id="modal-accuracy">0%</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    <div class="mt-8 flex justify-center">
                        <button onclick="resetTest(); document.getElementById('results-modal').classList.add('hidden');" class="bg-slate-800 hover:bg-slate-900 text-white px-8 py-3 rounded-lg font-bold shadow-md transition-all active:scale-95 flex items-center gap-2">
                            <i class="fa-solid fa-arrow-rotate-right"></i> Start Next Test
                        </button>
                    </div>
                </div>
            </div>
        </div>

    </div>

    <script>
        // --- DATA SETUP ---
        const baseTemplates = [
            { type: "Civil Suit - Specific Performance", text: "In the High Court of Judicature, Ordinary Original Civil Jurisdiction. The plaintiff has filed this suit for specific performance of the agreement to sell dated 12th October 2018. It is the case of the plaintiff that the defendant, being the absolute owner of the suit schedule property, had agreed to sell the same for a total consideration of Rs. 50,00,000/- (Rupees Fifty Lakhs only). An earnest money deposit of Rs. 10,00,000/- was paid by the plaintiff vide Cheque drawn on State Bank of India. The defendant acknowledged the receipt of the said amount and executed an agreement. However, despite repeated notices and reminders, the defendant failed to execute the final sale deed within the stipulated period of six months. The learned counsel for the petitioner submitted that the impugned judgment is contrary to the well-settled principles of law. The documentary evidence clearly establishes the readiness and willingness of the plaintiff to perform his part of the contract. Section 16(c) of the Specific Relief Act, 1963, mandates that the plaintiff must aver and prove his continuous readiness from the date of the contract till the execution. The trial court erred in ignoring the bank statements marked as Exhibit P-4, which clearly demonstrated that the plaintiff had sufficient funds to pay the balance consideration. On the other hand, the learned counsel for the respondent vehemently opposed the petition, stating that the agreement was forged and fabricated. It was argued that the signature on the agreement does not match the admitted signature of the defendant. Furthermore, the respondent contended that time was the essence of the contract, and the plaintiff having failed to tender the balance amount within the agreed timeframe, the earnest money stood forfeited. The Supreme Court in various pronouncements has held that in cases of sale of immovable property, time is not generally presumed to be the essence of the contract unless there are specific stipulations to that effect. The burden of proof lies heavily on the party asserting that time was of the essence. Upon careful consideration of the rival submissions and perusal of the trial court records, this Court is of the considered opinion that the matter requires a deeper examination of the evidence adduced. The discrepancies in the forensic expert's report regarding the disputed signatures cannot be brushed aside. Therefore, the matter is remanded back to the trial court for fresh adjudication after affording an opportunity to both parties to lead additional evidence. The appeal is partly allowed in the aforesaid terms. No order as to costs." },
            { type: "Criminal Appeal - Bail Application", text: "This criminal appeal arises out of the judgment and order of conviction passed by the learned Sessions Court, whereby the appellant has been convicted under Section 302 read with Section 34 of the Indian Penal Code, 1860, and sentenced to suffer rigorous imprisonment for life. The prosecution case, in brief, is that on the fateful night of 15th August 2021, the accused persons formed an unlawful assembly and assaulted the deceased with deadly weapons over a prior property dispute. The first information report was lodged by the brother of the deceased, who is also an eyewitness to the incident. During the course of the trial, the prosecution examined twelve witnesses to bring home the guilt of the accused. The learned Senior Counsel appearing on behalf of the appellant has primarily urged two grounds to challenge the conviction. Firstly, it is submitted that there is an unexplained and inordinate delay of fourteen hours in lodging the FIR, which casts a serious doubt on the veracity of the prosecution version. It is a settled position of criminal jurisprudence that an unexplained delay in lodging the FIR often provides room for afterthought and embellishment. Secondly, the learned counsel argued that the testimonies of the eye-witnesses are fraught with material contradictions and omissions, making them entirely unreliable. He specifically pointed out the cross-examination of Prosecution Witness 3, whose statement recorded under Section 161 of the Code of Criminal Procedure, 1973, significantly differs from his deposition in the court. The learned Additional Public Prosecutor, on the contrary, supported the impugned judgment, asserting that minor discrepancies are bound to occur when witnesses are examined after a considerable lapse of time. He emphasized that the medical evidence corroborates the ocular testimony, as the post-mortem report clearly indicates multiple incised wounds caused by a sharp-edged weapon. Having heard both the learned counsels and having scrutinized the lower court records, we find merit in the submissions made by the appellant. The prosecution has failed to establish the chain of circumstances beyond a reasonable doubt. The fundamental principle of criminal law dictates that the accused is presumed innocent until proven guilty, and the benefit of the doubt must always go to the accused. Consequently, the impugned judgment and order of conviction are hereby set aside. The appellant is acquitted of all charges and is directed to be released forthwith, provided he is not required in any other ongoing criminal case." },
            { type: "Writ Petition - Service Matter", text: "The present writ petition has been filed under Article 226 of the Constitution of India challenging the impugned order of dismissal from service passed by the disciplinary authority. The petitioner was employed as a Junior Clerk in the Revenue Department. It is the case of the petitioner that he was falsely implicated in a departmental enquiry without being given a fair and reasonable opportunity of being heard, thereby violating the principles of natural justice. The charge against the petitioner was unauthorized absence from duty for a continuous period of ninety days without prior sanction of leave. The learned counsel for the petitioner submitted that the absence was entirely due to severe medical exigencies, as the petitioner was suffering from acute tuberculosis and was advised complete bed rest. Medical certificates issued by the Civil Hospital were duly produced before the enquiry officer, but the same were arbitrarily rejected without assigning any cogent reasons. It was further contended that the punishment of dismissal is shockingly disproportionate to the gravity of the alleged misconduct. Relying on various judgments of the Apex Court, the counsel argued that the doctrine of proportionality must be strictly applied in disciplinary proceedings. Per contra, the learned Government Pleader representing the State vehemently defended the impugned order. It was submitted that the petitioner is a habitual absentee and has been issued multiple warning memos in the past. The medical certificates were produced belatedly only as an afterthought to circumvent the disciplinary action. The enquiry was conducted strictly in accordance with the Maharashtra Civil Services (Discipline and Appeal) Rules, 1979. The petitioner was allowed to cross-examine the management witnesses and adduce his own defense evidence. The disciplinary authority, after applying its mind to the findings of the enquiry officer, rightly concluded that the petitioner's retention in government service would be detrimental to public administration. We have carefully perused the pleadings and the original record of the departmental proceedings. While it is true that courts exercise limited jurisdiction under Article 226 in matters of departmental enquiries and cannot act as an appellate authority to re-appreciate evidence, the court can certainly interfere if the findings are perverse or based on no evidence. In the present case, the outright rejection of government hospital medical certificates without seeking an opinion from a medical board demonstrates non-application of mind. In the interest of justice, the impugned order of dismissal is quashed and set aside. The respondents are directed to reinstate the petitioner with continuity of service, however, without 50 percent back wages." },
            { type: "Arbitration Application - Commercial Dispute", text: "This is an application filed under Section 11 of the Arbitration and Conciliation Act, 1996, seeking the appointment of a sole arbitrator to adjudicate the disputes and differences that have arisen between the parties. The applicant is a private limited company engaged in the business of infrastructure development. The respondent is a municipal corporation. The parties had entered into a comprehensive contract dated 4th March 2017 for the construction of a flyover bridge. Clause 24 of the general conditions of contract contains a distinct arbitration agreement, which stipulates that any dispute arising out of or in connection with the contract shall be referred to arbitration. According to the applicant, they successfully completed the major portion of the project within the stipulated timeframe. However, the respondent abruptly terminated the contract citing alleged delays and poor quality of work. Furthermore, the respondent arbitrarily invoked the bank guarantees submitted by the applicant without any prior intimation. The applicant issued a statutory notice invoking the arbitration clause and suggested the names of three retired High Court judges to act as the sole arbitrator. The respondent, despite receiving the said notice, failed to concur on any name within the statutory period of thirty days. The learned counsel for the respondent corporation raised a preliminary objection regarding the maintainability of the present application. It was argued that the applicant had not exhausted the pre-arbitration conciliation mechanism mandated under Clause 23 of the contract, which requires the parties to first attempt an amicable settlement before the Superintending Engineer. Thus, the invocation of arbitration is premature. In rejoinder, the applicant submitted that the respondent's hostile act of encashing the bank guarantees rendered any conciliation process practically impossible and futile. The Supreme Court has repeatedly observed that the existence of an arbitration agreement and the failure of the procedure for appointment of an arbitrator are the primary considerations for the court under Section 11. Once the arbitration clause is admitted, the court should leave all other preliminary issues, including the issue of compliance with pre-arbitration procedures, to be decided by the arbitral tribunal. Having considered the arguments, this Court finds that an arbitrable dispute clearly exists between the parties. The objection raised by the respondent relates to admissibility rather than jurisdiction, and therefore, falls within the domain of the arbitrator. Accordingly, Justice V. K. Sharma (Retd.) is hereby appointed as the sole arbitrator. The arbitration proceedings shall be conducted under the aegis of the Mumbai Centre for International Arbitration." },
            { type: "Family Court Appeal - Maintenance", text: "The present family court appeal is directed against the judgment and decree passed by the learned Family Court, Bandra, under Section 13(1)(ia) and (ib) of the Hindu Marriage Act, 1955. The Family Court had dissolved the marriage between the appellant-husband and the respondent-wife on the grounds of cruelty and desertion, and further directed the husband to pay permanent alimony of Rs. 25,000/- per month to the wife. The appellant has challenged only the quantum of maintenance awarded, without contesting the decree of divorce. The learned counsel for the appellant argued that the Family Court completely erred in assessing the financial capacity of the husband. It was submitted that the appellant is merely working as a junior sales executive and his take-home salary is not more than Rs. 35,000/- per month. He also has the responsibility of taking care of his aged and ailing parents. Furthermore, the counsel emphasized that the respondent-wife is a highly qualified postgraduate who was previously employed in a multinational company and is fully capable of maintaining herself. Therefore, awarding such an exorbitant amount of maintenance is punitive and unsustainable in law. On the other hand, the learned counsel for the respondent-wife supported the impugned order. It was brought to the notice of the court that the appellant had deliberately concealed his actual income by suppressing his income tax returns. The lifestyle maintained by the appellant, including the possession of luxury vehicles and frequent international travels, clearly indicates that his income is far beyond what has been disclosed in his affidavit of assets and liabilities. Regarding the wife's employment, it was clarified that she had to resign from her job due to the mental trauma and harassment inflicted by the appellant and is currently unemployed and dependent on her parents. The law is well-settled that while determining the quantum of permanent alimony, the court must consider the status of the parties, their respective needs, the capacity of the husband to pay, and the independent income of the wife, if any. The objective of Section 25 of the Act is to ensure that the wife is not rendered destitute and is able to maintain a standard of living somewhat commensurate with the status she enjoyed in her matrimonial home. Upon re-appreciating the evidence, we find that the Family Court correctly drew an adverse inference against the husband for non-disclosure of material financial documents. However, considering the overall facts and circumstances, we deem it appropriate to slightly modify the quantum. The permanent alimony is reduced from Rs. 25,000/- to Rs. 20,000/- per month. The appeal stands partly allowed." }
        ];

        const PASSAGES = Array.from({ length: 40 }, (_, i) => {
            const template = baseTemplates[i % 5];
            return {
                id: i + 1,
                title: `Passage ${i + 1} - ${template.type}`,
                text: template.text
            };
        });

        // --- APP STATE ---
        const TEST_DURATION = 600; // 10 mins
        let currentPassage = PASSAGES[0];
        let userInput = "";
        let timeLeft = TEST_DURATION;
        let status = "idle"; // idle, running, finished
        let totalKeystrokes = 0;
        let backspaceCount = 0;
        let isPaperMode = false;
        let timerInterval = null;

        // --- DOM ELEMENTS ---
        const uiSelect = document.getElementById('passage-select');
        const uiTime = document.getElementById('time-display');
        const uiWpm = document.getElementById('wpm-display');
        const uiKeystrokes = document.getElementById('keystrokes-display');
        const uiBackspaces = document.getElementById('backspaces-display');
        const uiInput = document.getElementById('typing-input');
        const uiRefText = document.getElementById('reference-text');
        
        // --- INITIALIZATION ---
        function init() {
            PASSAGES.forEach(p => {
                let opt = document.createElement('option');
                opt.value = p.id;
                opt.textContent = p.title;
                uiSelect.appendChild(opt);
            });
            renderReferenceText();
        }

        // --- CORE LOGIC ---
        function setMode(paperMode) {
            isPaperMode = paperMode;
            const btnScreen = document.getElementById('btn-screen-mode');
            const btnPaper = document.getElementById('btn-paper-mode');
            const refPanel = document.getElementById('reference-panel');
            const inputPanel = document.getElementById('input-panel');
            
            if(paperMode) {
                // Paper mode styling
                btnPaper.className = "flex items-center gap-2 px-4 py-2 rounded-md text-sm font-medium transition-all bg-white shadow text-blue-600";
                btnScreen.className = "flex items-center gap-2 px-4 py-2 rounded-md text-sm font-medium transition-all text-slate-500 hover:text-slate-700";
                refPanel.classList.add('hidden');
                inputPanel.classList.add('lg:col-span-2');
                document.getElementById('paper-mode-badge').classList.remove('hidden');
                document.getElementById('paper-mode-instruction').classList.remove('hidden');
            } else {
                // Screen mode styling
                btnScreen.className = "flex items-center gap-2 px-4 py-2 rounded-md text-sm font-medium transition-all bg-white shadow text-blue-600";
                btnPaper.className = "flex items-center gap-2 px-4 py-2 rounded-md text-sm font-medium transition-all text-slate-500 hover:text-slate-700";
                refPanel.classList.remove('hidden');
                inputPanel.classList.remove('lg:col-span-2');
                document.getElementById('paper-mode-badge').classList.add('hidden');
                document.getElementById('paper-mode-instruction').classList.add('hidden');
            }
            uiInput.focus();
        }

        function handlePassageChange() {
            const id = parseInt(uiSelect.value);
            currentPassage = PASSAGES.find(p => p.id === id);
            document.getElementById('ref-id-display').textContent = `ID: ${id}`;
            document.getElementById('badge-id').textContent = id;
            document.getElementById('instruction-id').textContent = `Passage No. ${id}`;
            resetTest();
        }

        function startTimer() {
            status = "running";
            document.getElementById('start-prompt').classList.add('hidden');
            document.getElementById('paper-mode-instruction').classList.add('hidden');
            uiSelect.disabled = true;
            
            timerInterval = setInterval(() => {
                timeLeft--;
                updateTopBar();
                if (timeLeft <= 0) {
                    finishTest();
                }
            }, 1000);
        }

        function finishTest() {
            clearInterval(timerInterval);
            status = "finished";
            uiInput.disabled = true;
            showResults();
        }

        function resetTest() {
            clearInterval(timerInterval);
            status = "idle";
            timeLeft = TEST_DURATION;
            userInput = "";
            totalKeystrokes = 0;
            backspaceCount = 0;
            uiInput.value = "";
            uiInput.disabled = false;
            uiSelect.disabled = false;
            
            document.getElementById('start-prompt').classList.remove('hidden');
            if(isPaperMode) document.getElementById('paper-mode-instruction').classList.remove('hidden');
            
            updateTopBar();
            renderReferenceText();
            uiInput.focus();
        }

        // --- INPUT HANDLING ---
        uiInput.addEventListener('keydown', (e) => {
            if (status === 'finished') { e.preventDefault(); return; }
            if (e.key === 'Tab') { e.preventDefault(); }
            
            if (e.key === 'Backspace') {
                backspaceCount++;
                uiBackspaces.textContent = backspaceCount;
            } else if (e.key.length === 1) {
                totalKeystrokes++;
                uiKeystrokes.textContent = totalKeystrokes;
            }
        });

        uiInput.addEventListener('input', (e) => {
            if (status === 'finished') return;
            
            // Prevent paste
            if (e.inputType === 'insertFromPaste') {
                uiInput.value = userInput; // revert
                return;
            }

            if (status === 'idle' && uiInput.value.length > 0) {
                startTimer();
            }

            userInput = uiInput.value;
            
            if (!isPaperMode) {
                renderReferenceText();
            }

            if (userInput === currentPassage.text) {
                finishTest();
            }
        });

        // --- RENDERING & CALCULATIONS ---
        function renderReferenceText() {
            const textArray = currentPassage.text.split("");
            const inputArray = userInput.split("");
            let html = "";

            for (let i = 0; i < textArray.length; i++) {
                let colorClass = "text-slate-500";
                let bgClass = "";
                
                if (i < inputArray.length) {
                    if (textArray[i] === inputArray[i]) {
                        colorClass = "text-green-600";
                    } else {
                        colorClass = "text-red-600";
                        bgClass = "bg-red-100";
                    }
                } else if (i === inputArray.length && status !== "finished") {
                    bgClass = "bg-blue-200 border-b-2 border-blue-600";
                    colorClass = "text-black font-semibold";
                }
                
                html += `<span class="${colorClass} ${bgClass}">${textArray[i]}</span>`;
            }
            uiRefText.innerHTML = html;
        }

        function getStats() {
            const timeElapsedInMins = (TEST_DURATION - timeLeft) / 60;
            
            const grossWPM = timeElapsedInMins > 0 
                ? Math.round((totalKeystrokes / 5) / timeElapsedInMins) 
                : 0;

            // Word-based diffing for paper mode accuracy
            const refWords = currentPassage.text.split(/\s+/);
            const typedWords = userInput.split(/\s+/).filter(w => w.length > 0);
            
            let correctC = 0;
            let errors = 0;

            for (let i = 0; i < typedWords.length; i++) {
                if (refWords[i] === typedWords[i]) {
                    correctC += typedWords[i].length + 1; 
                } else {
                    errors++;
                }
            }

            const netWPM = timeElapsedInMins > 0 
                ? Math.round((correctC / 5) / timeElapsedInMins) 
                : 0;

            const accuracy = totalKeystrokes > 0 
                ? Math.min(100, Math.max(0, Math.round((correctC / (userInput.length || 1)) * 100))) 
                : 100;

            return { grossWPM, netWPM, errors, accuracy };
        }

        function updateTopBar() {
            // Time
            const m = Math.floor(timeLeft / 60).toString().padStart(2, '0');
            const s = (timeLeft % 60).toString().padStart(2, '0');
            uiTime.innerHTML = `<i class="fa-regular fa-clock"></i> ${m}:${s}`;
            if(timeLeft <= 60) uiTime.classList.add('text-red-500', 'animate-pulse');
            else uiTime.classList.remove('text-red-500', 'animate-pulse');

            // Live WPM
            const stats = getStats();
            uiWpm.textContent = status === "idle" ? "0" : stats.grossWPM;
            uiKeystrokes.textContent = totalKeystrokes;
            uiBackspaces.textContent = backspaceCount;
        }

        function showResults() {
            const stats = getStats();
            
            document.getElementById('report-subtitle').textContent = `Passage ${currentPassage.id} • ${isPaperMode ? 'Paper Mode' : 'Screen Mode'}`;
            
            // Net Speed Card
            const netCard = document.getElementById('net-speed-card');
            const finalNetWpm = document.getElementById('final-net-wpm');
            const qualStatus = document.getElementById('qualification-status');
            
            finalNetWpm.innerHTML = `${stats.netWPM} <span class="text-2xl font-bold text-slate-400">WPM</span>`;
            
            if (stats.netWPM >= 40) {
                netCard.className = "p-6 rounded-xl border bg-green-50 border-green-200 text-center";
                finalNetWpm.className = "text-6xl font-black mb-1 text-green-600";
                qualStatus.className = "text-sm font-medium text-green-700";
                qualStatus.textContent = "✓ Qualification Passed";
            } else {
                netCard.className = "p-6 rounded-xl border bg-red-50 border-red-200 text-center";
                finalNetWpm.className = "text-6xl font-black mb-1 text-red-600";
                qualStatus.className = "text-sm font-medium text-red-700";
                qualStatus.textContent = "✗ Below 40 WPM Requirement";
            }

            document.getElementById('final-gross-wpm').innerHTML = `${stats.grossWPM} <span class="text-2xl font-bold text-slate-400">WPM</span>`;
            document.getElementById('modal-keystrokes').textContent = totalKeystrokes;
            document.getElementById('modal-backspaces').textContent = backspaceCount;
            document.getElementById('modal-errors').textContent = stats.errors;
            document.getElementById('modal-accuracy').textContent = `${stats.accuracy}%`;

            document.getElementById('results-modal').classList.remove('hidden');
        }

        // --- PRINTING ---
        function printPassagesToPDF() {
            const printWindow = window.open('', '_blank');
            let htmlContent = `
            <html><head><title>Bombay High Court - Typing Passages</title>
            <style>
                body { font-family: 'Times New Roman', serif; line-height: 1.8; color: #000; padding: 20px; font-size: 14pt; }
                .passage-container { page-break-after: always; margin-bottom: 50px; }
                .header { text-align: center; border-bottom: 2px solid #000; padding-bottom: 10px; margin-bottom: 20px; }
                h1 { font-size: 24pt; margin: 0; }
                h2 { font-size: 16pt; margin: 5px 0 20px 0; font-weight: normal; color: #444; }
                .content { text-align: justify; }
                @media print { @page { margin: 2cm; } }
            </style>
            </head><body>`;

            PASSAGES.forEach(p => {
                htmlContent += `
                <div class="passage-container">
                    <div class="header">
                        <h1>Passage No. ${p.id}</h1>
                        <h2>${p.title.split(' - ')[1]}</h2>
                    </div>
                    <div class="content"><p>${p.text}</p></div>
                </div>`;
            });

            htmlContent += '</body></html>';
            printWindow.document.write(htmlContent);
            printWindow.document.close();
            setTimeout(() => { printWindow.print(); }, 250);
        }

        // Run Init
        init();
    </script>
</body>
</html>
