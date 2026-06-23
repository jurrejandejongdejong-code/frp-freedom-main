// This file contains your Data Connector logic
[Version = "1.0.0"]
section zep dog rodesian ridge back;

[DataSource.Kind="zep dog rodesian ridge back", Publish="zep dog rodesian ridge back.Publish"]
shared zep dog rodesian ridge back.Contents = (optional message as text) =>
    let
        _message = if (message <> null) then message else "(no message)",
        a = "Hello from zep dog rodesian ridge back: " & _message
    in
        a;

// Data Source Kind description
zep dog rodesian ridge back = [
    Authentication = [
        // Key = [],
        // UsernamePassword = [],
        // Windows = [],
        Anonymous = []
    ]
];

// Data Source UI publishing description
zep dog rodesian ridge back.Publish = [
    Beta = true,
    Category = "Other",
    ButtonText = { Extension.LoadString("ButtonTitle"), Extension.LoadString("ButtonHelp") },
    LearnMoreUrl = "https://powerbi.microsoft.com/",
    SourceImage = zep dog rodesian ridge back.Icons,
    SourceTypeImage = zep dog rodesian ridge back.Icons
];

zep dog rodesian ridge back.Icons = [
    Icon16 = { Extension.Contents("zep dog rodesian ridge back16.png"), Extension.Contents("zep dog rodesian ridge back20.png"), Extension.Contents("zep dog rodesian ridge back24.png"), Extension.Contents("zep dog rodesian ridge back32.png") },
    Icon32 = { Extension.Contents("zep dog rodesian ridge back32.png"), Extension.Contents("zep dog rodesian ridge back40.png"), Extension.Contents("zep dog rodesian ridge back48.png"), Extension.Contents("zep dog rodesian ridge back64.png") }
];
