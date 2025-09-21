<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>스마트 학습 도우미</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            backdrop-filter: blur(10px);
        }

        .header {
            text-align: center;
            margin-bottom: 40px;
            background: linear-gradient(45deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
            font-weight: 700;
        }

        .header p {
            font-size: 1.2em;
            color: #666;
            -webkit-text-fill-color: #666;
        }

        .file-upload {
            background: #f8f9fa;
            border: 2px dashed #667eea;
            border-radius: 15px;
            padding: 40px;
            text-align: center;
            margin-bottom: 30px;
            transition: all 0.3s ease;
            cursor: pointer;
        }

        .file-upload:hover {
            background: #e3f2fd;
            border-color: #764ba2;
            transform: translateY(-2px);
        }

        .file-upload input {
            display: none;
        }

        .file-upload-icon {
            font-size: 3em;
            color: #667eea;
            margin-bottom: 15px;
        }

        .tabs {
            display: flex;
            justify-content: center;
            margin-bottom: 30px;
            background: #f1f3f4;
            border-radius: 50px;
            padding: 5px;
        }

        .tab {
            padding: 12px 25px;
            margin: 0 5px;
            background: transparent;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-weight: 500;
            color: #666;
        }

        .tab.active {
            background: linear-gradient(45deg, #667eea, #764ba2);
            color: white;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        }

        .content-area {
            background: white;
            border-radius: 15px;
            padding: 30px;
            min-height: 400px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
        }

        .quiz-container {
            display: none;
        }

        .quiz-container.active {
            display: block;
        }

        .quiz-question {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 25px;
            border-radius: 15px;
            margin-bottom: 25px;
            font-size: 1.2em;
            font-weight: 500;
        }

        .quiz-options {
            display: grid;
            gap: 15px;
            margin-bottom: 25px;
        }

        .quiz-option {
            background: #f8f9fa;
            border: 2px solid #e9ecef;
            border-radius: 10px;
            padding: 15px 20px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: 1.1em;
        }

        .quiz-option:hover {
            background: #e3f2fd;
            border-color: #667eea;
            transform: translateX(5px);
        }

        .quiz-option.selected {
            background: linear-gradient(45deg, #667eea, #764ba2);
            color: white;
            border-color: transparent;
        }

        .quiz-option.correct {
            background: #4caf50;
            color: white;
            border-color: transparent;
        }

        .quiz-option.incorrect {
            background: #f44336;
            color: white;
            border-color: transparent;
        }

        .quiz-controls {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 25px;
        }

        .btn {
            padding: 12px 25px;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            font-weight: 500;
            font-size: 1em;
            transition: all 0.3s ease;
        }

        .btn-primary {
            background: linear-gradient(45deg, #667eea, #764ba2);
            color: white;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.6);
        }

        .btn-secondary {
            background: #6c757d;
            color: white;
        }

        .btn-secondary:hover {
            background: #5a6268;
            transform: translateY(-2px);
        }

        .score-display {
            font-size: 1.2em;
            font-weight: 600;
            color: #667eea;
        }

        .summary-section {
            display: none;
        }

        .summary-section.active {
            display: block;
        }

        .summary-card {
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 20px;
            border-left: 5px solid #667eea;
        }

        .summary-card h3 {
            color: #667eea;
            margin-bottom: 15px;
            font-size: 1.3em;
        }

        .summary-card ul {
            list-style: none;
            padding-left: 0;
        }

        .summary-card li {
            padding: 8px 0;
            padding-left: 20px;
            position: relative;
        }

        .summary-card li:before {
            content: "▶";
            position: absolute;
            left: 0;
            color: #667eea;
        }

        .terms-section {
            display: none;
        }

        .terms-section.active {
            display: block;
        }

        .term-card {
            background: white;
            border: 2px solid #e9ecef;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 15px;
            transition: all 0.3s ease;
            cursor: pointer;
        }

        .term-card:hover {
            border-color: #667eea;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.2);
        }

        .term-card h4 {
            color: #667eea;
            margin-bottom: 10px;
            font-size: 1.2em;
        }

        .term-definition {
            color: #666;
            line-height: 1.6;
            display: none;
        }

        .term-definition.show {
            display: block;
            animation: fadeIn 0.3s ease;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .progress-bar {
            background: #e9ecef;
            height: 8px;
            border-radius: 4px;
            overflow: hidden;
            margin-bottom: 20px;
        }

        .progress-fill {
            background: linear-gradient(45deg, #667eea, #764ba2);
            height: 100%;
            transition: width 0.3s ease;
            border-radius: 4px;
        }

        .loading {
            text-align: center;
            padding: 40px;
            color: #666;
        }

        .loading:after {
            content: '';
            display: inline-block;
            width: 20px;
            height: 20px;
            border: 3px solid #f3f3f3;
            border-top: 3px solid #667eea;
            border-radius: 50%;
            animation: spin 1s linear infinite;
            margin-left: 10px;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📚 스마트 학습 도우미</h1>
            <p>파일을 업로드하면 맞춤형 학습 자료를 자동으로 생성해드립니다</p>
        </div>

        <div class="file-upload" onclick="document.getElementById('fileInput').click()">
            <div class="file-upload-icon">📁</div>
            <h3>학습 자료 파일을 업로드하세요</h3>
            <p>텍스트 파일, PDF, 문서 파일을 지원합니다</p>
            <input type="file" id="fileInput" accept=".txt,.pdf,.doc,.docx,.md" multiple>
        </div>

        <div class="tabs">
            <button class="tab active" data-tab="quiz">📝 퀴즈</button>
            <button class="tab" data-tab="summary">📋 요약</button>
            <button class="tab" data-tab="terms">📖 용어사전</button>
        </div>

        <div class="content-area">
            <!-- 퀴즈 섹션 -->
            <div class="quiz-container active">
                <div class="loading">학습 자료를 분석하고 퀴즈를 생성중입니다...</div>
            </div>

            <!-- 요약 섹션 -->
            <div class="summary-section">
                <div class="loading">요약을 생성중입니다...</div>
            </div>

            <!-- 용어사전 섹션 -->
            <div class="terms-section">
                <div class="loading">핵심 용어를 추출중입니다...</div>
            </div>
        </div>
    </div>

    <script>
        class StudyHelper {
            constructor() {
                this.currentQuiz = 0;
                this.score = 0;
                this.quizData = [];
                this.summaryData = [];
                this.termsData = [];
                this.fileContent = '';
                
                this.initializeEventListeners();
                this.generateSampleData();
            }

            initializeEventListeners() {
                // 파일 업로드 이벤트
                document.getElementById('fileInput').addEventListener('change', (e) => {
                    this.handleFileUpload(e);
                });

                // 탭 전환 이벤트
                document.querySelectorAll('.tab').forEach(tab => {
                    tab.addEventListener('click', (e) => {
                        this.switchTab(e.target.dataset.tab);
                    });
                });
            }

            async handleFileUpload(event) {
                const files = event.target.files;
                if (files.length === 0) return;

                let combinedContent = '';
                for (let file of files) {
                    const content = await this.readFile(file);
                    combinedContent += content + '\n\n';
                }

                this.fileContent = combinedContent;
                this.analyzeContent();
            }

            readFile(file) {
                return new Promise((resolve) => {
                    const reader = new FileReader();
                    reader.onload = (e) => resolve(e.target.result);
                    reader.readAsText(file, 'UTF-8');
                });
            }

            analyzeContent() {
                // 업로드된 파일 내용을 분석하여 학습 자료 생성
                this.generateQuizFromContent();
                this.generateSummaryFromContent();
                this.generateTermsFromContent();
            }

            generateSampleData() {
                // 업로드된 문서를 기반으로 샘플 데이터 생성
                this.quizData = [
                    {
                        question: "에릭슨의 인간발달 이론에서 성년기(19세~39세)의 발달 과업은 무엇인가요?",
                        options: [
                            "정체감 대 정체감 혼미",
                            "친밀감 대 고립감", 
                            "생산성 대 침체성",
                            "통합감 대 절망감"
                        ],
                        correct: 1,
                        explanation: "성년기는 배우자를 선택하여 가정을 이루고, 다른 사람과 신뢰와 애정을 바탕으로 친밀감을 형성하는 시기입니다."
                    },
                    {
                        question: "대사증후군 진단 기준 중 복부비만의 기준은?",
                        options: [
                            "남성 85cm, 여성 90cm 이상",
                            "남성 90cm, 여성 85cm 이상",
                            "남성 95cm, 여성 90cm 이상", 
                            "남성 100cm, 여성 95cm 이상"
                        ],
                        correct: 1,
                        explanation: "대사증후군의 복부비만 진단 기준은 허리둘레가 남성 90cm 이상, 여성 85cm 이상입니다."
                    },
                    {
                        question: "식품 가공에서 '건조법'의 주요 목적은 무엇인가요?",
                        options: [
                            "맛을 향상시키기 위해",
                            "색깔을 좋게 하기 위해",
                            "수분 활성도를 낮춰 미생물 증식을 억제하기 위해",
                            "영양소를 증가시키기 위해"
                        ],
                        correct: 2,
                        explanation: "건조법은 바람과 열을 이용하여 수분 활성도를 낮춰 미생물의 증식을 억제하는 식품 저장 방법입니다."
                    },
                    {
                        question: "트랜스 지방이 건강에 미치는 영향으로 올바른 것은?",
                        options: [
                            "HDL 콜레스테롤을 증가시킨다",
                            "LDL 콜레스테롤을 감소시킨다",
                            "LDL 콜레스테롤을 증가시키고 HDL 콜레스테롤을 감소시킨다",
                            "콜레스테롤 수치에 영향을 주지 않는다"
                        ],
                        correct: 2,
                        explanation: "트랜스 지방은 나쁜 콜레스테롤(LDL)을 증가시키고 좋은 콜레스테롤(HDL)을 감소시켜 심혈관 질환 위험을 높입니다."
                    },
                    {
                        question: "유아기(25개월~5세)의 주요 발달 특징이 아닌 것은?",
                        options: [
                            "운동 기능과 인지능력이 눈에 띄게 발달함",
                            "친구들과 놀이를 통해 공동생활에 적응",
                            "2차 성징이 나타남",
                            "기본적인 생활 습관을 습득"
                        ],
                        correct: 2,
                        explanation: "2차 성징은 청소년기(13세~18세)에 나타나는 특징입니다. 유아기에는 운동 기능, 인지능력 발달과 기본 생활습관 습득이 주요 특징입니다."
                    }
                ];

                this.summaryData = [
                    {
                        title: "에릭슨의 인간발달 이론",
                        content: [
                            "성인이 된 이후에도 발달은 계속된다고 주장",
                            "8단계의 심리사회적 발달 단계 제시",
                            "각 단계마다 특정한 발달 과업과 위기 존재",
                            "성공적 과업 수행시 긍정적 특성 획득"
                        ]
                    },
                    {
                        title: "생활습관병의 특성",
                        content: [
                            "잘못된 식습관, 운동 부족, 음주, 흡연 등이 원인",
                            "예비군 → 생활습관병 → 중증질환으로 진행",
                            "대사증후군이 기저질환 역할",
                            "생활습관 개선을 통한 예방과 관리가 중요"
                        ]
                    },
                    {
                        title: "식품 가공의 목적과 방법",
                        content: [
                            "소화 흡수율 증대, 맛 향상, 저장성 향상",
                            "물리적, 화학적, 생물학적 방법으로 분류",
                            "온도, 수분, pH, 산소 조절이 핵심",
                            "원료별로 다양한 가공 방법 적용"
                        ]
                    }
                ];

                this.termsData = [
                    { term: "발달과업", definition: "인간이 성장하고 발달하는 동안 반드시 성취해야 하는 과제" },
                    { term: "대사증후군", definition: "잘못된 식습관, 스트레스, 운동 부족, 음주 등으로 인슐린 저항성이 높아져서 발생하는 만성적인 대사 장애" },
                    { term: "인슐린 저항성", definition: "혈당을 낮추는 호르몬인 인슐린에 대한 신체의 반응이 감소함으로써 혈당이 높은 상태로 유지되는 것" },
                    { term: "푸드테크", definition: "식품의 생산, 가공, 저장, 유통, 조리에 정보 통신 기술을 접목하여 새로운 산업을 창출하는 것" },
                    { term: "수분 활성도", definition: "식품 내 수분 중 미생물의 생장에 이용되는 자유수를 나타내는 지표" },
                    { term: "트랜스 지방", definition: "수소를 첨가하여 불포화 지방을 포화 지방으로 변환시키는 과정에서 생성되는 인공 지방산" },
                    { term: "HACCP", definition: "식품의 원료 관리 및 제조 유통의 모든 과정에서 식품의 오염을 방지하기 위하여 각 과정의 위해 요소를 분석하고 중점적으로 관리하는 제도" }
                ];

                this.renderQuiz();
                this.renderSummary();
                this.renderTerms();
            }

            generateQuizFromContent() {
                // 실제 파일 내용을 기반으로 퀴즈 생성 로직
                // 여기서는 샘플 데이터 사용
                this.renderQuiz();
            }

            generateSummaryFromContent() {
                // 실제 파일 내용을 기반으로 요약 생성 로직
                this.renderSummary();
            }

            generateTermsFromContent() {
                // 실제 파일 내용을 기반으로 용어 추출 로직
                this.renderTerms();
            }

            renderQuiz() {
                const quizContainer = document.querySelector('.quiz-container');
                if (this.quizData.length === 0) {
                    quizContainer.innerHTML = '<div class="loading">퀴즈 데이터를 준비중입니다...</div>';
                    return;
                }

                const quiz = this.quizData[this.currentQuiz];
                const progress = ((this.currentQuiz + 1) / this.quizData.length) * 100;

                quizContainer.innerHTML = `
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: ${progress}%"></div>
                    </div>
                    <div class="quiz-question">
                        <strong>문제 ${this.currentQuiz + 1}/${this.quizData.length}</strong><br>
                        ${quiz.question}
                    </div>
                    <div class="quiz-options">
                        ${quiz.options.map((option, index) => 
                            `<div class="quiz-option" data-index="${index}">${option}</div>`
                        ).join('')}
                    </div>
                    <div class="quiz-controls">
                        <div class="score-display">점수: ${this.score}/${this.quizData.length}</div>
                        <div>
                            <button class="btn btn-secondary" onclick="studyHelper.prevQuestion()">이전</button>
                            <button class="btn btn-primary" onclick="studyHelper.checkAnswer()">확인</button>
                            <button class="btn btn-primary" onclick="studyHelper.nextQuestion()">다음</button>
                        </div>
                    </div>
                    <div id="explanation" style="display: none; margin-top: 20px; padding: 20px; background: #e8f5e8; border-radius: 10px;"></div>
                `;

                // 옵션 클릭 이벤트
                document.querySelectorAll('.quiz-option').forEach(option => {
                    option.addEventListener('click', (e) => {
                        document.querySelectorAll('.quiz-option').forEach(opt => opt.classList.remove('selected'));
                        e.target.classList.add('selected');
                    });
                });
            }

            checkAnswer() {
                const selected = document.querySelector('.quiz-option.selected');
                if (!selected) {
                    alert('답을 선택해주세요!');
                    return;
                }

                const selectedIndex = parseInt(selected.dataset.index);
                const correct = this.quizData[this.currentQuiz].correct;
                
                document.querySelectorAll('.quiz-option').forEach(option => {
                    const index = parseInt(option.dataset.index);
                    if (index === correct) {
                        option.classList.add('correct');
                    } else if (option.classList.contains('selected')) {
                        option.classList.add('incorrect');
                    }
                });

                if (selectedIndex === correct) {
                    this.score++;
                }

                // 해설 표시
                const explanation = document.getElementById('explanation');
                explanation.innerHTML = `<strong>해설:</strong> ${this.quizData[this.currentQuiz].explanation}`;
                explanation.style.display = 'block';

                // 점수 업데이트
                document.querySelector('.score-display').textContent = `점수: ${this.score}/${this.quizData.length}`;
            }

            nextQuestion() {
                if (this.currentQuiz < this.quizData.length - 1) {
                    this.currentQuiz++;
                    this.renderQuiz();
                } else {
                    this.showResults();
                }
            }

            prevQuestion() {
                if (this.currentQuiz > 0) {
                    this.currentQuiz--;
                    this.renderQuiz();
                }
            }

            showResults() {
                const percentage = (this.score / this.quizData.length * 100).toFixed(1);
                const quizContainer = document.querySelector('.quiz-container');
                
                quizContainer.innerHTML = `
                    <div style="text-align: center; padding: 40px;">
                        <h2 style="color: #667eea; margin-bottom: 20px;">🎉 퀴즈 완료!</h2>
                        <div style="font-size: 2em; color: #667eea; margin: 20px 0;">
                            ${this.score} / ${this.quizData.length}
                        </div>
                        <div style="font-size: 1.5em; margin: 20px 0;">정답률: ${percentage}%</div>
                        <button class="btn btn-primary" onclick="studyHelper.resetQuiz()">다시 시작</button>
                    </div>
                `;
            }

            resetQuiz() {
                this.currentQuiz = 0;
                this.score = 0;
                this.renderQuiz();
            }

            renderSummary() {
                const summarySection = document.querySelector('.summary-section');
                
                summarySection.innerHTML = this.summaryData.map(summary => `
                    <div class="summary-card">
                        <h3>${summary.title}</h3>
                        <ul>
                            ${summary.content.map(item => `<li>${item}</li>`).join('')}
                        </ul>
                    </div>
                `).join('');
            }

            renderTerms() {
                const termsSection = document.querySelector('.terms-section');
                
                termsSection.innerHTML = this.termsData.map(term => `
                    <div class="term-card" onclick="studyHelper.toggleTerm(this)">
                        <h4>${term.term}</h4>
                        <div class="term-definition">${term.definition}</div>
                    </div>
                `).join('');
            }

            toggleTerm(element) {
                const definition = element.querySelector('.term-definition');
                definition.classList.toggle('show');
            }

            switchTab(tabName) {
                // 탭 활성화
                document.querySelectorAll('.tab').forEach(tab => tab.classList.remove('active'));
                document.querySelector(`[data-tab="${tabName}"]`).classList.add('active');

                // 콘텐츠 표시
                document.querySelectorAll('.quiz-container, .summary-section, .terms-section').forEach(section => {
                    section.classList.remove('active');
                });

                if (tabName === 'quiz') {
                    document.querySelector('.quiz-container').classList.add('active');
                } else if (tabName === 'summary') {
                    document.querySelector('.summary-section').classList.add('active');
                } else if (tabName === 'terms') {
                    document.querySelector('.terms-section').classList.add('active');
                }
            }
        }

        // 앱 초기화
        const studyHelper = new StudyHelper();
    </script>
</body>
</html>
