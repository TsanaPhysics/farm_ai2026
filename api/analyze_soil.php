<?php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['image'])) {
    $uploadDir = 'data/raw/uploads/';
    $fileName = time() . '_' . basename($_FILES['image']['name']);
    $targetFilePath = $uploadDir . $fileName;

    if (move_uploaded_file($_FILES['image']['tmp_name'], $targetFilePath)) {
        // Execute Python Model
        $pythonPath = 'python3'; // ปรับเป็น path ของ python ในเครื่องจริง
        $scriptPath = 'src/models/cv_ph_analysis.py';
        $fullPath = realpath($targetFilePath);
        
        $command = "$pythonPath $scriptPath \"$fullPath\" 2>&1";
        $output = shell_exec($command);
        
        if ($output) {
            echo $output; // Python returns JSON
        } else {
            echo json_encode(["status" => "error", "message" => "AI Model failed to execute"]);
        }
    } else {
        echo json_encode(["status" => "error", "message" => "Failed to upload image"]);
    }
} else {
    echo json_encode(["status" => "error", "message" => "Invalid request"]);
}
?>
