**What is the difference between WPF and Winforms? Why should we use WPF instead of WinForms**

**Ans:** Windows form is a legacy. WPF (Windows Presentation Framework) is a newer version. However, Winforms is still good and gets the job done.

Here are some benefits of WPF over WinForms:
1. WPF utilizes the video card via diretX which makes WPF UI better performance than WinForms
2. WPF supports media streaming such as audio, and video. 2D,3D animations.
3. WPF uses XAML for designing which gives a lot more flexibility to design. Even a designer who did not have knowledge of C# programming can easily work on XAML
4. XAML enables the use of Styles and themes which is somewhat similar to CSS. This gives a big boost in enriching the UI experience. 
5. Databinding is superior.
6. MVVM supports loose coupling and better unit test capabilities.

---

**What is XAML?**

XAML (pronounced as zammel) stands for eXtensible Application Markup Language. It is a variant of XML for describing the user interface. XAML is an essential part of WPF. All the windows/pages and all user controls consists a XAML file. `.xaml` file is responsible for all the UI where as `.xaml.cs` take care of the code behind.

Similar to XML, a XAML element syntax starts with `<` and ends with `/>`. Each element tag has a start tag and end tag for example, `<TextBox> </TextBox>` 

Each XAML document has a root element that works as a container and defines the basic properties and holds other child elements. Most common containers are as follows,
1. Windows
2. Page
3. UserControl
4. Application: This is used in App.xaml where we can setup and intailize the elements/resources requrired at the startup 
5. ResourceDirectory: Here we can keep common shared resources which can be used througout applications

**XAML Namespaces and attributes**

```XML
<Window x:Class="WPF_Layouts_Demo.MainWindow"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
```

See the above XAML snippet, as a part of the root element of each XAML are two or more attributes pre-fixed with `xmlns` and `xmlns:x`. The xmlns attribute indicates the default XAML namespace so the object elements in used in XAML can be specified without a prefix. Additionally, the x: prefix is used with more than just the namespace. Here are some common x:prefix syntaxes that are used in XAML.
- `x:Key`: Sets a unique key for each resource in a ResourceDictionary.
- `x:Class`: Class name provides code-behind for a XAML page.
- `x:Name`: Unique run-time object name for the instance that exists in run-time code after an object element is processed.
- `x:Static`: Enables a reference that returns a static value that is not otherwise a XAML-compatible property.
- `x:Type`: Constructs a Type reference based on a type name. 

---


* [**What is Dispatcher**](https://github.com/ashutosh-vaidya/Csharp-and-WPF-Interview-Prep/tree/main/dispatcher)
* [**WPF Layouts**](https://github.com/ashutosh-vaidya/Csharp-and-WPF-Interview-Prep/tree/main/WPF%20Layouts)
* [**Data Binding Modes**](https://github.com/ashutosh-vaidya/Csharp-and-WPF-Interview-Prep/tree/main/data%20binding)
* [**Routed Events**](https://github.com/ashutosh-vaidya/Csharp-and-WPF-Interview-Prep/tree/main/WPF%20Basics/routed%20events)




