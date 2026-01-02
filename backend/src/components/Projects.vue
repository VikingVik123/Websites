<script setup>
</script>

<template>
    <section class="projects" id="projects">
        <h2><span class="number">03.</span> Experience</h2>
        <div class="project-list">
            <!-- Project items will go here -->
            <a href="https://www.qview.ai/" target="_blank" rel="noopener noreferrer" class="project-item">
                <h3>Qview AI</h3>
                <p>QView is a cloud-backed video automation and streaming platform designed for secure, real-time and on-demand access to CCTV and RTSP camera feeds.</p>
                <div class="tech-tags">
                    <span class="tag">Python</span>
                    <span class="tag">FastAPI</span>
                    <span class="tag">Flask</span>
                    <span class="tag">FFmpeg</span>
                </div>
            </a>
            <a href="https://usemenucard.com/" target="_blank" rel="noopener noreferrer" class="project-item">
                <h3>MenuCard</h3>
                <p>MenuCard is a backend-centric restaurant management system that digitizes menus and automates inventory, order, and payment workflows</p>
                <div class="tech-tags">
                    <span class="tag">FastAPI</span>
                    <span class="tag">PostgreSQL</span>
                    <span class="tag">Redis</span>
                </div>
            </a>
        </div>
    </section>
</template>

<style scoped>
.projects {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 4rem 3rem;
}

.projects h2 {
    font-size: 2rem;
    font-weight: 700;
    color: #e2e8f0;
    margin-bottom: 3rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    letter-spacing: 0.5px;
}

.projects h2 .number {
    color: #00ff00;
    font-size: 1.5rem;
    font-weight: 600;
}

.project-list {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 2rem;
    max-width: 1200px;
}

.project-item {
    background: linear-gradient(135deg, #0f0f0f 0%, #1a1a1a 100%);
    border: 2px solid #333;
    padding: 2rem;
    border-radius: 8px;
    transition: all 0.3s ease;
    display: flex;
    flex-direction: column;
    gap: 1rem;
    text-decoration: none;
    cursor: pointer;
}

.project-item:hover {
    border-color: #00ff00;
    transform: translateY(-8px);
    box-shadow: 0 12px 32px rgba(0, 255, 0, 0.2);
}

.project-item h3 {
    font-size: 1.5rem;
    font-weight: 700;
    color: #ffffff;
    margin: 0;
    letter-spacing: 0.5px;
    transition: color 0.3s ease;
}

.project-item:hover h3 {
    color: #00ff00;
}

.project-item p {
    font-size: 1rem;
    color: #9ca3af;
    line-height: 1.7;
    margin: 0;
    flex: 1;
}

.tech-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-top: 0.5rem;
}

.tag {
    background-color: transparent;
    border: 1px solid #00ff00;
    color: #00ff00;
    padding: 0.4rem 0.8rem;
    border-radius: 4px;
    font-size: 0.8rem;
    font-weight: 600;
    letter-spacing: 0.3px;
    pointer-events: none;
    user-select: none;
}

/* Responsive Design */
@media (max-width: 768px) {
    .projects {
        padding: 3rem 1.5rem;
    }

    .projects h2 {
        font-size: 1.75rem;
    }

    .projects h2 .number {
        font-size: 1.25rem;
    }

    .project-list {
        grid-template-columns: 1fr;
        gap: 1.5rem;
    }

    .project-item {
        padding: 1.75rem;
    }

    .project-item:active {
        transform: scale(0.98);
        border-color: #10b981;
    }
}

@media (max-width: 480px) {
    .projects {
        padding: 2rem 1rem;
    }

    .projects h2 {
        font-size: 1.5rem;
    }

    .projects h2 .number {
        font-size: 1.1rem;
    }

    .project-item {
        padding: 1.5rem;
    }

    .project-item h3 {
        font-size: 1.2rem;
    }

    .project-item p {
        font-size: 0.95rem;
        line-height: 1.6;
    }

    .tech-tags {
        gap: 0.4rem;
    }

    .tag {
        padding: 0.35rem 0.7rem;
        font-size: 0.75rem;
    }

    .project-list {
        grid-template-columns: 1fr;
        min-width: unset;
    }
}
</style>

