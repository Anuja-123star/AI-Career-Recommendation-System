import React, { useState, useRef } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Button } from "@/components/ui/button";
import { Progress } from "@/components/ui/progress";
import {
  Shield, BrainCircuit, Code2,
  ChevronRight, RefreshCcw, Microscope, Leaf, FlaskConical,
  Headphones, Briefcase, Cloud,
  ShieldCheck, Landmark, Medal, Scale,
  BookOpen, Download,
} from "lucide-react";
type Scores = {
  ai: number;
  cyber: number;
  web: number;
  bio: number;
  enviro: number;
  research: number;
  support: number;
  ba: number;
  cloud: number;
  police: number;
  ias: number;
  defense: number;
  law: number;
};
const QUESTIONS = [
  { text: "Do you enjoy Mathematics?",                                              weights: { ai: 2, cyber: 0, web: 0, bio: 0, enviro: 0, research: 1, support: 0, ba: 1, cloud: 0, police: 0, ias: 0, defense: 0, law: 0 } },
  { text: "Are you interested in computer security?",                               weights: { ai: 0, cyber: 3, web: 0, bio: 0, enviro: 0, research: 0, support: 1, ba: 0, cloud: 1, police: 0, ias: 0, defense: 0, law: 0 } },
  { text: "Do you enjoy designing websites?",                                       weights: { ai: 0, cyber: 0, web: 3, bio: 0, enviro: 0, research: 0, support: 0, ba: 0, cloud: 0, police: 0, ias: 0, defense: 0, law: 0 } },
  { text: "Are you interested in Artificial Intelligence?",                         weights: { ai: 3, cyber: 0, web: 0, bio: 0, enviro: 0, research: 0, support: 0, ba: 0, cloud: 0, police: 0, ias: 0, defense: 0, law: 0 } },
  { text: "Do you enjoy solving logical problems?",                                 weights: { ai: 2, cyber: 1, web: 0, bio: 0, enviro: 0, research: 1, support: 0, ba: 1, cloud: 1, police: 0, ias: 1, defense: 0, law: 1 } },
  { text: "Do you enjoy creating user-friendly applications?",                      weights: { ai: 0, cyber: 0, web: 2, bio: 0, enviro: 0, research: 0, support: 1, ba: 1, cloud: 0, police: 0, ias: 0, defense: 0, law: 0 } },
  { text: "Do you enjoy conducting experiments in a laboratory?",                   weights: { ai: 0, cyber: 0, web: 0, bio: 2, enviro: 1, research: 3, support: 0, ba: 0, cloud: 0, police: 0, ias: 0, defense: 0, law: 0 } },
  { text: "Are you interested in how living organisms work?",                       weights: { ai: 0, cyber: 0, web: 0, bio: 3, enviro: 1, research: 1, support: 0, ba: 0, cloud: 0, police: 0, ias: 0, defense: 0, law: 0 } },
  { text: "Do you care about environmental issues and sustainability?",             weights: { ai: 0, cyber: 0, web: 0, bio: 0, enviro: 3, research: 1, support: 0, ba: 0, cloud: 0, police: 0, ias: 1, defense: 0, law: 0 } },
  { text: "Are you interested in studying chemistry or biology?",                   weights: { ai: 0, cyber: 0, web: 0, bio: 2, enviro: 1, research: 2, support: 0, ba: 0, cloud: 0, police: 0, ias: 0, defense: 0, law: 0 } },
  { text: "Do you enjoy helping others solve technical problems?",                  weights: { ai: 0, cyber: 0, web: 0, bio: 0, enviro: 0, research: 0, support: 3, ba: 1, cloud: 1, police: 0, ias: 0, defense: 0, law: 0 } },
  { text: "Are you interested in how businesses operate and improve?",              weights: { ai: 0, cyber: 0, web: 0, bio: 0, enviro: 0, research: 0, support: 0, ba: 3, cloud: 0, police: 0, ias: 1, defense: 0, law: 0 } },
  { text: "Do you like managing projects and coordinating teams?",                  weights: { ai: 0, cyber: 0, web: 0, bio: 0, enviro: 0, research: 0, support: 1, ba: 3, cloud: 1, police: 0, ias: 2, defense: 1, law: 0 } },
  { text: "Are you comfortable working with servers and cloud infrastructure?",     weights: { ai: 0, cyber: 1, web: 0, bio: 0, enviro: 0, research: 0, support: 1, ba: 0, cloud: 3, police: 0, ias: 0, defense: 0, law: 0 } },
  { text: "Do you have a strong sense of justice and wish to serve the public?",    weights: { ai: 0, cyber: 0, web: 0, bio: 0, enviro: 0, research: 0, support: 0, ba: 0, cloud: 0, police: 2, ias: 2, defense: 2, law: 2 } },
  { text: "Are you interested in governance, policy-making, and administration?",   weights: { ai: 0, cyber: 0, web: 0, bio: 0, enviro: 0, research: 0, support: 0, ba: 1, cloud: 0, police: 0, ias: 3, defense: 0, law: 1 } },
  { text: "Do you enjoy physical fitness and thrive in disciplined environments?",  weights: { ai: 0, cyber: 0, web: 0, bio: 0, enviro: 0, research: 0, support: 0, ba: 0, cloud: 0, police: 2, ias: 0, defense: 3, law: 0 } },
  { text: "Are you drawn to protecting people and maintaining law and order?",      weights: { ai: 0, cyber: 0, web: 0, bio: 0, enviro: 0, research: 0, support: 0, ba: 0, cloud: 0, police: 3, ias: 1, defense: 2, law: 1 } },
  { text: "Are you interested in law, rights, and the legal system?",               weights: { ai: 0, cyber: 0, web: 0, bio: 0, enviro: 0, research: 0, support: 0, ba: 0, cloud: 0, police: 1, ias: 1, defense: 0, law: 3 } },
];
const CAREERS: Record<keyof Scores, { title: string; desc: string; icon: React.ElementType; study: string[]; image: string }> = {
  ai:       { title: "AI Engineer",              desc: "You have strong interests in AI, problem-solving, and intelligent systems.",                       icon: BrainCircuit, image: "https://images.unsplash.com/photo-1677442135703-1787eea5ce01?w=800&h=400&fit=crop&q=80", study: ["B.Sc / B.Tech in Computer Science or Mathematics", "Specialise in Machine Learning or Data Science (M.Tech / M.S.)", "Certifications: TensorFlow Developer, AWS Machine Learning, DeepLearning.AI"] },
  cyber:    { title: "Cybersecurity Analyst",    desc: "You have a strong inclination towards security, networks, and protecting systems.",                icon: Shield,        image: "https://images.unsplash.com/photo-1563986768494-4747e5e4ab7b?w=800&h=400&fit=crop&q=80", study: ["B.Sc / B.Tech in Computer Science or Information Security", "Certifications: CEH, CISSP, CompTIA Security+, OSCP", "Practice on platforms like TryHackMe or HackTheBox"] },
  web:      { title: "Web Developer",            desc: "You enjoy building websites and creating user-friendly applications.",                             icon: Code2,         image: "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=800&h=400&fit=crop&q=80", study: ["B.Sc in Computer Science or a Web Development bootcamp", "Master HTML, CSS, JavaScript, and a framework like React or Vue", "Build a portfolio of projects on GitHub"] },
  bio:      { title: "Biomedical Scientist",     desc: "You are drawn to understanding living systems and applying science to improve human health.",      icon: Microscope,    image: "https://images.unsplash.com/photo-1576086213369-97a306d36557?w=800&h=400&fit=crop&q=80", study: ["B.Sc in Biomedical Science, Biology, or Biochemistry", "M.Sc or Ph.D for research or clinical specialisation", "Look into MBBS + research track or medical laboratory science"] },
  enviro:   { title: "Environmental Scientist",  desc: "You are passionate about studying and protecting our natural world and ecosystems.",                icon: Leaf,          image: "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=800&h=400&fit=crop&q=80", study: ["B.Sc in Environmental Science, Ecology, or Geography", "M.Sc for specialisation in climate science or conservation", "Internships with NGOs, government environmental agencies, or research institutes"] },
  research: { title: "Research Scientist",       desc: "You thrive on discovery, experimentation, and pushing the boundaries of human knowledge.",         icon: FlaskConical,  image: "https://images.unsplash.com/photo-1532187863486-abf9dbad1b69?w=800&h=400&fit=crop&q=80", study: ["B.Sc in Chemistry, Biology, or Physics", "M.Sc followed by a Ph.D in your field of interest", "Publish papers and apply for research fellowships (CSIR, DST, ICMR)"] },
  support:  { title: "IT Support Specialist",    desc: "You are a natural problem-solver who finds satisfaction in helping people navigate technology.",   icon: Headphones,    image: "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=800&h=400&fit=crop&q=80", study: ["Diploma or B.Sc in Information Technology or Computer Science", "Certifications: CompTIA A+, ITIL Foundation, Microsoft 365 Fundamentals", "Gain hands-on experience with networking and helpdesk tools"] },
  ba:       { title: "Business Analyst",         desc: "You bridge the gap between technology and business, turning needs into clear solutions.",          icon: Briefcase,     image: "https://images.unsplash.com/photo-1553484771-047a44eee27b?w=800&h=400&fit=crop&q=80", study: ["B.B.A, B.Com, or B.Tech with an MBA", "Certifications: CBAP, PMI-PBA, or Agile/Scrum certifications", "Learn tools like Excel, SQL, Tableau, and JIRA"] },
  cloud:    { title: "Cloud Engineer",           desc: "You enjoy building and managing scalable infrastructure that powers modern applications.",         icon: Cloud,         image: "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=800&h=400&fit=crop&q=80", study: ["B.Tech / B.Sc in Computer Science or IT", "Certifications: AWS Solutions Architect, Google Cloud Professional, Azure Administrator", "Build hands-on projects on cloud platforms using free tiers"] },
  police:   { title: "Police Officer",           desc: "You are driven by a strong sense of duty, justice, and a desire to protect your community.",      icon: ShieldCheck,   image: "https://images.unsplash.com/photo-1589578527966-fdac0f44566c?w=800&h=400&fit=crop&q=80", study: ["Appear for SSC CPO (Central Police Organisations) or State Police Exams (via State PSC)", "Eligibility: 10+2 or Graduation depending on the rank applied for", "Focus on physical fitness, General Knowledge, and Reasoning"] },
  ias:      { title: "Civil Services (IAS/IPS)", desc: "You are drawn to governance, public administration, and shaping policy for a better society.",    icon: Landmark,      image: "https://images.unsplash.com/photo-1568992687947-868a62a9f521?w=800&h=400&fit=crop&q=80", study: ["Complete any Graduation degree (any stream)", "Prepare for UPSC Civil Services Exam (Prelims → Mains → Interview)", "Key subjects: History, Geography, Polity, Economics, Current Affairs, Ethics"] },
  defense:  { title: "Defense Officer",          desc: "You excel in disciplined, high-stakes environments and are committed to national service.",        icon: Medal,         image: "https://images.unsplash.com/photo-1551376347-075b0121a65b?w=800&h=400&fit=crop&q=80", study: ["Appear for NDA (after 10+2) or CDS / AFCAT (after Graduation)", "Indian Military / Naval / Air Force Academy training follows selection", "Focus on Mathematics, English, General Knowledge, and physical fitness"] },
  law:      { title: "Legal Professional",       desc: "You have a keen sense of fairness, sharp reasoning, and a passion for upholding rights and law.", icon: Scale,         image: "https://images.unsplash.com/photo-1589829085413-56de8ae18c73?w=800&h=400&fit=crop&q=80", study: ["Pursue LLB (3-year after graduation) or integrated BA LLB / B.Com LLB (5-year)", "Enroll with the Bar Council of India to practice", "Consider specialisations: Criminal Law, Corporate Law, Constitutional Law"] },
};
const emptyScores = (): Scores => ({
  ai: 0, cyber: 0, web: 0,
  bio: 0, enviro: 0, research: 0,
  support: 0, ba: 0, cloud: 0,
  police: 0, ias: 0, defense: 0, law: 0,
});
export default function App() {
  const [screen, setScreen] = useState<"welcome" | "quiz" | "results">("welcome");
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [scores, setScores] = useState<Scores>(emptyScores());
  const [loadedImages, setLoadedImages] = useState<Set<string>>(new Set());
  const [downloading, setDownloading] = useState(false);
  const resultsRef = useRef<HTMLDivElement>(null);
  const handleStart = () => {
    Object.values(CAREERS).forEach(c => {
      const img = new Image();
      img.src = c.image;
      img.onload = () => setLoadedImages(prev => new Set(prev).add(c.image));
    });
    setScreen("quiz");
  };
  const handleAnswer = (yes: boolean) => {
    if (yes) {
      const q = QUESTIONS[currentQuestionIndex];
      setScores(prev => {
        const next = { ...prev };
        for (const key of Object.keys(next) as (keyof Scores)[]) {
          next[key] = prev[key] + (q.weights[key] ?? 0);
        }
        return next;
      });
    }
    if (currentQuestionIndex < QUESTIONS.length - 1) {
      setCurrentQuestionIndex(prev => prev + 1);
    } else {
      setScreen("results");
    }
  };
  const handleRetake = () => {
    setScores(emptyScores());
    setCurrentQuestionIndex(0);
    setScreen("welcome");
  };
  const handleDownload = async () => {
    if (!resultsRef.current) return;
    setDownloading(true);
    try {
      const html2canvas = (await import("html2canvas")).default;
      const jsPDF = (await import("jspdf")).default;
      const canvas = await html2canvas(resultsRef.current, {
        scale: 2,
        backgroundColor: "#0a0f1e",
        useCORS: true,
        allowTaint: true,
        logging: false,
      });
      const imgData = canvas.toDataURL("image/jpeg", 0.92);
      const pdf = new jsPDF({ orientation: "portrait", unit: "px", format: "a4" });
      const pageW = pdf.internal.pageSize.getWidth();
      const pageH = pdf.internal.pageSize.getHeight();
      const ratio = canvas.width / canvas.height;
      const imgW = pageW;
      const imgH = imgW / ratio;
      let y = 0;
      while (y < imgH) {
        if (y > 0) pdf.addPage();
        pdf.addImage(imgData, "JPEG", 0, -y, imgW, imgH);
        y += pageH;
      }
      const name = winners.map(w => CAREERS[w].title).join("_").replace(/\s+/g, "_");
      pdf.save(`Career_Result_${name}.pdf`);
    } finally {
      setDownloading(false);
    }
  };
  const sorted = Object.entries(scores).sort((a, b) => b[1] - a[1]);
  const topScore = sorted[0]?.[1] ?? 0;
  const winners = sorted.filter(([, s]) => s === topScore).map(([k]) => k as keyof Scores);
  const isTie = winners.length > 1;
  const currentQuestion = QUESTIONS[currentQuestionIndex];
  const progress = (currentQuestionIndex / QUESTIONS.length) * 100;
  return (
    <div className="min-h-screen bg-background text-foreground flex items-center justify-center p-4 selection:bg-primary selection:text-primary-foreground overflow-hidden relative">
      <div className="absolute top-[-10%] left-[-10%] w-[40%] h-[40%] bg-primary/10 rounded-full blur-[120px] pointer-events-none" />
      <div className="absolute bottom-[-10%] right-[-10%] w-[40%] h-[40%] bg-primary/5 rounded-full blur-[120px] pointer-events-none" />
      <div className="w-full max-w-xl z-10">
        <AnimatePresence mode="wait">
          {screen === "welcome" && (
            <motion.div
              key="welcome"
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -20 }}
              transition={{ duration: 0.5, ease: [0.22, 1, 0.36, 1] }}
              className="flex flex-col items-center text-center space-y-8"
            >
              <div className="inline-flex items-center justify-center p-3 bg-primary/10 rounded-2xl mb-4 border border-primary/20">
                <BrainCircuit className="w-10 h-10 text-primary" />
              </div>
              <div className="space-y-4">
                <h1 className="text-4xl sm:text-5xl font-bold tracking-tight">
                  Career <span className="text-primary block sm:inline mt-2 sm:mt-0">Recommendation</span>
                </h1>
                <p className="text-lg text-muted-foreground max-w-md mx-auto leading-relaxed">
                  Discover your ideal path across tech, science, services, and civil roles. Nineteen questions to reveal your true calling.
                </p>
              </div>
              <Button
                onClick={handleStart}
                size="lg"
                className="rounded-full px-8 py-6 text-lg font-medium group hover:scale-105 transition-transform"
                data-testid="button-start-quiz"
              >
                Start Quiz
                <ChevronRight className="ml-2 w-5 h-5 group-hover:translate-x-1 transition-transform" />
              </Button>
            </motion.div>
          )}
          {screen === "quiz" && (
            <motion.div
              key="quiz"
              initial={{ opacity: 0, x: 20 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: -20 }}
              transition={{ duration: 0.4, ease: [0.22, 1, 0.36, 1] }}
              className="w-full"
            >
              <div className="mb-12 space-y-4">
                <div className="flex justify-between items-center text-sm font-medium text-muted-foreground">
                  <span className="uppercase tracking-widest text-xs">Question {currentQuestionIndex + 1} of {QUESTIONS.length}</span>
                  <span className="text-primary">{Math.round(progress)}%</span>
                </div>
                <Progress value={progress} className="h-2 bg-muted/50">
                  <div className="h-full bg-primary transition-all duration-500 ease-out" style={{ width: `${progress}%` }} />
                </Progress>
              </div>
              <AnimatePresence mode="wait">
                <motion.div
                  key={currentQuestionIndex}
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                  exit={{ opacity: 0, y: -10 }}
                  transition={{ duration: 0.3 }}
                  className="min-h-[200px] flex flex-col justify-center mb-12"
                >
                  <h2 className="text-3xl sm:text-4xl font-semibold leading-tight text-center">
                    {currentQuestion.text}
                  </h2>
                </motion.div>
              </AnimatePresence>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <Button
                  variant="outline"
                  size="lg"
                  className="py-8 text-xl font-medium border-2 hover:border-primary/50 hover:bg-primary/5 hover:text-primary transition-all"
                  onClick={() => handleAnswer(false)}
                  data-testid="button-answer-no"
                >
                  No
                </Button>
                <Button
                  size="lg"
                  className="py-8 text-xl font-medium border-2 border-primary bg-primary text-primary-foreground hover:bg-primary/90 transition-all shadow-[0_0_20px_rgba(0,255,255,0.2)] hover:shadow-[0_0_30px_rgba(0,255,255,0.4)]"
                  onClick={() => handleAnswer(true)}
                  data-testid="button-answer-yes"
                >
                  Yes
                </Button>
              </div>
            </motion.div>
          )}
          {screen === "results" && (
            <motion.div
              key="results"
              initial={{ opacity: 0, scale: 0.95 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ duration: 0.6, ease: [0.22, 1, 0.36, 1], delay: 0.1 }}
              className="w-full space-y-8"
            >
              <div ref={resultsRef} className="space-y-8">
                <div className="text-center space-y-4 mb-10">
                  <motion.div
                    initial={{ scale: 0 }} animate={{ scale: 1 }} transition={{ delay: 0.4, type: "spring", bounce: 0.5 }}
                    className="flex justify-center gap-3 mb-4"
                  >
                    {winners.map(w => (
                      <div key={w} className="inline-flex items-center justify-center p-4 bg-primary/10 rounded-3xl border border-primary/30 shadow-[0_0_40px_rgba(0,255,255,0.15)]">
                        {React.createElement(CAREERS[w].icon, { className: "w-10 h-10 text-primary" })}
                      </div>
                    ))}
                  </motion.div>
                  <motion.h2
                    initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.5 }}
                    className="text-muted-foreground uppercase tracking-widest font-semibold text-sm"
                  >
                    {isTie ? "Your Recommended Careers" : "Your Recommended Career"}
                  </motion.h2>
                  <motion.h1
                    initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.6 }}
                    className="text-3xl sm:text-4xl font-bold text-primary leading-tight"
                  >
                    {winners.map(w => CAREERS[w].title).join(" & ")}
                  </motion.h1>
                  {isTie && (
                    <motion.p
                      initial={{ opacity: 0, y: 6 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.65 }}
                      className="text-sm text-muted-foreground/70 italic"
                    >
                      You scored equally — either path suits you well.
                    </motion.p>
                  )}
                  {winners.map((w, i) => (
                    <motion.p
                      key={w}
                      initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.7 + i * 0.1 }}
                      className="text-base text-muted-foreground/90 max-w-md mx-auto pt-1"
                    >
                      {isTie && <span className="font-semibold text-foreground">{CAREERS[w].title}: </span>}
                      {CAREERS[w].desc}
                    </motion.p>
                  ))}
                </div>
                <motion.div
                  initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.75 }}
                  className={`grid gap-3 ${winners.length > 1 ? "grid-cols-2" : "grid-cols-1"}`}
                >
                  {winners.map(w => {
                    const isLoaded = loadedImages.has(CAREERS[w].image);
                    return (
                      <div key={w} className="relative overflow-hidden rounded-2xl border border-border/40 aspect-video bg-muted/20">
                        {!isLoaded && (
                          <div className="absolute inset-0 animate-pulse bg-gradient-to-r from-muted/40 via-muted/60 to-muted/40" style={{ animation: "shimmer 1.4s infinite linear", backgroundSize: "200% 100%" }} />
                        )}
                        <img
                          src={CAREERS[w].image}
                          alt={CAREERS[w].title}
                          className={`w-full h-full object-cover transition-opacity duration-500 ${isLoaded ? "opacity-100" : "opacity-0"}`}
                          onLoad={() => setLoadedImages(prev => new Set(prev).add(CAREERS[w].image))}
                          onError={e => { (e.target as HTMLImageElement).parentElement!.style.display = "none"; }}
                        />
                        <div className="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent" />
                        <span className="absolute bottom-2 left-3 text-xs font-semibold text-white/90 tracking-wide">
                          {CAREERS[w].title}
                        </span>
                      </div>
                    );
                  })}
                </motion.div>
                <motion.div
                  initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.8 }}
                  className="bg-card border border-border/50 rounded-2xl p-6 sm:p-8"
                >
                  <h3 className="font-semibold text-sm uppercase tracking-wider text-muted-foreground mb-5">Score Breakdown</h3>
                  <div className="space-y-4">
                    {Object.entries(scores).sort((a, b) => b[1] - a[1]).map(([key, score], index) => {
                      const career = CAREERS[key as keyof Scores];
                      const maxScore = Math.max(...Object.values(scores), 1);
                      const percentage = (score / maxScore) * 100;
                      const isWinner = winners.includes(key as keyof Scores);
                      return (
                        <div key={key} className="space-y-1.5">
                          <div className="flex justify-between items-center text-sm">
                            <span className={`font-medium flex items-center gap-2 ${isWinner ? "text-primary" : ""}`}>
                              {React.createElement(career.icon, { className: `w-4 h-4 ${isWinner ? "text-primary" : "text-muted-foreground"}` })}
                              {career.title}
                              {isWinner && isTie && <span className="text-xs bg-primary/15 text-primary px-1.5 py-0.5 rounded-full">Tied</span>}
                              {isWinner && !isTie && index === 0 && <span className="text-xs bg-primary/15 text-primary px-1.5 py-0.5 rounded-full">Top</span>}
                            </span>
                            <span className="text-muted-foreground">{score} pts</span>
                          </div>
                          <div className="h-1.5 w-full bg-muted/30 rounded-full overflow-hidden">
                            <motion.div
                              initial={{ width: 0 }}
                              animate={{ width: `${percentage}%` }}
                              transition={{ delay: 1 + index * 0.05, duration: 0.7, ease: "easeOut" }}
                              className={`h-full rounded-full ${isWinner ? "bg-primary shadow-[0_0_10px_rgba(0,255,255,0.5)]" : "bg-muted-foreground/40"}`}
                            />
                          </div>
                        </div>
                      );
                    })}
                  </div>
                </motion.div>
                <motion.div
                  initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 1.4 }}
                  className="bg-card border border-border/50 rounded-2xl p-6 sm:p-8"
                >
                  <h3 className="font-semibold text-sm uppercase tracking-wider text-muted-foreground mb-5 flex items-center gap-2">
                    <BookOpen className="w-4 h-4" />
                    What to Study
                  </h3>
                  <div className="space-y-6">
                    {winners.map(w => (
                      <div key={w}>
                        {isTie && (
                          <p className="text-sm font-semibold text-primary mb-2">{CAREERS[w].title}</p>
                        )}
                        <ul className="space-y-2">
                          {CAREERS[w].study.map((tip, i) => (
                            <li key={i} className="flex items-start gap-3 text-sm text-muted-foreground">
                              <span className="mt-1.5 w-1.5 h-1.5 rounded-full bg-primary flex-shrink-0" />
                              {tip}
                            </li>
                          ))}
                        </ul>
                      </div>
                    ))}
                  </div>
                </motion.div>
              </div>
              <motion.div
                initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: 2 }}
                className="flex justify-center gap-3 pt-4 flex-wrap"
              >
                <Button
                  onClick={handleDownload}
                  disabled={downloading}
                  className="rounded-full px-6 py-6 bg-primary text-primary-foreground hover:bg-primary/90 gap-2"
                >
                  {downloading
                    ? <><span className="w-4 h-4 border-2 border-current border-t-transparent rounded-full animate-spin" />Generating…</>
                    : <><Download className="w-4 h-4" />Download PDF</>
                  }
                </Button>
                <Button
                  variant="ghost"
                  onClick={handleRetake}
                  className="rounded-full px-6 py-6 group hover:bg-white/5 border border-transparent hover:border-white/10"
                  data-testid="button-retake"
                >
                  <RefreshCcw className="mr-2 w-4 h-4 group-hover:-rotate-180 transition-transform duration-500" />
                  Retake Quiz
                </Button>
              </motion.div>
            </motion.div>
          )}
        </AnimatePresence>
      </div>
    </div>
  );
}

And the index.css:

@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap');
@import "tailwindcss";
@import "tw-animate-css";
@plugin "@tailwindcss/typography";
@custom-variant dark (&:is(.dark *));
@theme inline {
  --color-background: hsl(var(--background));
  --color-foreground: hsl(var(--foreground));
  --color-primary: hsl(var(--primary));
  --color-primary-foreground: hsl(var(--primary-foreground));
  --color-muted: hsl(var(--muted));
  --color-muted-foreground: hsl(var(--muted-foreground));
  --color-card: hsl(var(--card));
  --color-card-foreground: hsl(var(--card-foreground));
  --color-border: hsl(var(--border));
  --color-accent: hsl(var(--accent));
  --color-accent-foreground: hsl(var(--accent-foreground));
  --font-sans: 'Space Grotesk', sans-serif;
  --background: 220 30% 5%;
  --foreground: 210 40% 95%;
  --primary: 190 100% 50%;
  --primary-foreground: 220 30% 5%;
  --muted: 220 20% 12%;
  --muted-foreground: 210 20% 55%;
  --card: 220 25% 8%;
  --card-foreground: 210 40% 95%;
  --border: 220 20% 15%;
  --accent: 190 90% 50%;
  --accent-foreground: 190 90% 50%;
  --radius: 0.5rem;
}
@layer base {
  * {
    @apply border-border;
  }
  body {
    @apply font-sans antialiased bg-background text-foreground;
  }
}
@keyframes shimmer {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}
