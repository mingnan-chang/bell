<?php
$dir = __DIR__ . '/uploads/';
$files = [];
if (is_dir($dir)) {
    foreach (glob($dir . '*') as $file) {
        $files[] = 'uploads/' . basename($file);
    }
}
sort($files);
header('Content-Type: application/json');
echo json_encode($files);
?>
