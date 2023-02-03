**Data Binding modes**

![Data Binding Demo Demo](./databinding.png)

|Name| Description|
|---|---|
|OneWay| The target property is updated when the source property changes.|
|TwoWay| The target property is updated when the source property changes, and the source property is updated when the target property changes.|
|OneTime| The target property is set initially based on the source property value. However, changes are ignored from that point onward (unless the binding is set to a completely different object or you call BindingExpression.UpdateTarget()). Usually, you’ll use this mode to reduce overhead if you know the source property won’t change.|
|OneWayToSource| Similar to OneWay but in reverse. The source property is updated when the target property changes (which might seem a little backward), but the target property is never updated.|
|Default| The type of binding depends on the target property. It’s either TwoWay (for usersettable properties, such as the TextBox.Text) or OneWay (for everything else). All bindings use this approach unless you specify otherwise.|
