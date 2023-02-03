**WPF Resources**

Resources are arbitrary .NET objects stored (and named) in an element’s `Resources` property, typically meant to be shared by multiple child elements. The `FrameworkElement` and `FrameworkContentElement` base classes both have a Resources property (of type `System.Windows.ResourceDictionary`), so most WPF classes you’ll encounter have such a property. These resources are often styles or data providers.

Resources have `x:key` attribute which should be unique and allows us to reference the resource from the other part of the application. (Similar to Dictionay)

Resources are of generally two types:
1. Static Resource: Resolved at compile time. Used with keyword `StaticResource`
2. Dynamic Resource: Resolved at run time. Used with keyword `DynamicResource`

Resources can be defined at following places:
1. Control (layout) Level:
```XML
<Grid.Resources>
    <ResourceDictionary>
        <SolidColorBrush x:Key="WhiteColorBrush" Color="White"/>
        <SolidColorBrush x:Key="GoldColorBrush" Color="Gold"/>
    </ResourceDictionary>
</Grid.Resources>
```
2. Window Level:
```XML
<Window.Resources>
    <ResourceDictionary>
        <SolidColorBrush x:Key="RedColorBrush" Color="Red"/>
        <SolidColorBrush x:Key="BlueColorBrush" Color="Blue"/>
    </ResourceDictionary>
</Window.Resources>
```
3. Application Levle: Inside `app.xaml`
```XML
<Application.Resources>
    <ResourceDictionary>
        <SolidColorBrush x:Key="GreenColorBrush" Color="Green"/>
        <SolidColorBrush x:Key="YellowColorBrush" Color="Yellow"/>
    </ResourceDictionary>
</Application.Resources>
```

