<?php
$target_dir = __DIR__ . '/uploads/';
if (!file_exists($target_dir)) {
    mkdir($target_dir, 0777, true);
}
if (isset($_FILES['audio'])) {
    $fname = time() . '_' . basename($_FILES['audio']['name']);
    $target_file = $target_dir . $fname;
    if (move_uploaded_file($_FILES['audio']['tmp_name'], $target_file)) {
        echo json_encode(['status' => 'ok', 'file' => 'uploads/' . $fname]);
    } else {
        http_response_code(500);
        echo json_encode(['status' => 'error']);
    }
} else {
    http_response_code(400);
    echo json_encode(['status' => 'no file']);
}
?>
