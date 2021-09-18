import 'dart:convert';
import 'dart:io';

import 'package:http/http.dart' as http;
import 'package:flutter/cupertino.dart';

class EnPoint extends ChangeNotifier {
  final url = "http://10.0.2.2/upload";
  String me = '';

  Future<void> getCl(File file) async {
    final request = http.MultipartRequest("POST", Uri.parse(url));
    final headers = {"Content-type": "multipart/form-data"};
    request.files.add(http.MultipartFile(
        'img', file.readAsBytes().asStream(), file.lengthSync(),
        filename: file.path.split("/").last));
    request.headers.addAll(headers);

    final response = await request.send();
    final res = await http.Response.fromStream(response);
    final re = jsonDecode(res.body);
    me = re['message'];
    notifyListeners();
  }
}
