import 'package:http/http.dart' as http;
import 'package:flutter/cupertino.dart';

class EnPoint extends ChangeNotifier {
  final url = "http://10.0.2.2/uplo";

  Future<void> getCl() async {
    final repone = await http.post(Uri.parse(url));
    
  }
}
