/* Sidebar toggle controller and dynamic toast notification engine */

document.addEventListener('DOMContentLoaded', function() {
    // Sidebar Collapsing
    const sidebar = document.getElementById('sidebar');
    const sidebarToggle = document.getElementById('sidebar-toggle');
    const mobileToggle = document.getElementById('mobile-toggle');
    const sidebarOverlay = document.getElementById('sidebar-overlay');
    
    if (sidebarToggle && sidebar) {
        sidebarToggle.addEventListener('click', function() {
            sidebar.classList.toggle('collapsed');
            const isCollapsed = sidebar.classList.contains('collapsed');
            localStorage.setItem('sidebar-collapsed', isCollapsed);
        });
        
        // Restore state
        const wasCollapsed = localStorage.getItem('sidebar-collapsed') === 'true';
        if (wasCollapsed) {
            sidebar.classList.add('collapsed');
        }
    }
    
    // Mobile Drawer toggles
    if (mobileToggle && sidebar && sidebarOverlay) {
        function closeMobileSidebar() {
            sidebar.classList.remove('mobile-active');
            sidebarOverlay.classList.remove('active');
        }

        mobileToggle.addEventListener('click', function(e) {
            e.stopPropagation();
            sidebar.classList.add('mobile-active');
            sidebarOverlay.classList.add('active');
        });
        
        sidebarOverlay.addEventListener('click', closeMobileSidebar);

        // Close sidebar on link click on mobile
        sidebar.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', function() {
                if (window.innerWidth <= 992) {
                    closeMobileSidebar();
                }
            });
        });

        // Close on Escape key press
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') {
                closeMobileSidebar();
            }
        });
    }
    
    // Auto-hide messages from Django after 5 seconds
    const djangoToasts = document.querySelectorAll('.toast');
    djangoToasts.forEach(toast => {
        setTimeout(() => {
            toast.style.animation = 'slideIn 0.3s cubic-bezier(0.16, 1, 0.3, 1) reverse forwards';
            setTimeout(() => {
                toast.remove();
            }, 300);
        }, 5000);
    });

    // Dropdown Logic
    const dropdownTriggers = document.querySelectorAll('.dropdown-trigger');
    
    dropdownTriggers.forEach(trigger => {
        trigger.addEventListener('click', function(e) {
            e.stopPropagation();
            const container = this.closest('.dropdown-container');
            const menu = container.querySelector('.dropdown-menu');
            
            // Close other open dropdowns
            document.querySelectorAll('.dropdown-menu.active').forEach(openMenu => {
                if (openMenu !== menu) {
                    openMenu.classList.remove('active');
                }
            });
            
            // Toggle current dropdown
            if (menu) {
                menu.classList.toggle('active');
            }
        });
    });
    
    // Close dropdowns when clicking outside
    document.addEventListener('click', function(e) {
        if (!e.target.closest('.dropdown-container')) {
            document.querySelectorAll('.dropdown-menu.active').forEach(menu => {
                menu.classList.remove('active');
            });
        }
    });

    // Theme switching logic
    const themeToggle = document.getElementById('theme-toggle');
    const mobileThemeToggle = document.getElementById('mobile-theme-toggle');
    const publicThemeToggle = document.getElementById('public-theme-toggle');
    const themeToggleText = document.getElementById('theme-toggle-text');
    
    function setTheme(theme) {
        if (theme === 'light') {
            document.body.setAttribute('data-theme', 'light');
            localStorage.setItem('theme', 'light');
            updateThemeUI('light');
        } else {
            document.body.removeAttribute('data-theme');
            localStorage.setItem('theme', 'dark');
            updateThemeUI('dark');
        }
    }
    
    function updateThemeUI(theme) {
        const iconClass = theme === 'light' ? 'fa-sun' : 'fa-moon';
        const textVal = theme === 'light' ? 'Light Mode' : 'Dark Mode';
        
        [themeToggle, mobileThemeToggle, publicThemeToggle].forEach(btn => {
            if (btn) {
                const icon = btn.querySelector('i');
                if (icon) {
                    icon.className = `fas ${iconClass}`;
                }
            }
        });
        
        if (themeToggleText) {
            themeToggleText.innerText = textVal;
        }
    }
    
    // Read local storage and initialize
    const currentTheme = localStorage.getItem('theme') || 'dark';
    setTheme(currentTheme);
    
    // Add event listeners
    [themeToggle, mobileThemeToggle, publicThemeToggle].forEach(btn => {
        if (btn) {
            btn.addEventListener('click', function() {
                const isLight = document.body.getAttribute('data-theme') === 'light';
                setTheme(isLight ? 'dark' : 'light');
            });
        }
    });
});

// Global show toast helper function
function showToast(message, type = 'info') {
    const container = document.getElementById('toast-container');
    if (!container) return;
    
    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    
    let iconClass = 'info-circle';
    if (type === 'success') iconClass = 'check-circle';
    if (type === 'error') iconClass = 'times-circle';
    if (type === 'warning') iconClass = 'exclamation-circle';
    
    toast.innerHTML = `
        <i class="fas fa-${iconClass}"></i>
        <span>${message}</span>
    `;
    
    container.appendChild(toast);
    
    setTimeout(() => {
        toast.style.animation = 'slideIn 0.3s cubic-bezier(0.16, 1, 0.3, 1) reverse forwards';
        setTimeout(() => {
            toast.remove();
        }, 300);
    }, 5000);
}
