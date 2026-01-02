<script setup>

</script>

<template>
    <footer class="footer">
        <p><span class="arrow">></span> Built with passion & late nights</p>
    </footer>
</template>

<style scoped>
.footer {
    background: linear-gradient(135deg, #0f0f0f 0%, #1a1a1a 100%);
    border-top: 2px solid #333;
    padding: 2rem 3rem;
    text-align: center;
    font-family: 'Courier New', Courier, Monaco, monospace;
}

.footer p {
    color: #9ca3af;
    font-size: 0.95rem;
    margin: 0;
    letter-spacing: 0.5px;
}

.footer .arrow {
    color: #00ff00;
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
