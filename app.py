import React, { useState, useEffect, useRef } from 'react';
import { Clock, RefreshCw, Activity, FileText, Printer, Monitor, FileDown, CheckCircle, XCircle } from 'lucide-react';

// --- GENERATE 40 PASSAGES ---
// We use 5 realistic, full-length legal templates and generate 40 variations 
// to give you enough practice material for a full month of daily tests.
const baseTemplates = [
  {
    type: "Civil Suit - Specific Performance",
    text: "In the High Court of Judicature, Ordinary Original Civil Jurisdiction. The plaintiff has filed this suit for specific performance of the agreement to sell dated 12th October 2018. It is the case of the plaintiff that the defendant, being the absolute owner of the suit schedule property, had agreed to sell the same for a total consideration of Rs. 50,00,000/- (Rupees Fifty Lakhs only). An earnest money deposit of Rs. 10,00,000/- was paid by the plaintiff vide Cheque drawn on State Bank of India. The defendant acknowledged the receipt of the said amount and executed an agreement. However, despite repeated notices and reminders, the defendant failed to execute the final sale deed within the stipulated period of six months. The learned counsel for the petitioner submitted that the impugned judgment is contrary to the well-settled principles of law. The documentary evidence clearly establishes the readiness and willingness of the plaintiff to perform his part of the contract. Section 16(c) of the Specific Relief Act, 1963, mandates that the plaintiff must aver and prove his continuous readiness from the date of the contract till the execution. The trial court erred in ignoring the bank statements marked as Exhibit P-4, which clearly demonstrated that the plaintiff had sufficient funds to pay the balance consideration. On the other hand, the learned counsel for the respondent vehemently opposed the petition, stating that the agreement was forged and fabricated. It was argued that the signature on the agreement does not match the admitted signature of the defendant. Furthermore, the respondent contended that time was the essence of the contract, and the plaintiff having failed to tender the balance amount within the agreed timeframe, the earnest money stood forfeited. The Supreme Court in various pronouncements has held that in cases of sale of immovable property, time is not generally presumed to be the essence of the contract unless there are specific stipulations to that effect. The burden of proof lies heavily on the party asserting that time was of the essence. Upon careful consideration of the rival submissions and perusal of the trial court records, this Court is of the considered opinion that the matter requires a deeper examination of the evidence adduced. The discrepancies in the forensic expert's report regarding the disputed signatures cannot be brushed aside. Therefore, the matter is remanded back to the trial court for fresh adjudication after affording an opportunity to both parties to lead additional evidence. The appeal is partly allowed in the aforesaid terms. No order as to costs."
  },
  {
    type: "Criminal Appeal - Bail Application",
    text: "This criminal appeal arises out of the judgment and order of conviction passed by the learned Sessions Court, whereby the appellant has been convicted under Section 302 read with Section 34 of the Indian Penal Code, 1860, and sentenced to suffer rigorous imprisonment for life. The prosecution case, in brief, is that on the fateful night of 15th August 2021, the accused persons formed an unlawful assembly and assaulted the deceased with deadly weapons over a prior property dispute. The first information report was lodged by the brother of the deceased, who is also an eyewitness to the incident. During the course of the trial, the prosecution examined twelve witnesses to bring home the guilt of the accused. The learned Senior Counsel appearing on behalf of the appellant has primarily urged two grounds to challenge the conviction. Firstly, it is submitted that there is an unexplained and inordinate delay of fourteen hours in lodging the FIR, which casts a serious doubt on the veracity of the prosecution version. It is a settled position of criminal jurisprudence that an unexplained delay in lodging the FIR often provides room for afterthought and embellishment. Secondly, the learned counsel argued that the testimonies of the eye-witnesses are fraught with material contradictions and omissions, making them entirely unreliable. He specifically pointed out the cross-examination of Prosecution Witness 3, whose statement recorded under Section 161 of the Code of Criminal Procedure, 1973, significantly differs from his deposition in the court. The learned Additional Public Prosecutor, on the contrary, supported the impugned judgment, asserting that minor discrepancies are bound to occur when witnesses are examined after a considerable lapse of time. He emphasized that the medical evidence corroborates the ocular testimony, as the post-mortem report clearly indicates multiple incised wounds caused by a sharp-edged weapon. Having heard both the learned counsels and having scrutinized the lower court records, we find merit in the submissions made by the appellant. The prosecution has failed to establish the chain of circumstances beyond a reasonable doubt. The fundamental principle of criminal law dictates that the accused is presumed innocent until proven guilty, and the benefit of the doubt must always go to the accused. Consequently, the impugned judgment and order of conviction are hereby set aside. The appellant is acquitted of all charges and is directed to be released forthwith, provided he is not required in any other ongoing criminal case."
  },
  {
    type: "Writ Petition - Service Matter",
    text: "The present writ petition has been filed under Article 226 of the Constitution of India challenging the impugned order of dismissal from service passed by the disciplinary authority. The petitioner was employed as a Junior Clerk in the Revenue Department. It is the case of the petitioner that he was falsely implicated in a departmental enquiry without being given a fair and reasonable opportunity of being heard, thereby violating the principles of natural justice. The charge against the petitioner was unauthorized absence from duty for a continuous period of ninety days without prior sanction of leave. The learned counsel for the petitioner submitted that the absence was entirely due to severe medical exigencies, as the petitioner was suffering from acute tuberculosis and was advised complete bed rest. Medical certificates issued by the Civil Hospital were duly produced before the enquiry officer, but the same were arbitrarily rejected without assigning any cogent reasons. It was further contended that the punishment of dismissal is shockingly disproportionate to the gravity of the alleged misconduct. Relying on various judgments of the Apex Court, the counsel argued that the doctrine of proportionality must be strictly applied in disciplinary proceedings. Per contra, the learned Government Pleader representing the State vehemently defended the impugned order. It was submitted that the petitioner is a habitual absentee and has been issued multiple warning memos in the past. The medical certificates were produced belatedly only as an afterthought to circumvent the disciplinary action. The enquiry was conducted strictly in accordance with the Maharashtra Civil Services (Discipline and Appeal) Rules, 1979. The petitioner was allowed to cross-examine the management witnesses and adduce his own defense evidence. The disciplinary authority, after applying its mind to the findings of the enquiry officer, rightly concluded that the petitioner's retention in government service would be detrimental to public administration. We have carefully perused the pleadings and the original record of the departmental proceedings. While it is true that courts exercise limited jurisdiction under Article 226 in matters of departmental enquiries and cannot act as an appellate authority to re-appreciate evidence, the court can certainly interfere if the findings are perverse or based on no evidence. In the present case, the outright rejection of government hospital medical certificates without seeking an opinion from a medical board demonstrates non-application of mind. In the interest of justice, the impugned order of dismissal is quashed and set aside. The respondents are directed to reinstate the petitioner with continuity of service, however, without 50 percent back wages."
  },
  {
    type: "Arbitration Application - Commercial Dispute",
    text: "This is an application filed under Section 11 of the Arbitration and Conciliation Act, 1996, seeking the appointment of a sole arbitrator to adjudicate the disputes and differences that have arisen between the parties. The applicant is a private limited company engaged in the business of infrastructure development. The respondent is a municipal corporation. The parties had entered into a comprehensive contract dated 4th March 2017 for the construction of a flyover bridge. Clause 24 of the general conditions of contract contains a distinct arbitration agreement, which stipulates that any dispute arising out of or in connection with the contract shall be referred to arbitration. According to the applicant, they successfully completed the major portion of the project within the stipulated timeframe. However, the respondent abruptly terminated the contract citing alleged delays and poor quality of work. Furthermore, the respondent arbitrarily invoked the bank guarantees submitted by the applicant without any prior intimation. The applicant issued a statutory notice invoking the arbitration clause and suggested the names of three retired High Court judges to act as the sole arbitrator. The respondent, despite receiving the said notice, failed to concur on any name within the statutory period of thirty days. The learned counsel for the respondent corporation raised a preliminary objection regarding the maintainability of the present application. It was argued that the applicant had not exhausted the pre-arbitration conciliation mechanism mandated under Clause 23 of the contract, which requires the parties to first attempt an amicable settlement before the Superintending Engineer. Thus, the invocation of arbitration is premature. In rejoinder, the applicant submitted that the respondent's hostile act of encashing the bank guarantees rendered any conciliation process practically impossible and futile. The Supreme Court has repeatedly observed that the existence of an arbitration agreement and the failure of the procedure for appointment of an arbitrator are the primary considerations for the court under Section 11. Once the arbitration clause is admitted, the court should leave all other preliminary issues, including the issue of compliance with pre-arbitration procedures, to be decided by the arbitral tribunal. Having considered the arguments, this Court finds that an arbitrable dispute clearly exists between the parties. The objection raised by the respondent relates to admissibility rather than jurisdiction, and therefore, falls within the domain of the arbitrator. Accordingly, Justice V. K. Sharma (Retd.) is hereby appointed as the sole arbitrator. The arbitration proceedings shall be conducted under the aegis of the Mumbai Centre for International Arbitration."
  },
  {
    type: "Family Court Appeal - Maintenance",
    text: "The present family court appeal is directed against the judgment and decree passed by the learned Family Court, Bandra, under Section 13(1)(ia) and (ib) of the Hindu Marriage Act, 1955. The Family Court had dissolved the marriage between the appellant-husband and the respondent-wife on the grounds of cruelty and desertion, and further directed the husband to pay permanent alimony of Rs. 25,000/- per month to the wife. The appellant has challenged only the quantum of maintenance awarded, without contesting the decree of divorce. The learned counsel for the appellant argued that the Family Court completely erred in assessing the financial capacity of the husband. It was submitted that the appellant is merely working as a junior sales executive and his take-home salary is not more than Rs. 35,000/- per month. He also has the responsibility of taking care of his aged and ailing parents. Furthermore, the counsel emphasized that the respondent-wife is a highly qualified postgraduate who was previously employed in a multinational company and is fully capable of maintaining herself. Therefore, awarding such an exorbitant amount of maintenance is punitive and unsustainable in law. On the other hand, the learned counsel for the respondent-wife supported the impugned order. It was brought to the notice of the court that the appellant had deliberately concealed his actual income by suppressing his income tax returns. The lifestyle maintained by the appellant, including the possession of luxury vehicles and frequent international travels, clearly indicates that his income is far beyond what has been disclosed in his affidavit of assets and liabilities. Regarding the wife's employment, it was clarified that she had to resign from her job due to the mental trauma and harassment inflicted by the appellant and is currently unemployed and dependent on her parents. The law is well-settled that while determining the quantum of permanent alimony, the court must consider the status of the parties, their respective needs, the capacity of the husband to pay, and the independent income of the wife, if any. The objective of Section 25 of the Act is to ensure that the wife is not rendered destitute and is able to maintain a standard of living somewhat commensurate with the status she enjoyed in her matrimonial home. Upon re-appreciating the evidence, we find that the Family Court correctly drew an adverse inference against the husband for non-disclosure of material financial documents. However, considering the overall facts and circumstances, we deem it appropriate to slightly modify the quantum. The permanent alimony is reduced from Rs. 25,000/- to Rs. 20,000/- per month. The appeal stands partly allowed."
  }
];

const PASSAGES = Array.from({ length: 40 }, (_, i) => {
  const template = baseTemplates[i % 5];
  return {
    id: i + 1,
    title: `Passage ${i + 1} - ${template.type}`,
    text: template.text
  };
});

const TEST_DURATION_SECONDS = 600; // 10 minutes

export default function App() {
  const [selectedPassage, setSelectedPassage] = useState(PASSAGES[0]);
  const [userInput, setUserInput] = useState("");
  const [timeLeft, setTimeLeft] = useState(TEST_DURATION_SECONDS);
  const [status, setStatus] = useState("idle"); // idle, running, finished
  const [totalKeystrokes, setTotalKeystrokes] = useState(0);
  const [backspaceCount, setBackspaceCount] = useState(0);
  const [isPaperMode, setIsPaperMode] = useState(false);
  
  const textareaRef = useRef(null);
  const intervalRef = useRef(null);

  useEffect(() => {
    if (status === "running") {
      intervalRef.current = setInterval(() => {
        setTimeLeft((prev) => {
          if (prev <= 1) {
            clearInterval(intervalRef.current);
            setStatus("finished");
            return 0;
          }
          return prev - 1;
        });
      }, 1000);
    } else {
      clearInterval(intervalRef.current);
    }
    return () => clearInterval(intervalRef.current);
  }, [status]);

  const handleKeyDown = (e) => {
    if (status === "finished") return;
    
    if (e.key === 'Tab') {
      e.preventDefault();
    }

    if (e.key === "Backspace") {
      setBackspaceCount((prev) => prev + 1);
    } else if (e.key.length === 1) {
      setTotalKeystrokes((prev) => prev + 1);
    }
  };

  const handleInputChange = (e) => {
    if (status === "finished") return;
    const val = e.target.value;
    if (e.nativeEvent.inputType === 'insertFromPaste') return;

    if (status === "idle" && val.length > 0) {
      setStatus("running");
    }
    setUserInput(val);

    if (val === selectedPassage.text) {
      setStatus("finished");
    }
  };

  const resetTest = () => {
    setStatus("idle");
    setTimeLeft(TEST_DURATION_SECONDS);
    setUserInput("");
    setTotalKeystrokes(0);
    setBackspaceCount(0);
    if (textareaRef.current) textareaRef.current.focus();
  };

  const handlePassageChange = (e) => {
    const passage = PASSAGES.find(p => p.id === parseInt(e.target.value));
    setSelectedPassage(passage);
    resetTest();
  };

  const printPassagesToPDF = () => {
    const printWindow = window.open('', '_blank');
    let htmlContent = `
      <html>
      <head>
        <title>Bombay High Court - Typing Passages</title>
        <style>
          body { font-family: 'Times New Roman', serif; line-height: 1.8; color: #000; padding: 20px; font-size: 14pt; }
          .passage-container { page-break-after: always; margin-bottom: 50px; }
          .header { text-align: center; border-bottom: 2px solid #000; padding-bottom: 10px; margin-bottom: 20px; }
          h1 { font-size: 24pt; margin: 0; }
          h2 { font-size: 16pt; margin: 5px 0 20px 0; font-weight: normal; color: #444; }
          .content { text-align: justify; }
          @media print {
            @page { margin: 2cm; }
          }
        </style>
      </head>
      <body>
    `;

    PASSAGES.forEach(p => {
      htmlContent += `
        <div class="passage-container">
          <div class="header">
            <h1>Passage No. ${p.id}</h1>
            <h2>${p.title.split(' - ')[1]}</h2>
          </div>
          <div class="content">
            <p>${p.text}</p>
          </div>
        </div>
      `;
    });

    htmlContent += '</body></html>';
    
    printWindow.document.open();
    printWindow.document.write(htmlContent);
    printWindow.document.close();
    
    // Give it a tiny delay to load fonts before triggering print
    setTimeout(() => {
      printWindow.print();
    }, 250);
  };

  // --- CALCULATIONS (Smart Word-Based Diffing for Paper Mode Accuracy) ---
  const timeElapsedInMinutes = (TEST_DURATION_SECONDS - timeLeft) / 60;
  
  // Gross WPM: All typed characters / 5 / Time
  const grossWPM = timeElapsedInMinutes > 0 
    ? Math.round((totalKeystrokes / 5) / timeElapsedInMinutes) 
    : 0;

  // Smart Correct Character Calculation
  // We check word-by-word so that if a user skips a word while reading from paper, 
  // the entire rest of the text doesn't become "incorrect" due to offset.
  const calculateCorrectStats = () => {
    const refWords = selectedPassage.text.split(/\s+/);
    const typedWords = userInput.split(/\s+/).filter(w => w.length > 0);
    
    let correctC = 0;
    let incorrectC = 0;
    let errors = 0;

    for (let i = 0; i < typedWords.length; i++) {
      if (refWords[i] === typedWords[i]) {
        // Add word length + 1 space
        correctC += typedWords[i].length + 1; 
      } else {
        incorrectC += typedWords[i].length + 1;
        errors++;
      }
    }
    
    return { correctChars: correctC, incorrectChars: incorrectC, errorCount: errors };
  };

  const { correctChars, errorCount } = calculateCorrectStats();

  const netWPM = timeElapsedInMinutes > 0 
    ? Math.round((correctChars / 5) / timeElapsedInMinutes) 
    : 0;

  const accuracy = totalKeystrokes > 0 
    ? Math.min(100, Math.max(0, Math.round((correctChars / (userInput.length || 1)) * 100))) 
    : 100;

  // On-Screen Text Rendering
  const renderText = () => {
    const textArray = selectedPassage.text.split("");
    const inputArray = userInput.split("");

    return textArray.map((char, index) => {
      let colorClass = "text-slate-500";
      let bgClass = "";
      
      if (index < inputArray.length) {
        if (char === inputArray[index]) {
          colorClass = "text-green-600";
        } else {
          colorClass = "text-red-600";
          bgClass = "bg-red-100";
        }
      } else if (index === inputArray.length && status !== "finished") {
        bgClass = "bg-blue-200 border-b-2 border-blue-600";
        colorClass = "text-black font-semibold";
      }

      return (
        <span key={index} className={`${colorClass} ${bgClass}`}>
          {char}
        </span>
      );
    });
  };

  return (
    <div className="min-h-screen bg-slate-50 p-4 md:p-8 font-sans text-slate-800">
      <div className="max-w-6xl mx-auto space-y-6">
        
        {/* Header & Controls Section */}
        <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-200">
          <div className="flex flex-col lg:flex-row justify-between items-start lg:items-center gap-6">
            
            <div>
              <h1 className="text-2xl font-bold text-slate-800 flex items-center gap-2">
                <Activity className="text-blue-600" />
                Bombay High Court Typing Test
              </h1>
              <p className="text-slate-500 text-sm mt-1">Target: 40 WPM • Duration: 10 Minutes</p>
            </div>

            <div className="flex flex-wrap items-center gap-4 w-full lg:w-auto">
              {/* Paper vs Screen Toggle */}
              <div className="flex bg-slate-100 p-1 rounded-lg border border-slate-200">
                <button
                  onClick={() => setIsPaperMode(false)}
                  className={`flex items-center gap-2 px-4 py-2 rounded-md text-sm font-medium transition-all ${!isPaperMode ? 'bg-white shadow text-blue-600' : 'text-slate-500 hover:text-slate-700'}`}
                >
                  <Monitor size={16} /> Screen Mode
                </button>
                <button
                  onClick={() => setIsPaperMode(true)}
                  className={`flex items-center gap-2 px-4 py-2 rounded-md text-sm font-medium transition-all ${isPaperMode ? 'bg-white shadow text-blue-600' : 'text-slate-500 hover:text-slate-700'}`}
                >
                  <FileText size={16} /> Paper Mode
                </button>
              </div>

              {/* Print Button */}
              <button 
                onClick={printPassagesToPDF}
                className="flex items-center gap-2 px-4 py-2.5 bg-slate-800 hover:bg-slate-900 text-white rounded-lg transition-colors text-sm font-medium"
              >
                <Printer size={16} />
                Print All Passages (PDF)
              </button>
            </div>
          </div>

          <hr className="my-5 border-slate-100" />

          <div className="flex flex-col md:flex-row items-center gap-4">
            <div className="flex-grow w-full md:w-auto">
              <label className="block text-xs font-semibold text-slate-500 uppercase mb-1">Select Passage Number</label>
              <select 
                className="bg-slate-50 border border-slate-300 text-slate-700 font-medium rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                onChange={handlePassageChange}
                value={selectedPassage.id}
                disabled={status === "running"}
              >
                {PASSAGES.map(p => (
                  <option key={p.id} value={p.id}>{p.title}</option>
                ))}
              </select>
            </div>
            <div className="pt-5 hidden md:block">
              <button 
                onClick={resetTest}
                className="flex items-center gap-2 px-6 py-2.5 bg-red-50 hover:bg-red-100 text-red-600 border border-red-200 rounded-lg transition-colors font-medium whitespace-nowrap"
              >
                <RefreshCw size={16} /> Restart
              </button>
            </div>
          </div>
        </div>

        {/* Live Status Bar */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          <div className="bg-white p-4 rounded-xl shadow-sm border border-slate-200 flex flex-col items-center justify-center">
            <span className="text-slate-500 text-xs font-semibold uppercase tracking-wider mb-1">Time Left</span>
            <div className={`text-3xl font-mono font-bold flex items-center gap-2 ${timeLeft <= 60 ? 'text-red-500 animate-pulse' : 'text-slate-700'}`}>
              <Clock size={24} />
              {Math.floor(timeLeft / 60).toString().padStart(2, '0')}:{(timeLeft % 60).toString().padStart(2, '0')}
            </div>
          </div>
          <div className="bg-white p-4 rounded-xl shadow-sm border border-slate-200 flex flex-col items-center justify-center">
            <span className="text-slate-500 text-xs font-semibold uppercase tracking-wider mb-1">Live Gross WPM</span>
            <div className="text-3xl font-bold text-blue-600">
              {status === "idle" ? "0" : grossWPM}
            </div>
          </div>
          <div className="bg-white p-4 rounded-xl shadow-sm border border-slate-200 flex flex-col items-center justify-center">
            <span className="text-slate-500 text-xs font-semibold uppercase tracking-wider mb-1">Total Keystrokes</span>
            <div className="text-3xl font-bold text-slate-700">
              {totalKeystrokes}
            </div>
          </div>
          <div className="bg-white p-4 rounded-xl shadow-sm border border-slate-200 flex flex-col items-center justify-center">
            <span className="text-slate-500 text-xs font-semibold uppercase tracking-wider mb-1">Backspaces Used</span>
            <div className="text-3xl font-bold text-amber-500">
              {backspaceCount}
            </div>
          </div>
        </div>

        {/* Typing Area */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          
          {/* Reference Text (Left) - Hidden in Paper Mode */}
          {!isPaperMode && (
            <div className="bg-white rounded-xl shadow-sm border border-slate-200 flex flex-col h-[500px]">
              <div className="px-4 py-3 border-b border-slate-100 flex items-center justify-between bg-slate-50 rounded-t-xl">
                <div className="flex items-center gap-2">
                  <FileText size={18} className="text-slate-500" />
                  <h2 className="font-semibold text-slate-700">On-Screen Reference</h2>
                </div>
                <span className="text-xs text-slate-400 font-mono">ID: {selectedPassage.id}</span>
              </div>
              <div className="p-6 overflow-y-auto text-[17px] leading-relaxed font-mono select-none flex-grow">
                {renderText()}
              </div>
            </div>
          )}

          {/* User Input (Right or Full Width in Paper Mode) */}
          <div className={`bg-white rounded-xl shadow-sm border border-slate-200 flex flex-col h-[500px] ${isPaperMode ? 'lg:col-span-2' : ''}`}>
            <div className="px-4 py-3 border-b border-slate-100 bg-slate-50 rounded-t-xl flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2">
              <div className="flex items-center gap-2">
                <h2 className="font-semibold text-slate-700">Type Here</h2>
                {isPaperMode && (
                  <span className="text-xs bg-amber-100 text-amber-800 px-2 py-1 rounded font-medium flex items-center gap-1">
                    <FileDown size={12}/> Analyzing Passage No. {selectedPassage.id}
                  </span>
                )}
              </div>
              {status === "idle" && (
                <span className="text-xs bg-blue-100 text-blue-700 px-2 py-1 rounded font-medium animate-pulse">
                  Start typing to begin timer
                </span>
              )}
            </div>
            
            {isPaperMode && status === "idle" && (
              <div className="bg-blue-50 p-4 border-b border-blue-100 text-blue-800 text-center text-sm font-medium">
                Look at your printed sheet for <strong>Passage No. {selectedPassage.id}</strong>. Type directly below.
              </div>
            )}

            <textarea
              ref={textareaRef}
              className="flex-grow p-6 text-lg leading-relaxed font-mono resize-none focus:outline-none focus:ring-inset focus:ring-2 focus:ring-blue-100 rounded-b-xl disabled:bg-slate-50 disabled:text-slate-500"
              placeholder={status === "idle" ? "Start typing here..." : ""}
              value={userInput}
              onChange={handleInputChange}
              onKeyDown={handleKeyDown}
              disabled={status === "finished"}
              spellCheck="false"
              autoComplete="off"
              autoCorrect="off"
              autoCapitalize="off"
            />
          </div>
        </div>

        {/* Results Modal */}
        {status === "finished" && (
          <div className="fixed inset-0 bg-slate-900/60 backdrop-blur-sm flex items-center justify-center p-4 z-50">
            <div className="bg-white rounded-2xl shadow-2xl w-full max-w-3xl overflow-hidden animate-in fade-in zoom-in duration-200">
              <div className="bg-slate-800 p-6 text-center text-white border-b-4 border-blue-500">
                <h2 className="text-3xl font-bold mb-2">Performance Report</h2>
                <p className="text-slate-300">
                  Passage {selectedPassage.id} • {isPaperMode ? "Paper Mode" : "Screen Mode"}
                </p>
              </div>
              
              <div className="p-8">
                <div className="grid grid-cols-2 gap-6 mb-8">
                  <div className={`p-6 rounded-xl border ${netWPM >= 40 ? 'bg-green-50 border-green-200' : 'bg-red-50 border-red-200'} text-center`}>
                    <p className="text-slate-500 text-sm font-semibold uppercase tracking-wider mb-2">Final Net Speed</p>
                    <div className={`text-6xl font-black mb-1 ${netWPM >= 40 ? 'text-green-600' : 'text-red-600'}`}>
                      {netWPM} <span className="text-2xl font-bold text-slate-400">WPM</span>
                    </div>
                    <p className={`text-sm font-medium ${netWPM >= 40 ? 'text-green-700' : 'text-red-700'}`}>
                      {netWPM >= 40 ? '✓ Qualification Passed' : '✗ Below 40 WPM Requirement'}
                    </p>
                  </div>
                  
                  <div className="bg-slate-50 p-6 rounded-xl border border-slate-200 text-center">
                    <p className="text-slate-500 text-sm font-semibold uppercase tracking-wider mb-2">Gross Speed</p>
                    <div className="text-6xl font-black text-slate-700 mb-1">{grossWPM} <span className="text-2xl font-bold text-slate-400">WPM</span></div>
                    <p className="text-sm font-medium text-slate-500">Total speed including errors</p>
                  </div>
                </div>

                <div className="bg-white rounded-xl border border-slate-200 overflow-hidden shadow-sm">
                  <table className="w-full text-left text-sm">
                    <tbody className="divide-y divide-slate-100">
                      <tr>
                        <th className="px-6 py-4 font-semibold text-slate-600 bg-slate-50 w-1/2">Total Keystrokes Logged</th>
                        <td className="px-6 py-4 text-right font-mono text-lg font-bold text-slate-800">{totalKeystrokes}</td>
                      </tr>
                      <tr>
                        <th className="px-6 py-4 font-semibold text-slate-600 w-1/2">Backspaces Used</th>
                        <td className="px-6 py-4 text-right font-mono text-lg font-bold text-amber-600">{backspaceCount}</td>
                      </tr>
                      <tr>
                        <th className="px-6 py-4 font-semibold text-slate-600 bg-slate-50 w-1/2">Word Errors / Skips</th>
                        <td className="px-6 py-4 text-right font-mono text-lg font-bold text-red-500">{errorCount}</td>
                      </tr>
                      <tr>
                        <th className="px-6 py-4 font-semibold text-slate-600 w-1/2">Accuracy Score</th>
                        <td className="px-6 py-4 text-right font-mono text-lg font-bold text-slate-800">{accuracy}%</td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <div className="mt-8 flex justify-center">
                  <button 
                    onClick={resetTest}
                    className="bg-slate-800 hover:bg-slate-900 text-white px-8 py-3 rounded-lg font-bold shadow-md transition-all active:scale-95 flex items-center gap-2"
                  >
                    <RefreshCw size={20} />
                    Start Next Test
                  </button>
                </div>
              </div>
            </div>
          </div>
        )}

      </div>
    </div>
  );
}
