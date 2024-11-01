// Function to render the language selection area dynamically
function renderLanguageSelection() {
    document.getElementById('language-selection-container').innerHTML = `
        <div class="container">
            <div class="row my-5">
                <h2 class="header-text">Welcome Test User! Pick a language to start learning!</h2>
            </div>
            <div class="row mb-5">
                <div class="col">
                    <button onclick="selectLanguage('Turkish')" class="btn btn-style" style="width: 150px; height:90px;">
                        <img src="../static/assets/turkey.png" alt="Turkish Flag" width="20" style="margin-right: 8px;">
                        <span>Turkish</span>
                    </button>
                </div>
                <div class="col">
                    <button onclick="selectLanguage('German')" class="btn btn-style" style="width: 150px; height:90px;">
                        <img src="https://cdn-icons-png.flaticon.com/512/197/197571.png" alt="German Flag" width="20" style="margin-right: 8px;">
                        <span>German</span>
                    </button>
                </div>
                <div class="col">
                    <button onclick="selectLanguage('French')" class="btn btn-style" style="width: 150px; height:90px;">
                        <img src="https://cdn-icons-png.flaticon.com/512/197/197560.png" alt="French Flag" width="20" style="margin-right: 8px;">
                        <span>French</span>
                    </button>
                </div>
                <div class="col">
                    <button onclick="selectLanguage('Italian')" class="btn btn-style" style="width: 150px; height:90px;">
                        <img src="https://cdn-icons-png.flaticon.com/512/197/197626.png" alt="Italian Flag" width="20" style="margin-right: 8px;">
                        <span>Italian</span>
                    </button>
                </div>
            </div>

            <div class="row">
                <div class="col">
                    <button onclick="selectLanguage('Spanish')" class="btn btn-style" style="width: 150px; height:90px;">
                        <img src="https://cdn-icons-png.flaticon.com/512/197/197593.png" alt="Spanish Flag" width="20" style="margin-right: 8px;">
                        <span>Spanish</span>
                    </button>
                </div>
                <div class="col">
                    <button onclick="selectLanguage('Arabic')" class="btn btn-style" style="width: 150px; height:90px;">
                        <img src="../static/assets/united-arab-emirates.png" alt="Arabic Flag" width="20" style="margin-right: 8px;">
                        <span>Arabic</span>
                    </button>
                </div>
                <div class="col">
                    <button onclick="selectLanguage('Japanese')" class="btn btn-style" style="width: 150px; height:90px;">
                        <img src="https://cdn-icons-png.flaticon.com/512/197/197604.png" alt="Japanese Flag" width="20" style="margin-right: 8px;">
                        <span>Japanese</span>
                    </button>
                </div>
                <div class="col">
                    <button onclick="selectLanguage('Russian')" class="btn btn-style" style="width: 150px; height:90px;">
                        <img src="https://cdn-icons-png.flaticon.com/512/197/197408.png" alt="Russian Flag" width="20" style="margin-right: 8px;">
                        <span>Russian</span>
                    </button>
                </div>
            </div>
            <p id="selected-language" style="font-weight: bold; margin-top: 20px;"></p>
        </div>
    `;
}

function renderLanguageExam(language) {
    const examContainer = document.getElementById('language-exam-container');
    if (examContainer) {
        examContainer.innerHTML = `
            <div id="language-exam">
                <div class="container">
                    <div class="row my-5">
                        <h2 class="header-text">
                        Let's see your knowledge in ${language}!
                        We have 20 questions to assess a level for your learning path.
                        Are you ready?</h2>
                    </div>
                    <div class="row my-5">
                        <div class="col">
                            <button onclick="startExam()" class="btn btn-style" style="width: 200px; height: 100px;"><span>Take the exam</span></button>
                        </div>
                        <div class="col">
                            <button onclick="loadCategories()" class="btn btn-style" style="width: 200px; height:100px;"><span>I already know my level</span></button>
                        </div>
                    </div>
                </div>
            </div>
        `;
    } else {
        console.error('Container with id "language-exam-container" not found');
    }
}

// Call renderLanguageExam with the selected language and hide the language-selection-container
function selectLanguage(language) {
    document.getElementById('language-selection-container').style.display = 'none'; // Hide the language selection
    renderLanguageExam(language); // Render exam 
    console.log(`Language selected: ${language}`);
}

// Render the language selection area
document.addEventListener("DOMContentLoaded", () => {
    renderLanguageSelection();
});
