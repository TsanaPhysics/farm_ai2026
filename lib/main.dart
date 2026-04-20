import 'dart:io';
import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:camera/camera.dart';
import 'package:http/http.dart' as http;
import 'package:image/image.dart' as img;
import 'package:path_provider/path_provider.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  final cameras = await availableCameras();
  runApp(MaterialApp(
    theme: ThemeData.dark(),
    debugShowCheckedModeBanner: false,
    home: SoilAiApp(camera: cameras.first),
  ));
}

class SoilAiApp extends StatefulWidget {
  final CameraDescription camera;
  const SoilAiApp({Key? key, required this.camera}) : super(key: key);

  @override
  _SoilAiAppState createState() => _SoilAiAppState();
}

class _SoilAiAppState extends State<SoilAiApp> {
  late CameraController _controller;
  late Future<void> _initializeControllerFuture;
  Offset _roiOffset = Offset(0.5, 0.5);
  bool _isLoading = false;
  Map<String, dynamic>? _result;

  @override
  void initState() {
    super.initState();
    _controller = CameraController(widget.camera, ResolutionPreset.high);
    _initializeControllerFuture = _controller.initialize();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  Future<void> _analyzeSoil() async {
    setState(() => _isLoading = true);
    try {
      final image = await _controller.takePicture();
      final bytes = await File(image.path).readAsBytes();
      img.Image? originalImage = img.decodeImage(bytes);
      
      if (originalImage != null) {
        int roiSize = (originalImage.width * 0.3).toInt();
        int x = (originalImage.width * _roiOffset.dx - roiSize / 2).toInt();
        int y = (originalImage.height * _roiOffset.dy - roiSize / 2).toInt();
        img.Image cropped = img.copyCrop(originalImage, x: x, y: y, width: roiSize, height: roiSize);
        
        final tempDir = await getTemporaryDirectory();
        final roiFile = File('${tempDir.path}/roi_capture.jpg')..writeAsBytesSync(img.encodeJpg(cropped));

        var request = http.MultipartRequest('POST', Uri.parse('https://tsanaphysics.github.io/farm_ai2026/api/analyze_soil.php'));
        request.files.add(await http.MultipartRequest.fromPath('image', roiFile.path));
        var response = await request.send();
        var responseData = await response.stream.bytesToString();
        setState(() => _result = json.decode(responseData));
      }
    } catch (e) {
      print("Error: $e");
    } finally {
      setState(() => _isLoading = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Color(0xFF0B0E14),
      appBar: AppBar(title: Text("xAI Soil Monitor", style: TextStyle(color: Colors.cyanAccent))),
      body: Column(
        children: [
          Expanded(
            child: Stack(
              children: [
                FutureBuilder<void>(
                  future: _initializeControllerFuture,
                  builder: (context, snapshot) {
                    if (snapshot.connectionState == ConnectionState.done) {
                      return CameraPreview(_controller);
                    } else {
                      return Center(child: CircularProgressIndicator());
                    }
                  },
                ),
                Positioned(
                  left: MediaQuery.of(context).size.width * _roiOffset.dx - 50,
                  top: MediaQuery.of(context).size.height * 0.4 * _roiOffset.dy - 50,
                  child: Container(width: 100, height: 100, decoration: BoxDecoration(border: Border.all(color: Colors.cyanAccent, width: 2))),
                ),
              ],
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(20.0),
            child: ElevatedButton(
              onPressed: _isLoading ? null : _analyzeSoil,
              child: _isLoading ? CircularProgressIndicator() : Text("SCAN SOIL"),
            ),
          )
        ],
      ),
    );
  }
}
