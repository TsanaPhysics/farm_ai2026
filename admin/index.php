<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Dashboard | Farm AI xAI 2026</title>
    <link rel="stylesheet" href="../css/dashboard.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body style="background: #05070a;">
    <aside class="sidebar">
        <div class="logo">
            <i class="fas fa-shield-halved" style="color: var(--accent);"></i>
            <span>Admin Control</span>
        </div>
        <nav class="nav-links">
            <div class="nav-item">
                <a href="../dashboard/" class="nav-link">
                    <i class="fas fa-arrow-left"></i>
                    <span>Back to App</span>
                </a>
            </div>
            <div class="nav-item">
                <a href="#" class="nav-link active">
                    <i class="fas fa-database"></i>
                    <span>Manage Datasets</span>
                </a>
            </div>
            <div class="nav-item">
                <a href="#" class="nav-link">
                    <i class="fas fa-microchip"></i>
                    <span>Model Settings</span>
                </a>
            </div>
            <div class="nav-item">
                <a href="#" class="nav-link">
                    <i class="fas fa-users-cog"></i>
                    <span>Access Control</span>
                </a>
            </div>
        </nav>
    </aside>

    <main class="main-content">
        <header class="header">
            <h1>System Management</h1>
            <div class="status-badge" style="background: rgba(240, 147, 251, 0.1); color: var(--accent);">
                <span class="status-dot" style="background: var(--accent);"></span> Administrator
            </div>
        </header>

        <section class="stats-grid">
            <div class="stat-card">
                <div class="stat-label">Server Load</div>
                <div class="stat-value">12.4%</div>
                <div style="height: 5px; background: rgba(255,255,255,0.1); border-radius: 10px; margin-top: 10px;">
                    <div style="width: 12%; height: 100%; background: var(--primary); border-radius: 10px;"></div>
                </div>
            </div>
            <div class="stat-card">
                <div class="stat-label">API Requests</div>
                <div class="stat-value">84,102</div>
                <div style="font-size: 0.8rem; color: #888;">Last 24 Hours</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Storage Usage</div>
                <div class="stat-value">62%</div>
                <div style="height: 5px; background: rgba(255,255,255,0.1); border-radius: 10px; margin-top: 10px;">
                    <div style="width: 62%; height: 100%; background: var(--accent); border-radius: 10px;"></div>
                </div>
            </div>
        </section>

        <section class="dashboard-grid" style="grid-template-columns: 1fr 1fr;">
            <div class="chart-container">
                <h3><i class="fas fa-mobile-alt"></i> Connect Smartphone</h3>
                <div style="margin-top: 1rem; text-align: center; padding: 20px; background: rgba(255,255,255,0.05); border-radius: 15px;">
                    <p style="font-size: 0.8rem; color: #888; margin-bottom: 15px;">Scan this QR code to open the <b>xAI Soil Monitor</b> on your mobile device.</p>
                    <div id="qrcode" style="display: inline-block; padding: 10px; background: white; border-radius: 10px;"></div>
                    <p style="margin-top: 15px; font-family: monospace; font-size: 0.8rem; color: var(--primary);" id="serverLink"></p>
                </div>
            </div>

            <div class="chart-container" style="background: black; border-color: #333;">

                <h3 style="color: var(--primary); font-family: 'Courier New', Courier, monospace;"><i class="fas fa-terminal"></i> System Logs</h3>
                <div id="logs" style="margin-top: 1rem; font-family: 'Courier New', Courier, monospace; font-size: 0.85rem; height: 300px; overflow-y: auto; color: #00ff00;">
                    <div>[2026-04-20 10:15:23] INFO: System Initialized.</div>
                    <div>[2026-04-20 10:16:45] SUCCESS: NASA POWER Data Fetcher completed.</div>
                    <div>[2026-04-20 10:20:12] INFO: AI Model 'Soil_RF_v2' loaded successfully.</div>
                    <div>[2026-04-20 11:02:44] WARNING: Disk usage exceeding 60%.</div>
                    <div id="liveLog"></div>
                </div>
            </div>
        </section>
    </main>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
    <script>
        // Generate QR Code for Mobile App Access
        const currentUrl = window.location.href.replace('admin/', 'app/');
        document.getElementById('serverLink').innerText = currentUrl;
        new QRCode(document.getElementById("qrcode"), {
            text: currentUrl,
            width: 150,
            height: 150,
            colorDark : "#000000",
            colorLight : "#ffffff",
            correctLevel : QRCode.CorrectLevel.H
        });

        // Simulate real-time logs
        const liveLog = document.getElementById('liveLog');
        const messages = [
            "INFO: Scanning Geospatial Node #412...",
            "SUCCESS: Node #412 Sync Complete.",
            "INFO: Executing Soil Classification Model...",
            "DEBUG: Feature 'pH' importance: 0.245",
            "INFO: Waiting for next data stream..."
        ];
        let i = 0;
        setInterval(() => {
            const div = document.createElement('div');
            div.innerText = `[${new Date().toLocaleTimeString()}] ${messages[i % messages.length]}`;
            liveLog.appendChild(div);
            i++;
            const logs = document.getElementById('logs');
            logs.scrollTop = logs.scrollHeight;
        }, 3000);
    </script>
</body>
</html>

