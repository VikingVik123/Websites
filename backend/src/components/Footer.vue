<script setup>

</script>

<template>
    <footer class="footer">
        <p><span class="arrow">></span> Built with passion & late nights</p>
    </footer>
</template>

<style scoped>
.footer {
    background: linear-gradient(135deg, var(--bg-gradient-start) 0%, var(--bg-gradient-end) 100%);
    border-top: 2px solid var(--border-primary);
    padding: 2rem 3rem;
    text-align: center;
    font-family: 'Courier New', Courier, Monaco, monospace;
}

.footer p {
    color: var(--text-tertiary);
    font-size: 0.95rem;
    margin: 0;
    letter-spacing: 0.5px;
}

.footer .arrow {
    color: var(--accent-green);
    margin-right: 0.5rem;
}

/* Responsive Design */
@media (max-width: 768px) {
    .footer {
        padding: 1.5rem;
    }

    .footer p {
        font-size: 0.9rem;
    }
}

@media (max-width: 480px) {
    .footer {
        padding: 1rem;
    }

    .footer p {
        font-size: 0.85rem;
    }
}
</style>
