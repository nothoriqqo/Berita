import 'package:flutter/material.dart';

void main() {
  runApp(
    MaterialApp(
      title: 'Belajar Flutter',
      home: ,
    )
  );
}

class HomePage extends StatefulWidget {
  const HomePage ({Key? key}) : super(key: key);

  @override
  Widget build(Object context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Home Page'),
      ),
      body: Img.network('https://flutter.github.io/assets-for-api-docs/assets/widgets/owl.jpg');
      body: const Center(
        child: Text('Hello World'),
      ),
    );
  }
}
    return Scaffold(
      appBar: AppBar(
        title: const Text('Example Row'),
      ),
      body: Row(
        color: Colors.amber,
        height:300,
        width: double.infinity,
        child: row (
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          crossAxisAlignment: crossAxisAlignment.end,
        children: const [
          Icon.(
            Icons.train,
          size: 54,
          );
          Icon(
            Icons.airplanemode.activate,
            sizw: 54,
          ),
          Icon(
            Icons.car_repair,
            size: 54,
          ),
        ],
      ),
    ),
  );



  class MyHomePage extends StatefulWidget {
    const MyHomePage({super.key, required this.title});
  
  
    final String title;
  
    @override
    State<MyHomePage> createState() => _MyHomePageState();
  }
  
  class _MyHomePageState extends State<MyHomePage> {
    int _counter = 0;
  
    void _incrementCounter() {
      setState(() {
        _counter++;
      });
    }
  
    @override
    Widget build(BuildContext context) {
      return Scaffold(
        appBar: AppBar(
          title: Text(widget.title),
        ),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              const Text(
                'You have pushed the button this many times:',
              ),
              Text(
                '$_counter',
                style: Theme.of(context).textTheme.headline4,
              ),
            ],
          ),
        ),
        floatingActionButton: FloatingActionButton(
          onPressed: _incrementCounter,
          tooltip: 'Increment',
          child: const Icon(Icons.add),
        ), 
      );
    }
  }
  