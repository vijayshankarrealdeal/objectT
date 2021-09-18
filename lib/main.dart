import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:pipecount/cmr/cam.dart';
import 'package:provider/provider.dart';

void main() {
  runApp(
    ChangeNotifierProvider(
      create: (context) => CmKK(),
      child: MyApp(),
    ),
  );
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final cm = Provider.of<CmKK>(context);
    return Scaffold(
      appBar: AppBar(
        title: Text("Test"),
      ),
      body: Container(
        height: 200,
        child: cm.lo
            ? Center(
                child: CupertinoButton(
                  color: Colors.blueAccent,
                  child: Text('Hello'),
                  onPressed: () => cm.optionsDialogBox(context),
                ),
              )
            : Stack(
                children: [
                  Container(
                    height: 100,
                    child: Image.file(cm.file),
                    color: Colors.blue.withOpacity(0.2),
                  ),
                  Container(
                    height: 100,
                    child: Image.file(cm.file),
                  ),
                ],
              ),
      ),
    );
  }
}
