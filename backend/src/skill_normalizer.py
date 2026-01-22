SKILL_ALIASES = {
    "react": ["react", "reactjs", "react.js", "frontend", "front-end"],
    "javascript": ["javascript", "js", "ecmascript"],
    "html": ["html", "html5"],
    "css": ["css", "css3"],
    "typescript": ["typescript", "ts"],
    "angular": ["angular", "angularjs"],
    "vue": ["vue", "vue.js"],
    "git": ["git", "version control"],
    "docker": ["docker", "containerization"],
    "webpack": ["webpack"],
    "babel": ["babel"],
    "accessibility": ["wcag", "accessibility"],
}

def normalize_skill(token: str):
    token = token.lower()
    for canonical, aliases in SKILL_ALIASES.items():
        if token in aliases:
            return canonical
    return None
