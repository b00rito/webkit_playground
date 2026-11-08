# WebKit IPC messages - WebKit-7621.2.5.11.8

Generated from every `*.messages.in` in `Source/WebKit` (code-generator test fixtures excluded). Messages marked (sync) are synchronous: the sender blocks until the reply arrives.

## `AcceleratedBackingStoreDMABuf` - WebContent -> UI

`UIProcess/dmabuf/AcceleratedBackingStoreDMABuf.messages.in` - non-Apple ports - direction: observed send sites

`DidCreateBuffer`, `DidCreateBufferSHM`, `DidDestroyBuffer`, `Frame`

## `AudioSessionRoutingArbitratorProxy` - WebContent -> UI

`UIProcess/Media/AudioSessionRoutingArbitratorProxy.messages.in` - direction: annotated

`BeginRoutingArbitrationWithCategory`, `EndRoutingArbitration`

## `DigitalCredentialsCoordinatorProxy` - WebContent -> UI

`UIProcess/DigitalCredentials/DigitalCredentialsCoordinatorProxy.messages.in` - direction: annotated

`RequestDigitalCredential`, `Cancel`

## `DrawingAreaProxy` - WebContent -> UI

`UIProcess/DrawingAreaProxy.messages.in` - direction: annotated

`EnterAcceleratedCompositingMode`, `UpdateAcceleratedCompositingMode`, `DidFirstLayerFlush`, `DispatchPresentationCallbacksAfterFlushingLayers`, `Update`, `ExitAcceleratedCompositingMode`

## `LogStream` - WebContent -> UI

`Shared/LogStream.messages.in` - stream - direction: manual: created in UIProcess/Cocoa/WebProcessProxyCocoa.mm; WebContent logs through it when logd is blocked

`LogOnBehalfOfWebContent`

## `NotificationManagerMessageHandler` - WebContent -> UI, Networking

`Shared/Notifications/NotificationManagerMessageHandler.messages.in` - direction: manual: sent from WebProcess/; handled in UI and Networking (ExceptionForDispatchedTo on main)

`ShowNotification`, `CancelNotification`, `ClearNotifications`, `DidDestroyNotification`, `PageWasNotifiedOfNotificationPermission`, `RequestPermission`, `SetAppBadge`, `GetPermissionState`, `GetPermissionStateSync` (sync)

## `PlatformXRSystem` - WebContent -> UI

`UIProcess/XR/PlatformXRSystem.messages.in` - direction: annotated

`EnumerateImmersiveXRDevices`, `RequestPermissionOnSessionFeatures`, `InitializeTrackingAndRendering`, `ShutDownTrackingAndRendering`, `RequestFrame`, `SubmitFrame`, `DidCompleteShutdownTriggeredBySystem`

## `PlaybackSessionManagerProxy` - WebContent -> UI

`UIProcess/Cocoa/PlaybackSessionManagerProxy.messages.in` - direction: annotated

`CurrentTimeChanged`, `BufferedTimeChanged`, `SeekableRangesVectorChanged`, `CanPlayFastReverseChanged`, `AudioMediaSelectionOptionsChanged`, `LegibleMediaSelectionOptionsChanged`, `AudioMediaSelectionIndexChanged`, `LegibleMediaSelectionIndexChanged`, `ExternalPlaybackPropertiesChanged`, `WirelessVideoPlaybackDisabledChanged`, `DurationChanged`, `PlaybackStartedTimeChanged`, `RateChanged`, `MutedChanged`, `VolumeChanged`, `PictureInPictureSupportedChanged`, `IsInWindowFullscreenActiveChanged`, `SupportsLinearMediaPlayerChanged`, `SpatialVideoMetadataChanged`, `SetUpPlaybackControlsManagerWithID`, `ClearPlaybackControlsManager`, `SwapFullscreenModes`, `HandleControlledElementIDResponse`, `SetLogIdentifier`

## `RemoteLayerTreeDrawingAreaProxy` - WebContent -> UI

`UIProcess/RemoteLayerTree/RemoteLayerTreeDrawingAreaProxy.messages.in` - direction: annotated

`SetPreferredFramesPerSecond`, `WillCommitLayerTree`, `CommitLayerTreeNotTriggered`, `CommitLayerTree`, `AsyncSetLayerContents`

## `RemoteMediaSessionCoordinatorProxy` - WebContent -> UI

`UIProcess/Media/RemoteMediaSessionCoordinatorProxy.messages.in` - direction: annotated

`Join`, `Leave`, `CoordinateSeekTo`, `CoordinatePlay`, `CoordinatePause`, `CoordinateSetTrack`, `PositionStateChanged`, `ReadyStateChanged`, `PlaybackStateChanged`, `TrackIdentifierChanged`

## `RemoteWebInspectorUIProxy` - WebContent -> UI

`UIProcess/Inspector/RemoteWebInspectorUIProxy.messages.in` - direction: annotated

`FrontendLoaded`, `FrontendDidClose`, `Reopen`, `ResetState`, `BringToFront`, `Save`, `Load`, `PickColorFromScreen`, `SetForcedAppearance`, `SetSheetRect`, `StartWindowDrag`, `OpenURLExternally`, `RevealFileExternally`, `ShowCertificate`, `SendMessageToBackend`, `SetInspectorPageDeveloperExtrasEnabled`

## `SmartMagnificationController` - WebContent -> UI

`UIProcess/ios/SmartMagnificationController.messages.in` - direction: annotated

`DidCollectGeometryForSmartMagnificationGesture`, `ScrollToRect`

## `SpeechRecognitionRemoteRealtimeMediaSourceManager` - WebContent -> UI

`UIProcess/SpeechRecognitionRemoteRealtimeMediaSourceManager.messages.in` - direction: annotated

`RemoteAudioSamplesAvailable`, `RemoteCaptureFailed`, `RemoteSourceStopped`, `SetStorage`

## `SpeechRecognitionServer` - WebContent -> UI

`UIProcess/SpeechRecognitionServer.messages.in` - direction: annotated

`Start`, `Stop`, `Abort`, `Invalidate`

## `VideoPresentationManagerProxy` - WebContent -> UI

`UIProcess/Cocoa/VideoPresentationManagerProxy.messages.in` - direction: annotated

`SetHasVideo`, `SetDocumentVisibility`, `AudioSessionCategoryChanged`, `SetVideoDimensions`, `SetupFullscreenWithID`, `SetPlayerIdentifier`, `EnterFullscreen`, `ExitFullscreen`, `SetInlineRect`, `SetHasVideoContentLayer`, `CleanupFullscreen`, `PreparedToReturnToInline`, `PreparedToExitFullscreen`, `ExitFullscreenWithoutAnimationToMode`, `SetVideoFullscreenMode`, `ClearVideoFullscreenMode`, `TextTrackRepresentationUpdate`, `TextTrackRepresentationSetContentsScale`, `TextTrackRepresentationSetHidden`

## `ViewGestureController` - WebContent -> UI

`UIProcess/ViewGestureController.messages.in` - direction: annotated

`DidCollectGeometryForSmartMagnificationGesture`, `DidCollectGeometryForMagnificationGesture`, `DidHitRenderTreeSizeThreshold`

## `VisitedLinkStore` - WebContent -> UI

`UIProcess/VisitedLinkStore.messages.in` - direction: annotated

`AddVisitedLinkHashFromPage`

## `WebAuthenticatorCoordinatorProxy` - WebContent -> UI

`UIProcess/WebAuthentication/WebAuthenticatorCoordinatorProxy.messages.in` - direction: annotated

`MakeCredential`, `GetAssertion`, `isConditionalMediationAvailable`, `IsUserVerifyingPlatformAuthenticatorAvailable`, `GetClientCapabilities`, `Cancel`

## `WebAutomationSession` - WebContent -> UI

`UIProcess/Automation/WebAutomationSession.messages.in` - direction: annotated-on-main

`LogEntryAdded`

## `WebDeviceOrientationUpdateProviderProxy` - WebContent -> UI

`UIProcess/ios/WebDeviceOrientationUpdateProviderProxy.messages.in` - direction: annotated

`StartUpdatingDeviceOrientation`, `StopUpdatingDeviceOrientation`, `StartUpdatingDeviceMotion`, `StopUpdatingDeviceMotion`

## `WebExtensionContext` - WebContent -> UI

`UIProcess/Extensions/WebExtensionContext.messages.in` - direction: annotated

`ActionGetTitle`, `ActionSetTitle`, `ActionSetIcon`, `ActionGetPopup`, `ActionSetPopup`, `ActionOpenPopup`, `ActionGetBadgeText`, `ActionSetBadgeText`, `ActionGetEnabled`, `ActionSetEnabled`, `AlarmsCreate`, `AlarmsGet`, `AlarmsClear`, `AlarmsGetAll`, `AlarmsClearAll`, `CommandsGetAll`, `CookiesGet`, `CookiesGetAll`, `CookiesSet`, `CookiesRemove`, `CookiesGetAllCookieStores`, `DeclarativeNetRequestGetEnabledRulesets`, `DeclarativeNetRequestUpdateEnabledRulesets`, `DeclarativeNetRequestDisplayActionCountAsBadgeText`, `DeclarativeNetRequestIncrementActionCount`, `DeclarativeNetRequestGetMatchedRules`, `DeclarativeNetRequestGetDynamicRules`, `DeclarativeNetRequestUpdateDynamicRules`, `DeclarativeNetRequestGetSessionRules`, `DeclarativeNetRequestUpdateSessionRules`, `DevToolsPanelsCreate`, `DevToolsInspectedWindowEval`, `DevToolsInspectedWindowReload`, `AddListener`, `RemoveListener`, `ExtensionIsAllowedIncognitoAccess`, `MenusCreate`, `MenusUpdate`, `MenusRemove`, `MenusRemoveAll`, `PermissionsGetAll`, `PermissionsContains`, `PermissionsRequest`, `PermissionsRemove`, `PortPostMessage`, `PortRemoved`, `RuntimeGetBackgroundPage`, `RuntimeOpenOptionsPage`, `RuntimeReload`, `RuntimeSendMessage`, `RuntimeConnect`, `RuntimeSendNativeMessage`, `RuntimeConnectNative`, `RuntimeWebPageSendMessage`, `RuntimeWebPageConnect`, `ScriptingExecuteScript`, `ScriptingInsertCSS`, `ScriptingRemoveCSS`, `ScriptingRegisterContentScripts`, `ScriptingUpdateRegisteredScripts`, `ScriptingGetRegisteredScripts`, `ScriptingUnregisterContentScripts`, `SidebarOpen`, `SidebarIsOpen`, `SidebarClose`, `SidebarToggle`, `SidebarGetOptions`, `SidebarSetOptions`, `SidebarGetTitle`, `SidebarSetTitle`, `SidebarSetIcon`, `SidebarSetActionClickBehavior`, `SidebarGetActionClickBehavior`, `StorageGet`, `StorageGetKeys`, `StorageGetBytesInUse`, `StorageSet`, `StorageRemove`, `StorageClear`, `StorageSetAccessLevel`, `TabsCreate`, `TabsUpdate`, `TabsDuplicate`, `TabsGet`, `TabsGetCurrent`, `TabsQuery`, `TabsReload`, `TabsGoBack`, `TabsGoForward`, `TabsDetectLanguage`, `TabsToggleReaderMode`, `TabsCaptureVisibleTab`, `TabsSendMessage`, `TabsConnect`, `TabsGetZoom`, `TabsSetZoom`, `TabsRemove`, `TabsExecuteScript`, `TabsInsertCSS`, `TabsRemoveCSS`, `WebNavigationGetAllFrames`, `WebNavigationGetFrame`, `WindowsCreate`, `WindowsGet`, `WindowsGetLastFocused`, `WindowsGetAll`, `WindowsUpdate`, `WindowsRemove`

## `WebExtensionController` - WebContent -> UI

`UIProcess/Extensions/WebExtensionController.messages.in` - direction: annotated

`DidStartProvisionalLoadForFrame`, `DidCommitLoadForFrame`, `DidFinishLoadForFrame`, `DidFailLoadForFrame`, `TestResult`, `TestEqual`, `TestLogMessage`, `TestSentMessage`, `TestFinished`

## `WebFullScreenManagerProxy` - WebContent -> UI

`UIProcess/WebFullScreenManagerProxy.messages.in` - direction: annotated

`EnterFullScreen`, `UpdateImageSource`, `ExitFullScreen`, `BeganEnterFullScreen`, `BeganExitFullScreen`, `Close`

## `WebGeolocationManagerProxy` - WebContent -> UI

`UIProcess/WebGeolocationManagerProxy.messages.in` - direction: annotated

`StartUpdating`, `StopUpdating`, `SetEnableHighAccuracy`

## `WebInspectorUIExtensionControllerProxy` - WebContent -> UI

`UIProcess/Inspector/WebInspectorUIExtensionControllerProxy.messages.in` - direction: annotated

`DidShowExtensionTab`, `DidHideExtensionTab`, `DidNavigateExtensionTab`, `InspectedPageDidNavigate`

## `WebInspectorUIProxy` - WebContent -> UI

`UIProcess/Inspector/WebInspectorUIProxy.messages.in` - direction: annotated

`RequestOpenLocalInspectorFrontend`, `SetFrontendConnection`, `SendMessageToBackend`, `FrontendLoaded`, `DidClose`, `BringToFront`, `Reopen`, `ResetState`, `SetForcedAppearance`, `EffectiveAppearanceDidChange`, `OpenURLExternally`, `RevealFileExternally`, `InspectedURLChanged`, `ShowCertificate`, `ElementSelectionChanged`, `TimelineRecordingChanged`, `SetDeveloperPreferenceOverride`, `SetEmulatedConditions`, `Save`, `Load`, `PickColorFromScreen`, `AttachBottom`, `AttachRight`, `AttachLeft`, `Detach`, `AttachAvailabilityChanged`, `SetAttachedWindowHeight`, `SetAttachedWindowWidth`, `SetSheetRect`, `StartWindowDrag`, `SetInspectorPageDeveloperExtrasEnabled`

## `WebLockRegistryProxy` - WebContent -> UI

`UIProcess/WebLockRegistryProxy.messages.in` - direction: annotated

`RequestLock`, `ReleaseLock`, `AbortLockRequest`, `Snapshot`, `ClientIsGoingAway`

## `WebPageProxy` - WebContent -> UI

`UIProcess/WebPageProxy.messages.in` - direction: annotated

`CreateNewPage` (sync), `ShowPage`, `ClosePage`, `RunJavaScriptAlert` (sync), `RunJavaScriptConfirm` (sync), `RunJavaScriptPrompt` (sync), `MouseDidMoveOverElement`, `DidReceiveEvent`, `SetCursor`, `SetCursorHiddenUntilMouseMoves`, `SetFocus`, `TakeFocus`, `FocusFromServiceWorker`, `FocusedFrameChanged`, `SetRenderTreeSize`, `SetToolbarsAreVisible`, `GetToolbarsAreVisible` (sync), `SetMenuBarIsVisible`, `GetMenuBarIsVisible` (sync), `SetStatusBarIsVisible`, `GetStatusBarIsVisible` (sync), `SetIsResizable`, `SetWindowFrame`, `GetWindowFrame` (sync), `ScreenToRootView` (sync), `RootViewPointToScreen` (sync), `RootViewRectToScreen` (sync), `AccessibilityScreenToRootView` (sync), `RootViewToAccessibilityScreen` (sync), `RelayAccessibilityNotification`, `EnableAccessibilityForAllProcesses`, `ShowValidationMessage`, `HideValidationMessage`, `RunBeforeUnloadConfirmPanel` (sync), `PageDidScroll`, `SetHasActiveAnimatedScrolls`, `RunOpenPanel`, `ShowShareSheet`, `ShowContactPicker`, `PrintFrame` (sync), `RunModal`, `NotifyScrollerThumbIsVisibleInRect`, `RecommendedScrollbarStyleDidChange`, `DidChangeScrollbarsForMainFrame`, `DidChangeScrollOffsetPinningForMainFrame`, `DidChangePageCount`, `ThemeColorChanged`, `PageExtendedBackgroundColorDidChange`, `SampledPageTopColorChanged`, `SetCanShortCircuitHorizontalWheelEvents`, `DidChangeContentSize`, `DidChangeIntrinsicContentSize`, `ShowColorPicker`, `SetColorPickerColor`, `EndColorPicker`, `ShowDataListSuggestions`, `HandleKeydownInDataList`, `EndDataListSuggestions`, `ShowDateTimePicker`, `EndDateTimePicker`, `DecidePolicyForResponse`, `DecidePolicyForNavigationActionAsync`, `DecidePolicyForNavigationActionSync` (sync), `DecidePolicyForNewWindowAction`, `DidChangeProgress`, `DidFinishProgress`, `DidStartProgress`, `SetNetworkRequestsInProgress`, `StartNetworkRequestsForPageLoadTiming`, `EndNetworkRequestsForPageLoadTiming`, `DidCreateSubframe`, `DidDestroyFrame`, `DidStartProvisionalLoadForFrame`, `DidReceiveServerRedirectForProvisionalLoadForFrame`, `WillPerformClientRedirectForFrame`, `DidCancelClientRedirectForFrame`, `DidChangeProvisionalURLForFrame`, `DidFailProvisionalLoadForFrame`, `DidCommitLoadForFrame`, `DidFailLoadForFrame`, `DidFinishDocumentLoadForFrame`, `DidFinishLoadForFrame`, `DidFirstLayoutForFrame`, `DidFirstVisuallyNonEmptyLayoutForFrame`, `DidReachLayoutMilestone`, `DidReceiveTitleForFrame`, `DidDisplayInsecureContentForFrame`, `DidRunInsecureContentForFrame`, `DidSameDocumentNavigationForFrame`, `DidSameDocumentNavigationForFrameViaJS`, `DidChangeMainDocument`, `DidExplicitOpenForFrame`, `DidDestroyNavigation`, `UpdateSandboxFlags`, `UpdateOpener`, `UpdateScrollingMode`, `UpdateRemoteFrameSize`, `ResolveAccessibilityHitTestForTesting`, `MainFramePluginHandlesPageScaleGestureDidChange`, `DidInitiateLoadForResource`, `DidSendRequestForResource`, `DidReceiveResponseForResource`, `DidFinishLoadForResource`, `DidNavigateWithNavigationData`, `DidPerformClientRedirect`, `DidPerformServerRedirect`, `DidUpdateHistoryTitle`, `DidFinishLoadingDataForCustomContentProvider`, `WillSubmitForm`, `InterpretKeyEvent` (sync), `DidReceivePositionInformation`, `SaveImageToLibrary`, `ShowPlaybackTargetPicker`, `CommitPotentialTapFailed`, `DidNotHandleTapAsClick`, `DidCompleteSyntheticClick`, `DidHandleTapAsHover`, `DisableDoubleTapGesturesDuringTapIfNecessary`, `HandleSmartMagnificationInformationForPotentialTap`, `IsPotentialTapInProgress`, `SetDataDetectionResult`, `HandleClickForDataDetectionResult`, `PageScaleFactorDidChange`, `ViewScaleFactorDidChange`, `PluginScaleFactorDidChange`, `PluginZoomFactorDidChange`, `BindAccessibilityTree`, `SetInputMethodState`, `BackForwardAddItem`, `BackForwardSetChildItem`, `BackForwardClearChildren`, `BackForwardUpdateItem`, `BackForwardGoToItem` (sync), `BackForwardItemAtIndex` (sync), `BackForwardListContainsItem` (sync), `BackForwardListCounts` (sync), `ShouldGoToBackForwardListItemSync` (sync), `RegisterEditCommandForUndo`, `ClearAllEditCommands`, `RegisterInsertionUndoGrouping`, `CanUndoRedo` (sync), `ExecuteUndoRedo` (sync), `LogDiagnosticMessageFromWebProcess`, `LogDiagnosticMessageWithResultFromWebProcess`, `LogDiagnosticMessageWithValueFromWebProcess`, `LogDiagnosticMessageWithEnhancedPrivacyFromWebProcess`, `LogDiagnosticMessageWithValueDictionaryFromWebProcess`, `LogDiagnosticMessageWithDomainFromWebProcess`, `LogScrollingEvent`, `EditorStateChanged`, `CompositionWasCanceled`, `SetHasFocusedElementWithUserInteraction`, `RequestTextRecognition`, `HandleContextMenuTranslation`, `ProofreadingSessionShowDetailsForSuggestionWithIDRelativeToRect`, `ProofreadingSessionUpdateStateForSuggestionWithID`, `AddTextAnimationForAnimationID`, `AddTextAnimationForAnimationIDWithCompletionHandler`, `RemoveTextAnimationForAnimationID`, `DidEndPartialIntelligenceTextAnimation`, `ShowMediaControlsContextMenu`, `SetIsTouchBarUpdateSuppressedForHiddenContentEditable`, `SetIsNeverRichlyEditableForTouchBar`, `RequestDOMPasteAccess` (sync), `SetTextIndicatorFromFrame`, `ClearTextIndicator`, `DidGetImageForFindMatch`, `ShowPopupMenuFromFrame`, `HidePopupMenu`, `ShowContextMenu`, `ShowContextMenuFromFrame`, `DidFinishServiceWorkerPageRegistration`, `ExceededDatabaseQuota` (sync), `RequestGeolocationPermissionForFrame`, `RevokeGeolocationAuthorizationToken`, `RequestUserMediaPermissionForFrame`, `EnumerateMediaDevicesForFrame`, `BeginMonitoringCaptureDevices`, `ValidateCaptureStateUpdate`, `SetShouldListenToVoiceActivity`, `RequestMediaKeySystemPermissionForFrame`, `RequestNotificationPermission`, `CheckTextOfParagraph` (sync), `CheckSpellingOfString` (sync), `CheckGrammarOfString` (sync), `SpellingUIIsShowing` (sync), `UpdateSpellingUIWithMisspelledWord`, `UpdateSpellingUIWithGrammarString`, `GetGuessesForWord` (sync), `LearnWord`, `IgnoreWord`, `RequestCheckingOfString`, `StartDrag`, `SetPromisedDataForImage`, `StartDrag`, `DidHandleDragStartRequest`, `DidHandleAdditionalDragItemsRequest`, `WillReceiveEditDragSnapshot`, `DidReceiveEditDragSnapshot`, `DidPerformDictionaryLookup`, `ExecuteSavedCommandBySelector` (sync), `RegisterWebProcessAccessibilityToken`, `GetIsSpeaking` (sync), `MakeFirstResponder`, `AssistiveTechnologyMakeFirstResponder`, `SearchTheWeb`, `SubstitutionsPanelIsShowing` (sync), `toggleSmartInsertDelete`, `toggleAutomaticQuoteSubstitution`, `toggleAutomaticLinkDetection`, `toggleAutomaticDashSubstitution`, `toggleAutomaticTextReplacement`, `ShowCorrectionPanel`, `DismissCorrectionPanel`, `DismissCorrectionPanelSoon` (sync), `RecordAutocorrectionResponse`, `SetEditableElementIsFocused`, `HandleAcceptsFirstMouse`, `DidUpdateRenderingAfterCommittingLoad`, `ShowDictationAlternativeUI`, `RemoveDictationAlternatives`, `DictationAlternatives` (sync), `BeginTextRecognitionForVideoInElementFullScreen`, `CancelTextRecognitionForVideoInElementFullScreen`, `CouldNotRestorePageState`, `RestorePageState`, `RestorePageCenterAndScale`, `DidGetTapHighlightGeometries`, `ElementDidFocus`, `ElementDidBlur`, `UpdateInputContextAfterBlurringAndRefocusingElement`, `DidProgrammaticallyClearFocusedElement`, `UpdateFocusedElementInformation`, `FocusedElementDidChangeInputMode`, `ScrollingNodeScrollWillStartScroll`, `ScrollingNodeScrollDidEndScroll`, `ShowInspectorHighlight`, `HideInspectorHighlight`, `ShowInspectorIndication`, `HideInspectorIndication`, `EnableInspectorNodeSearch`, `DisableInspectorNodeSearch`, `UpdateStringForFind`, `HandleAutocorrectionContext`, `ShowDataDetectorsUIForPositionInformation`, `DidChangeInspectorFrontendCount`, `CreateInspectorTarget`, `DestroyInspectorTarget`, `SendMessageToInspectorFrontend`, `SaveRecentSearches`, `LoadRecentSearches` (sync), `DidUpdateActivityState`, `WrapCryptoKey` (sync), `SerializeAndWrapCryptoKey` (sync), `UnwrapCryptoKey` (sync), `ShowTelephoneNumberMenu`, `DidStartLoadForQuickLookDocumentInMainFrame`, `DidFinishLoadForQuickLookDocumentInMainFrame`, `RequestPasswordForQuickLookDocumentInMainFrame`, `ContentFilterDidBlockLoadForFrame`, `IsAnyAnimationAllowedToPlayDidChange`, `IsPlayingMediaDidChange`, `HandleAutoplayEvent`, `DidPerformImmediateActionHitTest`, `HandleMessage`, `HandleMessageWithAsyncReply`, `HandleSynchronousMessage` (sync), `HandleAutoFillButtonClick`, `DidResignInputElementStrongPasswordAppearance`, `PerformSwitchHapticFeedback`, `ContentRuleListNotification`, `AddPlaybackTargetPickerClient`, `RemovePlaybackTargetPickerClient`, `ShowPlaybackTargetPicker`, `PlaybackTargetPickerClientStateDidChange`, `SetMockMediaPlaybackTargetPickerEnabled`, `SetMockMediaPlaybackTargetPickerState`, `MockMediaPlaybackTargetPickerDismissPopup`, `SetMockVideoPresentationModeEnabled`, `RequestPointerLock`, `RequestPointerUnlock`, `DidFailToSuspendAfterProcessSwap`, `DidSuspendAfterProcessSwap`, `ImageOrMediaDocumentSizeChanged`, `UseFixedLayoutDidChange`, `FixedLayoutSizeDidChange`, `DidRestoreScrollPosition`, `RequestScrollToRect`, `GetLoadDecisionForIcon`, `StartURLSchemeTask`, `StopURLSchemeTask`, `LoadSynchronousURLSchemeTask` (sync), `ShouldAllowDeviceOrientationAndMotionAccess`, `RegisterAttachmentIdentifierFromData`, `RegisterAttachmentIdentifierFromFilePath`, `RegisterAttachmentIdentifier`, `RegisterAttachmentsFromSerializedData`, `CloneAttachmentData`, `DidInsertAttachmentWithIdentifier`, `DidRemoveAttachmentWithIdentifier`, `SerializedAttachmentDataForIdentifiers` (sync), `WritePromisedAttachmentToPasteboard`, `RequestAttachmentIcon`, `SpeechSynthesisVoiceList` (sync), `SpeechSynthesisSpeak`, `SpeechSynthesisSetFinishedCallback`, `SpeechSynthesisCancel`, `SpeechSynthesisPause`, `SpeechSynthesisResume`, `SpeechSynthesisResetState`, `ShowPDFContextMenu`, `PluginDidInstallPDFDocument`, `CreatePDFHUD`, `UpdatePDFHUDLocation`, `RemovePDFHUD`, `ConfigureLoggingChannel`, `ShowEmojiPicker`, `DidCreateContextInWebProcessForVisibilityPropagation`, `SetMockWebAuthenticationConfiguration`, `SendMessageToWebView`, `SendMessageToWebViewWithReply`, `DidFindTextManipulationItems`, `AddMediaUsageManagerSession`, `UpdateMediaUsageManagerSessionState`, `RemoveMediaUsageManagerSession`, `SetHasExecutedAppBoundBehaviorBeforeNavigation`, `ChangeUniversalAccessZoomFocus`, `TakeModelElementFullscreen`, `ModelElementSetInteractionEnabled`, `ModelElementCreateRemotePreview`, `ModelElementLoadRemotePreview`, `ModelElementDestroyRemotePreview`, `ModelElementSizeDidChange`, `HandleMouseDownForModelElement`, `HandleMouseMoveForModelElement`, `HandleMouseUpForModelElement`, `ModelInlinePreviewUUIDs`, `ModelElementGetCamera`, `ModelElementSetCamera`, `ModelElementIsPlayingAnimation`, `ModelElementSetAnimationIsPlaying`, `ModelElementIsLoopingAnimation`, `ModelElementSetIsLoopingAnimation`, `ModelElementAnimationDuration`, `ModelElementAnimationCurrentTime`, `ModelElementSetAnimationCurrentTime`, `ModelElementHasAudio`, `ModelElementIsMuted`, `ModelElementSetIsMuted`, `StartApplePayAMSUISession`, `AbortApplePayAMSUISession`, `BeginSystemPreview`, `DidCreateSleepDisabler`, `DidDestroySleepDisabler`, `RequestCookieConsent`, `DidAccessWindowProxyPropertyViaOpenerForFrame`, `DidApplyLinkDecorationFiltering`, `BroadcastProcessSyncData`, `BroadcastTopDocumentSyncData`, `DispatchLoadEventToFrameOwnerElement`, `FocusRemoteFrame`, `PostMessageToRemote`, `RenderTreeAsTextForTesting` (sync), `FrameTextForTesting` (sync), `LayerTreeAsTextForTesting` (sync), `BindRemoteAccessibilityFrames` (sync), `UpdateRemoteFrameAccessibilityOffset`, `DocumentURLForConsoleLog`, `NowPlayingMetadataChanged`, `DidAdjustVisibilityWithSelectors`, `FrameNameChanged`, `GamepadsRecentlyAccessed`, `HasActiveNowPlayingSessionChanged`, `SetAllowsLayoutViewportHeightExpansion`, `ShouldOffloadIFrameForHost`

## `WebPasteboardProxy` - WebContent -> UI

`UIProcess/WebPasteboardProxy.messages.in` - direction: annotated

`WriteURLToPasteboard`, `WriteWebContentToPasteboard`, `WriteImageToPasteboard`, `WriteStringToPasteboard`, `UpdateSupportedTypeIdentifiers`, `WriteCustomData` (sync), `TypesSafeForDOMToReadAndWrite` (sync), `AllPasteboardItemInfo` (sync), `InformationForItemAtIndex` (sync), `GetPasteboardItemsCount` (sync), `ReadStringFromPasteboard` (sync), `ReadURLFromPasteboard` (sync), `ReadBufferFromPasteboard` (sync), `ContainsStringSafeForDOMToReadForType` (sync), `GetNumberOfFiles` (sync), `GetPasteboardTypes` (sync), `GetPasteboardPathnamesForType` (sync), `GetPasteboardStringForType` (sync), `GetPasteboardStringsForType` (sync), `GetPasteboardBufferForType` (sync), `GetPasteboardChangeCount` (sync), `GetPasteboardColor` (sync), `GetPasteboardURL` (sync), `AddPasteboardTypes` (sync), `SetPasteboardTypes` (sync), `SetPasteboardURL` (sync), `SetPasteboardColor` (sync), `SetPasteboardStringForType` (sync), `SetPasteboardBufferForType` (sync), `ContainsURLStringSuitableForLoading` (sync), `URLStringSuitableForLoading` (sync), `TestIPCSharedMemory` (sync), `GetTypes` (sync), `ReadText` (sync), `ReadFilePaths` (sync), `ReadBuffer` (sync), `WriteToClipboard`, `ClearClipboard`, `GetPasteboardChangeCount` (sync), `GetPasteboardTypes` (sync), `WriteWebContentToPasteboard`, `WriteStringToPasteboard`

## `WebPaymentCoordinatorProxy` - WebContent -> UI

`Shared/ApplePay/WebPaymentCoordinatorProxy.messages.in` - direction: manual: DispatchedFrom=WebContent; To=UI, or Networking when APPLE_PAY_REMOTE_UI (comment on main)

`CanMakePayments` (sync), `CanMakePaymentsWithActiveCard`, `OpenPaymentSetup`, `ShowPaymentUI` (sync), `CompleteMerchantValidation`, `CompleteShippingMethodSelection`, `CompleteShippingContactSelection`, `CompletePaymentMethodSelection`, `CompleteCouponCodeChange`, `CompletePaymentSession`, `AbortPaymentSession`, `CancelPaymentSession`, `GetSetupFeatures`, `BeginApplePaySetup`, `EndApplePaySetup`

## `WebPermissionControllerProxy` - WebContent -> UI

`UIProcess/WebPermissionControllerProxy.messages.in` - direction: annotated

`Query`

## `WebProcessPool` - WebContent -> UI

`UIProcess/WebProcessPool.messages.in` - direction: annotated

`HandleMessage`, `HandleSynchronousMessage` (sync), `StartedUsingGamepads`, `StoppedUsingGamepads`, `PlayGamepadEffect`, `StopGamepadEffects`, `ReportWebContentCPUTime`

## `WebProcessProxy` - WebContent -> UI

`UIProcess/WebProcessProxy.messages.in` - direction: annotated

`DidDestroyUserGestureToken`, `ShouldTerminate` (sync), `EnableSuddenTermination`, `DisableSuddenTermination`, `GetNetworkProcessConnection` (sync), `WaitForSharedPreferencesForWebProcessToSync` (sync), `CreateGPUProcessConnection`, `GPUProcessConnectionDidBecomeUnresponsive`, `CreateModelProcessConnection`, `DidExceedActiveMemoryLimit`, `DidExceedInactiveMemoryLimit`, `DidExceedMemoryFootprintThreshold`, `DidExceedCPULimit`, `StopResponsivenessTimer`, `DidReceiveBackgroundResponsivenessPing`, `MemoryPressureStatusChanged`, `DidCollectPrewarmInformation`, `CacheMediaMIMETypes`, `StartDisplayLink`, `StopDisplayLink`, `SetDisplayLinkPreferredFramesPerSecond`, `SendMessageToWebContext`, `SendMessageToWebContextWithReply`, `CreateSpeechRecognitionServer`, `DestroySpeechRecognitionServer`, `SystemBeep`, `IsAXAuthenticated` (sync), `SetCaptionDisplayMode`, `SetCaptionLanguage`, `GetNotifications`, `SetAppBadge`, `SetClientBadge`, `WrapCryptoKey` (sync), `SerializeAndWrapCryptoKey` (sync), `UnwrapCryptoKey` (sync), `SetupLogStream`

## `WebScreenOrientationManagerProxy` - WebContent -> UI

`UIProcess/WebScreenOrientationManagerProxy.messages.in` - direction: annotated

`CurrentOrientation` (sync), `Lock`, `Unlock`, `SetShouldSendChangeNotification`

## `WebUserContentControllerProxy` - WebContent -> UI

`UIProcess/UserContent/WebUserContentControllerProxy.messages.in` - direction: annotated

`DidPostMessage`

## `GPUConnectionToWebProcess` - WebContent -> GPU

`GPUProcess/GPUConnectionToWebProcess.messages.in` - direction: annotated

`CreateRenderingBackend`, `ReleaseRenderingBackend`, `CreateGraphicsContextGL`, `ReleaseGraphicsContextGL`, `CreateGPU`, `ReleaseGPU`, `ClearNowPlayingInfo`, `SetNowPlayingInfo`, `EnsureAudioSession` (sync), `EnsureMediaSessionHelper`, `CreateVisibilityPropagationContextForPage`, `DestroyVisibilityPropagationContextForPage`, `SetMediaOverridesForTesting`, `CreateAudioHardwareListener`, `ReleaseAudioHardwareListener`, `CreateRemoteCommandListener`, `ReleaseRemoteCommandListener`, `ConfigureLoggingChannel`, `CreateWCLayerTreeHost`, `ReleaseWCLayerTreeHost`, `EnableMockMediaSource`, `UpdateSampleBufferDisplayLayerBoundsAndPosition`, `SetMediaEnvironment`

## `LibWebRTCCodecsProxy` - WebContent -> GPU

`GPUProcess/webrtc/LibWebRTCCodecsProxy.messages.in` - direction: annotated

`CreateDecoder`, `ReleaseDecoder`, `FlushDecoder`, `SetDecoderFormatDescription`, `DecodeFrame`, `SetFrameSize`, `CreateEncoder`, `ReleaseEncoder`, `InitializeEncoder`, `EncodeFrame`, `FlushEncoder`, `SetEncodeRates`, `SetSharedVideoFrameSemaphore`, `SetSharedVideoFrameMemory`, `SetRTCLoggingLevel`

## `RemoteAdapter` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteAdapter.messages.in` - stream - direction: annotated

`Destruct`, `RequestDevice` (sync)

## `RemoteAudioDestinationManager` - WebContent -> GPU

`GPUProcess/media/RemoteAudioDestinationManager.messages.in` - direction: annotated

`CreateAudioDestination`, `DeleteAudioDestination`, `StartAudioDestination`, `StopAudioDestination`, `AudioSamplesStorageChanged`

## `RemoteAudioMediaStreamTrackRendererInternalUnitManager` - WebContent -> GPU

`GPUProcess/webrtc/RemoteAudioMediaStreamTrackRendererInternalUnitManager.messages.in` - direction: annotated

`CreateUnit`, `DeleteUnit`, `StartUnit`, `StopUnit`, `SetLastDeviceUsed`

## `RemoteAudioSessionProxy` - WebContent -> GPU

`GPUProcess/media/RemoteAudioSessionProxy.messages.in` - direction: annotated

`SetCategory`, `SetPreferredBufferSize`, `TryToSetActive` (sync), `SetIsPlayingToBluetoothOverride`, `TriggerBeginInterruptionForTesting`, `TriggerEndInterruptionForTesting`, `BeginInterruptionRemote`, `EndInterruptionRemote`, `SetSceneIdentifier`, `SetSoundStageSize`

## `RemoteBarcodeDetector` - WebContent -> GPU

`GPUProcess/ShapeDetection/RemoteBarcodeDetector.messages.in` - stream - direction: annotated

`Detect`

## `RemoteBindGroup` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteBindGroup.messages.in` - stream - direction: annotated

`Destruct`, `SetLabel`, `UpdateExternalTextures` (sync)

## `RemoteBindGroupLayout` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteBindGroupLayout.messages.in` - stream - direction: annotated

`Destruct`, `SetLabel`

## `RemoteBuffer` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteBuffer.messages.in` - stream - direction: annotated

`GetMappedRange` (sync), `MapAsync`, `Copy`, `Unmap`, `Destroy`, `Destruct`, `SetLabel`

## `RemoteCDMFactoryProxy` - WebContent -> GPU

`GPUProcess/media/RemoteCDMFactoryProxy.messages.in` - direction: annotated

`CreateCDM` (sync), `SupportsKeySystem` (sync), `RemoveInstance`, `RemoveSession`

## `RemoteCDMInstanceProxy` - WebContent -> GPU

`GPUProcess/media/RemoteCDMInstanceProxy.messages.in` - direction: annotated

`CreateSession` (sync), `InitializeWithConfiguration`, `SetServerCertificate`, `SetStorageDirectory`

## `RemoteCDMInstanceSessionProxy` - WebContent -> GPU

`GPUProcess/media/RemoteCDMInstanceSessionProxy.messages.in` - direction: annotated

`SetLogIdentifier`, `RequestLicense`, `UpdateLicense`, `LoadSession`, `CloseSession`, `RemoveSessionData`, `StoreRecordOfKeyUsage`

## `RemoteCDMProxy` - WebContent -> GPU

`GPUProcess/media/RemoteCDMProxy.messages.in` - direction: annotated

`GetSupportedConfiguration`, `CreateInstance` (sync), `LoadAndInitialize`, `SetLogIdentifier`

## `RemoteCommandBuffer` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteCommandBuffer.messages.in` - stream - direction: annotated

`Destruct`, `SetLabel`

## `RemoteCommandEncoder` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteCommandEncoder.messages.in` - stream - direction: annotated

`BeginRenderPass`, `BeginComputePass`, `CopyBufferToBuffer`, `CopyBufferToTexture`, `CopyTextureToBuffer`, `CopyTextureToTexture`, `ClearBuffer`, `Destruct`, `PushDebugGroup`, `PopDebugGroup`, `InsertDebugMarker`, `WriteTimestamp`, `ResolveQuerySet`, `Finish`, `SetLabel`

## `RemoteCompositorIntegration` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteCompositorIntegration.messages.in` - stream - direction: annotated

`RecreateRenderBuffers` (sync), `PrepareForDisplay` (sync), `PaintCompositedResultsToCanvas` (sync), `Destruct`

## `RemoteComputePassEncoder` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteComputePassEncoder.messages.in` - stream - direction: annotated

`Destruct`, `SetPipeline`, `Dispatch`, `DispatchIndirect`, `End`, `SetBindGroup`, `PushDebugGroup`, `PopDebugGroup`, `InsertDebugMarker`, `SetLabel`

## `RemoteComputePipeline` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteComputePipeline.messages.in` - stream - direction: annotated

`Destruct`, `GetBindGroupLayout`, `SetLabel`

## `RemoteDevice` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteDevice.messages.in` - stream - direction: annotated

`Destroy`, `Destruct`, `CreateXRBinding`, `CreateBuffer`, `CreateTexture`, `CreateSampler`, `CreateBindGroupLayout`, `CreatePipelineLayout`, `CreateBindGroup`, `CreateShaderModule`, `CreateComputePipeline`, `CreateRenderPipeline`, `CreateComputePipelineAsync`, `CreateRenderPipelineAsync`, `CreateCommandEncoder`, `CreateRenderBundleEncoder`, `CreateQuerySet`, `PushErrorScope`, `PopErrorScope`, `ResolveUncapturedErrorEvent`, `ResolveDeviceLostPromise`, `SetLabel`, `PauseAllErrorReporting`, `SetSharedVideoFrameSemaphore`, `SetSharedVideoFrameMemory`, `ImportExternalTextureFromVideoFrame`, `UpdateExternalTexture`

## `RemoteDisplayListRecorder` - WebContent -> GPU

`GPUProcess/graphics/RemoteDisplayListRecorder.messages.in` - stream - direction: annotated

`Save`, `Restore`, `Translate`, `Rotate`, `Scale`, `SetCTM`, `ConcatenateCTM`, `SetInlineFillColor`, `SetInlineStroke`, `SetState`, `SetLineCap`, `SetLineDash`, `SetLineJoin`, `SetMiterLimit`, `ClearDropShadow`, `Clip`, `ClipRoundedRect`, `ClipOut`, `ClipOutRoundedRect`, `ClipToImageBuffer`, `ClipOutToPath`, `ClipPath`, `ResetClip`, `DrawGlyphs`, `DrawDecomposedGlyphs`, `DrawFilteredImageBuffer`, `DrawImageBuffer`, `DrawNativeImage`, `DrawSystemImage`, `DrawPattern`, `BeginTransparencyLayer`, `BeginTransparencyLayerWithCompositeMode`, `EndTransparencyLayer`, `DrawRect`, `DrawLine`, `DrawLinesForText`, `DrawDotsForDocumentMarker`, `DrawEllipse`, `DrawPath`, `DrawFocusRingPath`, `DrawFocusRingRects`, `FillRect`, `FillRectWithColor`, `FillRectWithGradient`, `FillRectWithGradientAndSpaceTransform`, `FillCompositedRect`, `FillRoundedRect`, `FillRectWithRoundedHole`, `FillLine`, `FillArc`, `FillClosedArc`, `FillQuadCurve`, `FillBezierCurve`, `FillPathSegment`, `FillPath`, `FillEllipse`, `StrokeRect`, `StrokeLine`, `StrokeLineWithColorAndThickness`, `StrokeArc`, `StrokeClosedArc`, `StrokeQuadCurve`, `StrokeBezierCurve`, `StrokePathSegment`, `StrokePath`, `StrokeEllipse`, `ClearRect`, `DrawControlPart`, `ApplyStrokePattern`, `ApplyFillPattern`, `ApplyDeviceScaleFactor`, `BeginPage`, `EndPage`, `SetURLForRect`, `DrawVideoFrame`, `SetSharedVideoFrameSemaphore`, `SetSharedVideoFrameMemory`

## `RemoteExternalTexture` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteExternalTexture.messages.in` - stream - direction: annotated

`Destruct`, `SetLabel`, `Destroy`, `Undestroy`

## `RemoteFaceDetector` - WebContent -> GPU

`GPUProcess/ShapeDetection/RemoteFaceDetector.messages.in` - stream - direction: annotated

`Detect`

## `RemoteGPU` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteGPU.messages.in` - stream - direction: annotated

`RequestAdapter` (sync), `CreatePresentationContext`, `CreateCompositorIntegration`, `IsValid` (sync)

## `RemoteGraphicsContextGL` - WebContent -> GPU

`GPUProcess/graphics/RemoteGraphicsContextGL.messages.in` - stream - direction: annotated

`Reshape`, `PrepareForDisplay` (sync), `PrepareForDisplay` (sync), `PrepareForDisplay` (sync), `PrepareForDisplay` (sync), `EnsureExtensionEnabled`, `GetErrors` (sync), `DrawSurfaceBufferToImageBuffer` (sync), `SurfaceBufferToVideoFrame` (sync), `CopyTextureFromVideoFrame` (sync), `SetSharedVideoFrameSemaphore`, `SetSharedVideoFrameMemory`, `SimulateEventForTesting`, `GetBufferSubDataInline` (sync), `GetBufferSubDataSharedMemory` (sync), `ReadPixelsInline` (sync), `ReadPixelsSharedMemory` (sync), `MultiDrawArraysANGLE`, `MultiDrawArraysInstancedANGLE`, `MultiDrawElementsANGLE`, `MultiDrawElementsInstancedANGLE`, `MultiDrawArraysInstancedBaseInstanceANGLE`, `MultiDrawElementsInstancedBaseVertexBaseInstanceANGLE`, `ActiveTexture`, `AttachShader`, `BindAttribLocation`, `BindBuffer`, `BindFramebuffer`, `BindRenderbuffer`, `BindTexture`, `BlendColor`, `BlendEquation`, `BlendEquationSeparate`, `BlendFunc`, `BlendFuncSeparate`, `CheckFramebufferStatus` (sync), `Clear`, `ClearColor`, `ClearDepth`, `ClearStencil`, `ColorMask`, `CompileShader`, `CopyTexImage2D`, `CopyTexSubImage2D`, `CreateBuffer`, `CreateFramebuffer`, `CreateProgram`, `CreateRenderbuffer`, `CreateShader`, `CreateTexture`, `CullFace`, `DeleteBuffer`, `DeleteFramebuffer`, `DeleteProgram`, `DeleteRenderbuffer`, `DeleteShader`, `DeleteTexture`, `DepthFunc`, `DepthMask`, `DepthRange`, `DetachShader`, `Disable`, `DisableVertexAttribArray`, `DrawArrays`, `DrawElements`, `Enable`, `EnableVertexAttribArray`, `Finish`, `Flush`, `FramebufferRenderbuffer`, `FramebufferTexture2D`, `FrontFace`, `GenerateMipmap`, `GetActiveAttrib` (sync), `GetActiveUniform` (sync), `GetAttribLocation` (sync), `GetBufferParameteri` (sync), `GetString` (sync), `GetFloatv` (sync), `GetIntegerv` (sync), `GetIntegeri_v` (sync), `GetInteger64` (sync), `GetInteger64i` (sync), `GetProgrami` (sync), `GetBooleanv` (sync), `GetFramebufferAttachmentParameteri` (sync), `GetProgramInfoLog` (sync), `GetRenderbufferParameteri` (sync), `GetShaderi` (sync), `GetShaderInfoLog` (sync), `GetShaderPrecisionFormat` (sync), `GetShaderSource` (sync), `GetTexParameterf` (sync), `GetTexParameteri` (sync), `GetUniformfv` (sync), `GetUniformiv` (sync), `GetUniformuiv` (sync), `GetUniformLocation` (sync), `GetVertexAttribOffset` (sync), `Hint`, `IsBuffer` (sync), `IsEnabled` (sync), `IsFramebuffer` (sync), `IsProgram` (sync), `IsRenderbuffer` (sync), `IsShader` (sync), `IsTexture` (sync), `LineWidth`, `LinkProgram`, `PixelStorei`, `PolygonOffset`, `RenderbufferStorage`, `SampleCoverage`, `Scissor`, `ShaderSource`, `StencilFunc`, `StencilFuncSeparate`, `StencilMask`, `StencilMaskSeparate`, `StencilOp`, `StencilOpSeparate`, `TexParameterf`, `TexParameteri`, `Uniform1f`, `Uniform1fv`, `Uniform1i`, `Uniform1iv`, `Uniform2f`, `Uniform2fv`, `Uniform2i`, `Uniform2iv`, `Uniform3f`, `Uniform3fv`, `Uniform3i`, `Uniform3iv`, `Uniform4f`, `Uniform4fv`, `Uniform4i`, `Uniform4iv`, `UniformMatrix2fv`, `UniformMatrix3fv`, `UniformMatrix4fv`, `UseProgram`, `ValidateProgram`, `VertexAttrib1f`, `VertexAttrib1fv`, `VertexAttrib2f`, `VertexAttrib2fv`, `VertexAttrib3f`, `VertexAttrib3fv`, `VertexAttrib4f`, `VertexAttrib4fv`, `VertexAttribPointer`, `Viewport`, `BufferData0`, `BufferData1`, `BufferSubData`, `ReadPixelsBufferObject`, `TexImage2D0`, `TexImage2D1`, `TexSubImage2D0`, `TexSubImage2D1`, `CompressedTexImage2D0`, `CompressedTexImage2D1`, `CompressedTexSubImage2D0`, `CompressedTexSubImage2D1`, `DrawArraysInstanced`, `DrawElementsInstanced`, `VertexAttribDivisor`, `CreateVertexArray`, `DeleteVertexArray`, `IsVertexArray` (sync), `BindVertexArray`, `CopyBufferSubData`, `BlitFramebuffer`, `FramebufferTextureLayer`, `InvalidateFramebuffer`, `InvalidateSubFramebuffer`, `ReadBuffer`, `RenderbufferStorageMultisample`, `TexStorage2D`, `TexStorage3D`, `TexImage3D0`, `TexImage3D1`, `TexSubImage3D0`, `TexSubImage3D1`, `CopyTexSubImage3D`, `CompressedTexImage3D0`, `CompressedTexImage3D1`, `CompressedTexSubImage3D0`, `CompressedTexSubImage3D1`, `GetFragDataLocation` (sync), `Uniform1ui`, `Uniform2ui`, `Uniform3ui`, `Uniform4ui`, `Uniform1uiv`, `Uniform2uiv`, `Uniform3uiv`, `Uniform4uiv`, `UniformMatrix2x3fv`, `UniformMatrix3x2fv`, `UniformMatrix2x4fv`, `UniformMatrix4x2fv`, `UniformMatrix3x4fv`, `UniformMatrix4x3fv`, `VertexAttribI4i`, `VertexAttribI4iv`, `VertexAttribI4ui`, `VertexAttribI4uiv`, `VertexAttribIPointer`, `DrawRangeElements`, `DrawBuffers`, `ClearBufferiv`, `ClearBufferuiv`, `ClearBufferfv`, `ClearBufferfi`, `CreateQuery`, `DeleteQuery`, `IsQuery` (sync), `BeginQuery`, `EndQuery`, `GetQuery` (sync), `GetQueryObjectui` (sync), `CreateSampler`, `DeleteSampler`, `IsSampler` (sync), `BindSampler`, `SamplerParameteri`, `SamplerParameterf`, `GetSamplerParameterf` (sync), `GetSamplerParameteri` (sync), `FenceSync` (sync), `IsSync` (sync), `DeleteSync`, `ClientWaitSync` (sync), `WaitSync`, `GetSynci` (sync), `CreateTransformFeedback`, `DeleteTransformFeedback`, `IsTransformFeedback` (sync), `BindTransformFeedback`, `BeginTransformFeedback`, `EndTransformFeedback`, `TransformFeedbackVaryings`, `GetTransformFeedbackVarying` (sync), `PauseTransformFeedback`, `ResumeTransformFeedback`, `BindBufferBase`, `BindBufferRange`, `GetUniformIndices` (sync), `GetActiveUniforms` (sync), `GetUniformBlockIndex` (sync), `GetActiveUniformBlockName` (sync), `UniformBlockBinding`, `GetActiveUniformBlockiv` (sync), `GetTranslatedShaderSourceANGLE` (sync), `DrawBuffersEXT`, `CreateQueryEXT`, `DeleteQueryEXT`, `IsQueryEXT` (sync), `BeginQueryEXT`, `EndQueryEXT`, `QueryCounterEXT`, `GetQueryiEXT` (sync), `GetQueryObjectiEXT` (sync), `GetQueryObjectui64EXT` (sync), `GetInteger64EXT` (sync), `EnableiOES`, `DisableiOES`, `BlendEquationiOES`, `BlendEquationSeparateiOES`, `BlendFunciOES`, `BlendFuncSeparateiOES`, `ColorMaskiOES`, `DrawArraysInstancedBaseInstanceANGLE`, `DrawElementsInstancedBaseVertexBaseInstanceANGLE`, `ClipControlEXT`, `ProvokingVertexANGLE`, `PolygonModeANGLE`, `PolygonOffsetClampEXT`, `RenderbufferStorageMultisampleANGLE`, `GetInternalformativ` (sync), `SetDrawingBufferColorSpace`, `CreateExternalImage`, `DeleteExternalImage`, `BindExternalImage`, `CreateExternalSync`, `DeleteExternalSync`, `EnableRequiredWebXRExtensions` (sync), `AddFoveation` (sync), `EnableFoveation`, `DisableFoveation`, `FramebufferDiscard`, `FramebufferResolveRenderbuffer`

## `RemoteImageBuffer` - WebContent -> GPU

`GPUProcess/graphics/RemoteImageBuffer.messages.in` - stream - direction: annotated

`GetPixelBuffer` (sync), `GetPixelBufferWithNewMemory` (sync), `PutPixelBuffer`, `GetShareableBitmap` (sync), `FilteredNativeImage` (sync), `ConvertToLuminanceMask`, `TransformToColorSpace`, `FlushContext`, `FlushContextSync` (sync), `DynamicContentScalingDisplayList` (sync)

## `RemoteImageBufferSet` - WebContent -> GPU

`GPUProcess/graphics/RemoteImageBufferSet.messages.in` - stream - direction: annotated

`UpdateConfiguration`, `EndPrepareForDisplay`, `DynamicContentScalingDisplayList` (sync)

## `RemoteImageDecoderAVFProxy` - WebContent -> GPU

`GPUProcess/media/RemoteImageDecoderAVFProxy.messages.in` - direction: annotated

`CreateDecoder` (sync), `DeleteDecoder`, `SetExpectedContentSize`, `SetData` (sync), `CreateFrameImageAtIndex` (sync), `ClearFrameBufferCache`

## `RemoteLegacyCDMFactoryProxy` - WebContent -> GPU

`GPUProcess/media/RemoteLegacyCDMFactoryProxy.messages.in` - direction: annotated

`CreateCDM` (sync), `SupportsKeySystem` (sync), `RemoveSession`

## `RemoteLegacyCDMProxy` - WebContent -> GPU

`GPUProcess/media/RemoteLegacyCDMProxy.messages.in` - direction: annotated

`SupportsMIMEType` (sync), `CreateSession` (sync), `SetPlayerId`

## `RemoteLegacyCDMSessionProxy` - WebContent -> GPU

`GPUProcess/media/RemoteLegacyCDMSessionProxy.messages.in` - direction: annotated

`GenerateKeyRequest` (sync), `ReleaseKeys`, `Update` (sync), `CachedKeyForKeyID` (sync)

## `RemoteMediaEngineConfigurationFactoryProxy` - WebContent -> GPU

`GPUProcess/media/RemoteMediaEngineConfigurationFactoryProxy.messages.in` - direction: annotated

`CreateDecodingConfiguration`, `CreateEncodingConfiguration`

## `RemoteMediaPlayerManagerProxy` - WebContent -> GPU

`GPUProcess/media/RemoteMediaPlayerManagerProxy.messages.in` - direction: annotated

`CreateMediaPlayer`, `DeleteMediaPlayer`, `GetSupportedTypes` (sync), `SupportsTypeAndCodecs` (sync), `SupportsKeySystem` (sync)

## `RemoteMediaPlayerProxy` - WebContent -> GPU

`GPUProcess/media/RemoteMediaPlayerProxy.messages.in` - direction: annotated

`PrepareForPlayback`, `Load`, `LoadMediaSource`, `CancelLoad`, `PrepareToPlay`, `Play`, `Pause`, `SetVolume`, `SetMuted`, `SeekToTarget`, `SetPreload`, `SetPrivateBrowsingMode`, `SetPreservesPitch`, `SetPitchCorrectionAlgorithm`, `PrepareForRendering`, `SetPageIsVisible`, `SetShouldMaintainAspectRatio`, `AcceleratedRenderingStateChanged`, `SetShouldDisableSleep`, `SetRate`, `DidLoadingProgress`, `UpdateVideoFullscreenInlineImage`, `SetVideoFullscreenMode`, `SetVideoFullscreenGravity`, `VideoFullscreenStandbyChanged`, `SetBufferingPolicy`, `SetPresentationSize`, `SetVideoLayerSizeFenced`, `SetWirelessVideoPlaybackDisabled`, `SetWirelessPlaybackTarget`, `SetShouldPlayToPlaybackTarget`, `SetLegacyCDMSession`, `KeyAdded`, `CdmInstanceAttached`, `CdmInstanceDetached`, `AttemptToDecryptWithInstance`, `SetShouldContinueAfterKeyNeeded`, `BeginSimulatedHDCPError`, `EndSimulatedHDCPError`, `NotifyActiveSourceBuffersChanged`, `ApplicationWillResignActive`, `ApplicationDidBecomeActive`, `NotifyTrackModeChanged`, `TracksChanged`, `AudioTrackSetEnabled`, `VideoTrackSetSelected`, `TextTrackSetMode`, `PerformTaskAtTime`, `IsCrossOrigin` (sync), `SetVideoPlaybackMetricsUpdateInterval`, `SetPreferredDynamicRangeMode`, `ErrorLog` (sync), `AccessLog` (sync), `CreateAudioSourceProvider`, `SetShouldEnableAudioSourceProvider`, `NativeImageForCurrentTime` (sync), `ColorSpace` (sync), `VideoFrameForCurrentTimeIfChanged` (sync), `PlayAtHostTime`, `PauseAtHostTime`, `StartVideoFrameMetadataGathering`, `StopVideoFrameMetadataGathering`, `PlayerContentBoxRectChanged`, `SetShouldDisableHDR`, `RequestHostingContextID`, `SetShouldCheckHardwareSupport`, `SetDefaultSpatialTrackingLabel`, `SetSpatialTrackingLabel`, `AudioOutputDeviceChanged`, `IsInFullscreenOrPictureInPictureChanged`

## `RemoteMediaRecorderPrivateWriterManager` - WebContent -> GPU

`GPUProcess/media/RemoteMediaRecorderPrivateWriterManager.messages.in` - direction: observed send sites

`Create`, `AddAudioTrack` (sync), `AddVideoTrack` (sync), `AllTracksAdded` (sync), `WriteFrames`, `Close`

## `RemoteMediaResourceManager` - WebContent -> GPU

`GPUProcess/media/RemoteMediaResourceManager.messages.in` - direction: annotated

`ResponseReceived`, `RedirectReceived`, `DataSent`, `DataReceived`, `AccessControlCheckFailed`, `LoadFailed`, `LoadFinished`

## `RemoteMediaSessionHelperProxy` - WebContent -> GPU

`GPUProcess/media/ios/RemoteMediaSessionHelperProxy.messages.in` - direction: annotated

`StartMonitoringWirelessRoutes`, `StopMonitoringWirelessRoutes`, `ProvidePresentingApplicationPID`

## `RemoteMediaSourceProxy` - WebContent -> GPU

`GPUProcess/media/RemoteMediaSourceProxy.messages.in` - direction: annotated

`AddSourceBuffer` (sync), `DurationChanged`, `BufferedChanged`, `SetMediaPlayerReadyState`, `SetTimeFudgeFactor`, `MarkEndOfStream`, `UnmarkEndOfStream`, `Shutdown`

## `RemotePipelineLayout` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemotePipelineLayout.messages.in` - stream - direction: annotated

`Destruct`, `SetLabel`

## `RemotePresentationContext` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemotePresentationContext.messages.in` - stream - direction: annotated

`Configure`, `Unconfigure`, `GetCurrentTexture`, `Present`

## `RemoteQuerySet` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteQuerySet.messages.in` - stream - direction: annotated

`Destroy`, `Destruct`, `SetLabel`

## `RemoteQueue` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteQueue.messages.in` - stream - direction: annotated

`Destruct`, `Submit`, `OnSubmittedWorkDone`, `WriteBuffer`, `WriteTexture`, `CopyExternalImageToTexture`, `SetLabel`

## `RemoteRemoteCommandListenerProxy` - WebContent -> GPU

`GPUProcess/media/RemoteRemoteCommandListenerProxy.messages.in` - direction: annotated

`UpdateSupportedCommands`

## `RemoteRenderBundle` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteRenderBundle.messages.in` - stream - direction: annotated

`Destruct`, `SetLabel`

## `RemoteRenderBundleEncoder` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteRenderBundleEncoder.messages.in` - stream - direction: annotated

`Destruct`, `SetPipeline`, `SetIndexBuffer`, `SetVertexBuffer`, `UnsetVertexBuffer`, `Draw`, `DrawIndexed`, `DrawIndirect`, `DrawIndexedIndirect`, `SetBindGroup`, `PushDebugGroup`, `PopDebugGroup`, `InsertDebugMarker`, `Finish`, `SetLabel`

## `RemoteRenderPassEncoder` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteRenderPassEncoder.messages.in` - stream - direction: annotated

`Destruct`, `SetPipeline`, `SetIndexBuffer`, `SetVertexBuffer`, `UnsetVertexBuffer`, `Draw`, `DrawIndexed`, `DrawIndirect`, `DrawIndexedIndirect`, `SetBindGroup`, `PushDebugGroup`, `PopDebugGroup`, `InsertDebugMarker`, `SetViewport`, `SetScissorRect`, `SetBlendConstant`, `SetStencilReference`, `BeginOcclusionQuery`, `EndOcclusionQuery`, `ExecuteBundles`, `End`, `SetLabel`

## `RemoteRenderPipeline` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteRenderPipeline.messages.in` - stream - direction: annotated

`Destruct`, `GetBindGroupLayout`, `SetLabel`

## `RemoteRenderingBackend` - WebContent -> GPU

`GPUProcess/graphics/RemoteRenderingBackend.messages.in` - stream - direction: annotated

`CreateImageBuffer`, `ReleaseImageBuffer`, `GetImageBufferResourceLimitsForTesting`, `DestroyGetPixelBufferSharedMemory`, `CacheNativeImage`, `CacheFont`, `CacheFontCustomPlatformData`, `CacheDecomposedGlyphs`, `CacheGradient`, `CacheFilter`, `ReleaseAllDrawingResources`, `ReleaseAllImageResources`, `ReleaseRenderingResource`, `CreateRemoteImageBufferSet`, `ReleaseRemoteImageBufferSet`, `PrepareImageBufferSetsForDisplay`, `PrepareImageBufferSetsForDisplaySync` (sync), `MarkSurfacesVolatile`, `FinalizeRenderingUpdate`, `Flush`, `MoveToSerializedBuffer`, `MoveToImageBuffer`, `DidDrawRemoteToPDF`, `CreateRemoteBarcodeDetector`, `ReleaseRemoteBarcodeDetector`, `GetRemoteBarcodeDetectorSupportedFormats`, `CreateRemoteFaceDetector`, `ReleaseRemoteFaceDetector`, `CreateRemoteTextDetector`, `ReleaseRemoteTextDetector`

## `RemoteSampleBufferDisplayLayer` - WebContent -> GPU

`GPUProcess/webrtc/RemoteSampleBufferDisplayLayer.messages.in` - direction: annotated

`SetLogIdentifier`, `UpdateDisplayMode`, `Flush`, `FlushAndRemoveImage`, `EnqueueVideoFrame`, `ClearVideoFrames`, `Play`, `Pause`, `SetSharedVideoFrameSemaphore`, `SetSharedVideoFrameMemory`, `SetShouldMaintainAspectRatio`

## `RemoteSampleBufferDisplayLayerManager` - WebContent -> GPU

`GPUProcess/webrtc/RemoteSampleBufferDisplayLayerManager.messages.in` - direction: annotated

`CreateLayer`, `ReleaseLayer`

## `RemoteSampler` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteSampler.messages.in` - stream - direction: annotated

`Destruct`, `SetLabel`

## `RemoteShaderModule` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteShaderModule.messages.in` - stream - direction: annotated

`CompilationInfo`, `SetLabel`, `Destruct`

## `RemoteSharedResourceCache` - WebContent -> GPU

`GPUProcess/RemoteSharedResourceCache.messages.in` - direction: annotated-on-main

`ReleaseSerializedImageBuffer`

## `RemoteSourceBufferProxy` - WebContent -> GPU

`GPUProcess/media/RemoteSourceBufferProxy.messages.in` - direction: annotated

`SetActive`, `CanSwitchToType` (sync), `SetMode`, `Append`, `Abort`, `ResetParserState`, `RemovedFromMediaSource`, `SetMediaSourceEnded`, `StartChangingType`, `AddTrackBuffer`, `ResetTrackBuffers`, `ClearTrackBuffers`, `SetAllTrackBuffersNeedRandomAccess`, `RemoveCodedFrames`, `EvictCodedFrames` (sync), `AsyncEvictCodedFrames`, `ReenqueueMediaIfNeeded`, `SetGroupStartTimestamp`, `SetGroupStartTimestampToEndTimestamp`, `SetShouldGenerateTimestamps`, `ResetTimestampOffsetInTrackBuffers`, `SetTimestampOffset`, `SetAppendWindowStart`, `SetAppendWindowEnd`, `SetMaximumBufferSize`, `ComputeSeekTime`, `SeekToTime`, `UpdateTrackIds`, `BufferedSamplesForTrackId`, `EnqueuedSamplesForTrackID`, `MemoryPressure`, `Detach`, `Attach`, `SetMaximumQueueDepthForTrackID`, `MinimumUpcomingPresentationTimeForTrackID` (sync)

## `RemoteTextDetector` - WebContent -> GPU

`GPUProcess/ShapeDetection/RemoteTextDetector.messages.in` - stream - direction: annotated

`Detect`

## `RemoteTexture` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteTexture.messages.in` - stream - direction: annotated

`CreateView`, `Destroy`, `Undestroy`, `Destruct`, `SetLabel`

## `RemoteTextureView` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteTextureView.messages.in` - stream - direction: annotated

`Destruct`, `SetLabel`

## `RemoteVideoFrameObjectHeap` - WebContent -> GPU

`GPUProcess/media/RemoteVideoFrameObjectHeap.messages.in` - direction: annotated

`GetVideoFrameBuffer`, `PixelBuffer` (sync), `SetSharedVideoFrameSemaphore`, `SetSharedVideoFrameMemory`, `ConvertFrameBuffer` (sync), `ReleaseVideoFrame`

## `RemoteWCLayerTreeHost` - WebContent -> GPU

`GPUProcess/graphics/wc/RemoteWCLayerTreeHost.messages.in` - non-Apple ports - direction: observed send sites

`Update`

## `RemoteXRBinding` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteXRBinding.messages.in` - stream - direction: annotated

`Destruct`, `CreateProjectionLayer`, `GetViewSubImage`

## `RemoteXRProjectionLayer` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteXRProjectionLayer.messages.in` - stream - direction: annotated

`StartFrame`, `EndFrame`, `Destruct`

## `RemoteXRSubImage` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteXRSubImage.messages.in` - stream - direction: annotated

`Destruct`, `GetColorTexture`, `GetDepthTexture`

## `RemoteXRView` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteXRView.messages.in` - stream - direction: annotated

`Destruct`

## `UserMediaCaptureManagerProxy` - WebContent -> GPU

`UIProcess/Cocoa/UserMediaCaptureManagerProxy.messages.in` - direction: annotated-on-main

`CreateMediaSourceForCaptureDeviceWithConstraints`, `StartProducingData`, `StopProducingData`, `RemoveSource`, `ApplyConstraints`, `TakePhoto`, `GetPhotoCapabilities`, `GetPhotoSettings`, `Clone`, `EndProducingData`, `SetShouldApplyRotation`, `SetIsInBackground`, `IsPowerEfficient` (sync)

## `NetworkBroadcastChannelRegistry` - WebContent -> Networking

`NetworkProcess/NetworkBroadcastChannelRegistry.messages.in` - direction: annotated

`RegisterChannel`, `UnregisterChannel`, `PostMessage`

## `NetworkConnectionToWebProcess` - WebContent -> Networking

`NetworkProcess/NetworkConnectionToWebProcess.messages.in` - direction: annotated

`ScheduleResourceLoad`, `PerformSynchronousLoad` (sync), `TestProcessIncomingSyncMessagesWhenWaitingForSyncReply` (sync), `LoadPing`, `RemoveLoadIdentifier`, `PageLoadCompleted`, `BrowsingContextRemoved`, `PrefetchDNS`, `SendH2Ping`, `PreconnectTo`, `IsResourceLoadFinished`, `StartDownload`, `ConvertMainResourceLoadToDownload`, `CookiesForDOM` (sync), `SetCookiesFromDOM`, `CookiesEnabledSync` (sync), `CookiesEnabled`, `CookieRequestHeaderFieldValue` (sync), `SetRawCookie`, `GetRawCookies` (sync), `DeleteCookie`, `DomCookiesForHost` (sync), `CookiesForDOMAsync`, `SetCookieFromDOMAsync`, `SubscribeToCookieChangeNotifications`, `UnsubscribeFromCookieChangeNotifications`, `RegisterInternalFileBlobURL`, `RegisterInternalBlobURL`, `RegisterBlobURL`, `RegisterInternalBlobURLOptionallyFileBacked`, `RegisterInternalBlobURLForSlice`, `UnregisterBlobURL`, `BlobType` (sync), `BlobSize` (sync), `WriteBlobsToTemporaryFilesForIndexedDB`, `RegisterBlobURLHandle`, `UnregisterBlobURLHandle`, `RegisterBlobPathForTesting`, `SetCaptureExtraNetworkLoadMetricsEnabled`, `CreateSocketChannel`, `ClearPageSpecificData`, `RemoveStorageAccessForFrame`, `LogUserInteraction`, `ResourceLoadStatisticsUpdated`, `HasStorageAccess`, `RequestStorageAccess`, `StorageAccessQuirkForTopFrameDomain`, `RequestStorageAccessUnderOpener`, `AddOriginAccessAllowListEntry`, `RemoveOriginAccessAllowListEntry`, `ResetOriginAccessAllowLists`, `GetNetworkLoadInformationResponse` (sync), `GetNetworkLoadIntermediateInformation` (sync), `TakeNetworkLoadInformationMetrics` (sync), `EstablishSWContextConnection`, `CloseSWContextConnection`, `PingPongForServiceWorkers`, `EstablishSharedWorkerContextConnection`, `CloseSharedWorkerContextConnection`, `CreateRTCProvider`, `ConnectToRTCDataChannelRemoteSource`, `CreateNewMessagePortChannel`, `EntangleLocalPortInThisProcessToRemote`, `MessagePortDisentangled`, `MessagePortClosed`, `TakeAllMessagesForPort`, `PostMessageToRemote`, `DidDeliverMessagePortMessages`, `RegisterURLSchemesAsCORSEnabled`, `SetCORSDisablingPatterns`, `GetProcessDisplayName`, `UpdateActivePages`, `SetResourceLoadSchedulingMode`, `PrioritizeResourceLoads`, `InstallMockContentFilter`, `UseRedirectionForCurrentNavigation`, `NavigatorSubscribeToPushService`, `NavigatorUnsubscribeFromPushService`, `NavigatorGetPushSubscription`, `NavigatorGetPushPermissionState`, `InitializeWebTransportSession`, `DestroyWebTransportSession`, `ClearFrameLoadRecordsForStorageAccess`, `LoadImageForDecoding`, `SetLoginStatus`, `IsLoggedIn`

## `NetworkMDNSRegister` - WebContent -> Networking

`NetworkProcess/webrtc/NetworkMDNSRegister.messages.in` - direction: annotated

`UnregisterMDNSNames`, `RegisterMDNSName`

## `NetworkRTCMonitor` - WebContent -> Networking

`NetworkProcess/webrtc/NetworkRTCMonitor.messages.in` - direction: annotated

`StartUpdatingIfNeeded`, `StopUpdating`

## `NetworkRTCProvider` - WebContent -> Networking

`NetworkProcess/webrtc/NetworkRTCProvider.messages.in` - direction: annotated

`CreateUDPSocket`, `CreateClientTCPSocket`, `CreateResolver`, `StopResolver`, `GetInterfaceName`, `SendToSocket`, `CloseSocket`, `SetSocketOption`

## `NetworkResourceLoader` - WebContent -> Networking

`NetworkProcess/NetworkResourceLoader.messages.in` - direction: annotated

`ContinueDidReceiveResponse`

## `NetworkSocketChannel` - WebContent -> Networking

`NetworkProcess/NetworkSocketChannel.messages.in` - direction: annotated

`SendString`, `SendData`, `Close`

## `NetworkStorageManager` - WebContent -> Networking

`NetworkProcess/storage/NetworkStorageManager.messages.in` - direction: annotated

`Persisted`, `Persist`, `Estimate`, `FileSystemGetDirectory`, `CloseHandle`, `IsSameEntry`, `GetFileHandle`, `GetDirectoryHandle`, `RemoveEntry`, `Resolve`, `Move`, `GetFile`, `CreateSyncAccessHandle`, `CloseSyncAccessHandle`, `RequestNewCapacityForSyncAccessHandle`, `CreateWritable`, `CloseWritable`, `ExecuteCommandForWritable`, `GetHandleNames`, `GetHandle`, `ConnectToStorageArea`, `ConnectToStorageAreaSync` (sync), `CancelConnectToStorageArea`, `DisconnectFromStorageArea`, `SetItem`, `RemoveItem`, `Clear`, `OpenDatabase`, `OpenDBRequestCancelled`, `DeleteDatabase`, `EstablishTransaction`, `DatabaseConnectionPendingClose`, `DatabaseConnectionClosed`, `AbortOpenAndUpgradeNeeded`, `DidFireVersionChangeEvent`, `DidFinishHandlingVersionChangeTransaction`, `AbortTransaction`, `CommitTransaction`, `CreateObjectStore`, `DeleteObjectStore`, `RenameObjectStore`, `ClearObjectStore`, `CreateIndex`, `DeleteIndex`, `RenameIndex`, `PutOrAdd`, `GetRecord`, `GetAllRecords`, `GetCount`, `DeleteRecord`, `OpenCursor`, `IterateCursor`, `GetAllDatabaseNamesAndVersions`, `CacheStorageOpenCache`, `CacheStorageRemoveCache`, `CacheStorageAllCaches`, `CacheStorageReference`, `CacheStorageDereference`, `LockCacheStorage`, `UnlockCacheStorage`, `CacheStorageRetrieveRecords`, `CacheStorageRemoveRecords`, `CacheStoragePutRecords`, `CacheStorageClearMemoryRepresentation`, `CacheStorageRepresentation`, `ResetQuotaUpdatedBasedOnUsageForTesting`

## `NetworkTransportSession` - WebContent -> Networking

`NetworkProcess/webtransport/NetworkTransportSession.messages.in` - direction: annotated

`SendDatagram`, `CreateOutgoingUnidirectionalStream`, `CreateBidirectionalStream`, `StreamSendBytes`, `CancelReceiveStream`, `CancelSendStream`, `DestroyStream`, `Terminate`

## `RTCDataChannelRemoteManagerProxy` - WebContent -> Networking

`NetworkProcess/webrtc/RTCDataChannelRemoteManagerProxy.messages.in` - direction: annotated

`SendData`, `Close`, `ChangeReadyState`, `ReceiveData`, `DetectError`, `BufferedAmountIsDecreasing`

## `ServiceWorkerDownloadTask` - WebContent -> Networking

`NetworkProcess/ServiceWorker/ServiceWorkerDownloadTask.messages.in` - direction: annotated

`DidFail`, `DidReceiveData`, `DidReceiveFormData`, `DidFinish`

## `ServiceWorkerFetchTask` - WebContent -> Networking

`NetworkProcess/ServiceWorker/ServiceWorkerFetchTask.messages.in` - direction: annotated

`DidNotHandle`, `DidFail`, `DidReceiveRedirectResponse`, `DidReceiveResponse`, `DidReceiveData`, `DidReceiveFormData`, `DidFinish`, `UsePreload`, `WorkerClosed`

## `WebSWServerConnection` - WebContent -> Networking

`NetworkProcess/ServiceWorker/WebSWServerConnection.messages.in` - direction: annotated

`ScheduleJobInServer`, `ScheduleUnregisterJobInServer`, `FinishFetchingScriptInServer`, `AddServiceWorkerRegistrationInServer`, `RemoveServiceWorkerRegistrationInServer`, `PostMessageToServiceWorker`, `DidResolveRegistrationPromise`, `MatchRegistration`, `WhenRegistrationReady`, `GetRegistrations`, `RegisterServiceWorkerClient`, `UnregisterServiceWorkerClient`, `TerminateWorkerFromClient`, `WhenServiceWorkerIsTerminatedForTesting`, `SetThrottleState`, `StoreRegistrationsOnDisk`, `SubscribeToPushService`, `UnsubscribeFromPushService`, `GetPushSubscription`, `GetPushPermissionState`, `EnableNavigationPreload`, `DisableNavigationPreload`, `SetNavigationPreloadHeaderValue`, `GetNavigationPreloadState`, `StartBackgroundFetch`, `BackgroundFetchInformation`, `BackgroundFetchIdentifiers`, `AbortBackgroundFetch`, `MatchBackgroundFetch`, `RetrieveRecordResponse`, `RetrieveRecordResponseBody`, `AddCookieChangeSubscriptions`, `RemoveCookieChangeSubscriptions`, `CookieChangeSubscriptions`, `GetNotifications`

## `WebSWServerToContextConnection` - WebContent -> Networking

`NetworkProcess/ServiceWorker/WebSWServerToContextConnection.messages.in` - direction: annotated

`ScriptContextFailedToStart`, `ScriptContextStarted`, `DidFinishInstall`, `DidFinishActivation`, `SetServiceWorkerHasPendingEvents`, `SkipWaiting`, `WorkerTerminated`, `FindClientByVisibleIdentifier`, `MatchAll`, `Claim`, `Focus`, `Navigate`, `SetScriptResource`, `PostMessageToServiceWorkerClient`, `DidFailHeartBeatCheck`, `SetAsInspected`, `OpenWindow`, `ReportConsoleMessage`

## `WebSharedWorkerServerConnection` - WebContent -> Networking

`NetworkProcess/SharedWorker/WebSharedWorkerServerConnection.messages.in` - direction: annotated

`RequestSharedWorker`, `SharedWorkerObjectIsGoingAway`, `SuspendForBackForwardCache`, `ResumeForBackForwardCache`

## `WebSharedWorkerServerToContextConnection` - WebContent -> Networking

`NetworkProcess/SharedWorker/WebSharedWorkerServerToContextConnection.messages.in` - direction: annotated

`PostErrorToWorkerObject`, `SharedWorkerTerminated`

## `ModelConnectionToWebProcess` - WebContent -> Model

`ModelProcess/ModelConnectionToWebProcess.messages.in` - direction: annotated

`CreateVisibilityPropagationContextForPage`, `DestroyVisibilityPropagationContextForPage`, `ConfigureLoggingChannel`

## `ModelProcessModelPlayerManagerProxy` - WebContent -> Model

`ModelProcess/ModelProcessModelPlayerManagerProxy.messages.in` - direction: annotated-on-main

`CreateModelPlayer`, `DeleteModelPlayer`

## `ModelProcessModelPlayerProxy` - WebContent -> Model

`ModelProcess/cocoa/ModelProcessModelPlayerProxy.messages.in` - direction: annotated-on-main

`CreateLayer`, `LoadModel`, `SizeDidChange`, `SetBackgroundColor`, `SetEntityTransform`, `SetAutoplay`, `SetLoop`, `SetPlaybackRate`, `SetPaused`, `SetCurrentTime`, `SetEnvironmentMap`, `SetHasPortal`

## `AcceleratedSurfaceDMABuf` - UI -> WebContent

`WebProcess/WebPage/dmabuf/AcceleratedSurfaceDMABuf.messages.in` - non-Apple ports - direction: observed send sites

`ReleaseBuffer`, `FrameDone`

## `AuxiliaryProcess` - UI -> WebContent, GPU, Networking, Model

`Shared/AuxiliaryProcess.messages.in` - direction: manual: received by every auxiliary process; sent only from UIProcess/

`ShutDown`, `SetProcessSuppressionEnabled`, `MainThreadPing`, `PreferenceDidUpdate`, `DidReceiveMemoryPressureEvent`

## `DrawingArea` - UI -> WebContent

`WebProcess/WebPage/DrawingArea.messages.in` - direction: annotated

`UpdateGeometry`, `ForceUpdate`, `DidDiscardBackingStore`, `SetDeviceScaleFactor`, `DisplayDidRefresh`, `UpdateGeometry`, `SetColorSpace`, `SetViewExposedRect`, `AcceleratedAnimationDidStart`, `AcceleratedAnimationDidEnd`, `DispatchAfterEnsuringDrawing`, `UpdateGeometryWC`, `AdjustTransientZoom`, `CommitTransientZoom`

## `EventDispatcher` - UI -> WebContent

`WebProcess/WebPage/EventDispatcher.messages.in` - direction: annotated

`WheelEvent`, `TouchEvent`, `GestureEvent`, `DisplayDidRefresh`, `SetScrollingAccelerationCurve`, `PageScreenDidChange`

## `PlatformXRSystemProxy` - UI -> WebContent

`WebProcess/XR/PlatformXRSystemProxy.messages.in` - direction: annotated

`SessionDidEnd`, `SessionDidUpdateVisibilityState`

## `PlaybackSessionManager` - UI -> WebContent

`WebProcess/cocoa/PlaybackSessionManager.messages.in` - direction: annotated

`Play`, `Pause`, `TogglePlayState`, `BeginScrubbing`, `EndScrubbing`, `SeekToTime`, `FastSeek`, `BeginScanningForward`, `BeginScanningBackward`, `EndScanning`, `SetDefaultPlaybackRate`, `SetPlaybackRate`, `SelectAudioMediaOption`, `SelectLegibleMediaOption`, `HandleControlledElementIDRequest`, `TogglePictureInPicture`, `EnterFullscreen`, `ExitFullscreen`, `EnterInWindow`, `ExitInWindow`, `ToggleMuted`, `SetMuted`, `SetVolume`, `SetPlayingOnSecondScreen`, `SendRemoteCommand`, `SetSoundStageSize`, `SetSpatialTrackingLabel`

## `RemoteMediaSessionCoordinator` - UI -> WebContent

`WebProcess/MediaSession/RemoteMediaSessionCoordinator.messages.in` - direction: annotated

`SeekSessionToTime`, `PlaySession`, `PauseSession`, `SetSessionTrack`, `CoordinatorStateChanged`

## `RemoteObjectRegistry` - UI, WebContent -> WebContent, UI

`Shared/API/Cocoa/RemoteObjectRegistry.messages.in` - direction: manual: bidirectional UI <-> WebContent (injected-bundle remote objects)

`InvokeMethod`, `CallReplyBlock`, `ReleaseUnusedReplyBlock`

## `RemoteScrollingCoordinator` - UI -> WebContent

`WebProcess/WebPage/RemoteLayerTree/RemoteScrollingCoordinator.messages.in` - direction: annotated

`ScrollPositionChangedForNode`, `AnimatedScrollDidEndForNode`, `CurrentSnapPointIndicesChangedForNode`, `ScrollingStateInUIProcessChanged`, `ReceivedWheelEventWithPhases`, `StartDeferringScrollingTestCompletionForNode`, `StopDeferringScrollingTestCompletionForNode`, `ScrollingTreeNodeScrollbarVisibilityDidChange`, `ScrollingTreeNodeScrollbarMinimumThumbLengthDidChange`

## `RemoteWebInspectorUI` - UI -> WebContent

`WebProcess/Inspector/RemoteWebInspectorUI.messages.in` - direction: annotated

`Initialize`, `UpdateFindString`, `SetDiagnosticLoggingAvailable`, `ShowConsole`, `ShowResources`, `SendMessageToFrontend`

## `RemoteWebLockRegistry` - UI -> WebContent

`WebProcess/WebCoreSupport/RemoteWebLockRegistry.messages.in` - direction: annotated

`DidCompleteLockRequest`, `DidStealLock`

## `SpeechRecognitionRealtimeMediaSourceManager` - UI -> WebContent

`WebProcess/Speech/SpeechRecognitionRealtimeMediaSourceManager.messages.in` - direction: annotated

`CreateSource`, `DeleteSource`, `Start`, `Stop`

## `SystemSettingsManager` - UI -> WebContent

`WebProcess/glib/SystemSettingsManager.messages.in` - non-Apple ports - direction: observed send sites

`DidChange`

## `TextCheckingControllerProxy` - UI -> WebContent

`WebProcess/WebPage/Cocoa/TextCheckingControllerProxy.messages.in` - direction: annotated

`ReplaceRelativeToSelection`, `RemoveAnnotationRelativeToSelection`

## `UserMediaCaptureManager` - UI -> WebContent

`WebProcess/cocoa/UserMediaCaptureManager.messages.in` - direction: observed send sites

`SourceStopped`, `SourceMutedChanged`, `SourceSettingsChanged`, `SourceConfigurationChanged`, `ApplyConstraintsSucceeded`, `ApplyConstraintsFailed`

## `UserMediaCaptureManager` - UI -> WebContent

`WebProcess/glib/UserMediaCaptureManager.messages.in` - non-Apple ports - direction: observed send sites

`ValidateUserMediaRequestConstraints`, `GetMediaStreamDevices`

## `VideoPresentationManager` - UI -> WebContent

`WebProcess/cocoa/VideoPresentationManager.messages.in` - direction: annotated

`RequestFullscreenMode`, `RequestUpdateInlineRect`, `RequestVideoContentLayer`, `ReturnVideoContentLayer`, `DidSetupFullscreen`, `WillExitFullscreen`, `DidExitFullscreen`, `DidEnterFullscreen`, `FailedToEnterFullscreen`, `DidCleanupFullscreen`, `SetVideoLayerFrameFenced`, `SetVideoLayerGravityEnum`, `SetVideoFullscreenFrame`, `FullscreenModeChanged`, `FullscreenMayReturnToInline`, `RequestRouteSharingPolicyAndContextUID`, `EnsureUpdatedVideoDimensions`, `SetRequiresTextTrackRepresentation`, `SetTextTrackRepresentationBounds`

## `ViewGestureGeometryCollector` - UI -> WebContent

`WebProcess/WebPage/ViewGestureGeometryCollector.messages.in` - direction: annotated

`CollectGeometryForSmartMagnificationGesture`, `CollectGeometryForMagnificationGesture`, `SetRenderTreeSizeNotificationThreshold`

## `ViewUpdateDispatcher` - UI -> WebContent

`WebProcess/WebPage/ViewUpdateDispatcher.messages.in` - direction: annotated

`VisibleContentRectUpdate`

## `VisitedLinkTableController` - UI -> WebContent

`WebProcess/WebPage/VisitedLinkTableController.messages.in` - direction: annotated

`SetVisitedLinkTable`, `VisitedLinkStateChanged`, `AllVisitedLinkStateChanged`, `RemoveAllVisitedLinks`

## `WebAutomationSessionProxy` - UI -> WebContent

`WebProcess/Automation/WebAutomationSessionProxy.messages.in` - direction: annotated

`EvaluateJavaScriptFunction`, `ResolveChildFrameWithOrdinal`, `ResolveChildFrameWithNodeHandle`, `ResolveChildFrameWithName`, `ResolveParentFrame`, `ComputeElementLayout`, `GetComputedRole`, `GetComputedLabel`, `SelectOptionElement`, `SetFilesForInputFileUpload`, `TakeScreenshot`, `SnapshotRectForScreenshot`, `GetCookiesForFrame`, `DeleteCookie`

## `WebDeviceOrientationUpdateProvider` - UI -> WebContent

`WebProcess/WebCoreSupport/WebDeviceOrientationUpdateProvider.messages.in` - direction: annotated

`DeviceOrientationChanged`, `DeviceMotionChanged`

## `WebExtensionContextProxy` - UI -> WebContent

`WebProcess/Extensions/WebExtensionContextProxy.messages.in` - direction: annotated

`DispatchActionClickedEvent`, `DispatchAlarmsEvent`, `DispatchCommandsCommandEvent`, `DispatchCommandsChangedEvent`, `DispatchCookiesChangedEvent`, `AddInspectorPageIdentifier`, `AddInspectorBackgroundPageIdentifier`, `DispatchDevToolsExtensionPanelShownEvent`, `DispatchDevToolsExtensionPanelHiddenEvent`, `DispatchDevToolsNetworkNavigatedEvent`, `DispatchDevToolsPanelsThemeChangedEvent`, `SetBackgroundPageIdentifier`, `AddPopupPageIdentifier`, `AddTabPageIdentifier`, `DispatchMenusClickedEvent`, `UpdateGrantedPermissions`, `DispatchPermissionsEvent`, `DispatchPortMessageEvent`, `DispatchPortDisconnectEvent`, `DispatchRuntimeMessageEvent`, `DispatchRuntimeConnectEvent`, `DispatchRuntimeInstalledEvent`, `DispatchRuntimeStartupEvent`, `SetStorageAccessLevel`, `DispatchStorageChangedEvent`, `DispatchTabsCreatedEvent`, `DispatchTabsUpdatedEvent`, `DispatchTabsReplacedEvent`, `DispatchTabsDetachedEvent`, `DispatchTabsMovedEvent`, `DispatchTabsAttachedEvent`, `DispatchTabsActivatedEvent`, `DispatchTabsHighlightedEvent`, `DispatchTabsRemovedEvent`, `DispatchTestMessageEvent`, `DispatchWebNavigationEvent`, `ResourceLoadDidSendRequest`, `ResourceLoadDidPerformHTTPRedirection`, `ResourceLoadDidReceiveChallenge`, `ResourceLoadDidReceiveResponse`, `ResourceLoadDidCompleteWithError`, `DispatchWindowsEvent`

## `WebExtensionControllerProxy` - UI -> WebContent

`WebProcess/Extensions/WebExtensionControllerProxy.messages.in` - direction: annotated

`Load`, `Unload`

## `WebFullScreenManager` - UI -> WebContent

`WebProcess/FullScreen/WebFullScreenManager.messages.in` - direction: annotated

`RequestRestoreFullScreen`, `RequestExitFullScreen`, `DidEnterFullScreen`, `WillExitFullScreen`, `DidExitFullScreen`, `SetAnimatingFullScreen`, `SaveScrollPosition`, `RestoreScrollPosition`, `SetFullscreenInsets`, `SetFullscreenAutoHideDuration`

## `WebGeolocationManager` - UI -> WebContent

`WebProcess/Geolocation/WebGeolocationManager.messages.in` - direction: annotated-on-main

`DidChangePosition`, `DidFailToDeterminePosition`, `ResetPermissions`

## `WebInspector` - UI -> WebContent

`WebProcess/Inspector/WebInspector.messages.in` - direction: annotated

`Show`, `Close`, `SetAttached`, `ShowConsole`, `ShowResources`, `ShowMainResourceForFrame`, `StartPageProfiling`, `StopPageProfiling`, `StartElementSelection`, `StopElementSelection`, `SetFrontendConnection`

## `WebInspectorInterruptDispatcher` - UI -> WebContent

`WebProcess/Inspector/WebInspectorInterruptDispatcher.messages.in` - direction: annotated

`NotifyNeedDebuggerBreak`

## `WebInspectorUI` - UI -> WebContent

`WebProcess/Inspector/WebInspectorUI.messages.in` - direction: observed send sites

`EstablishConnection`, `UpdateConnection`, `AttachedBottom`, `AttachedRight`, `AttachedLeft`, `Detached`, `SetDockingUnavailable`, `SetIsVisible`, `UpdateFindString`, `SetDiagnosticLoggingAvailable`, `ShowConsole`, `ShowResources`, `ShowMainResourceForFrame`, `StartPageProfiling`, `StopPageProfiling`, `StartElementSelection`, `StopElementSelection`, `SendMessageToFrontend`, `EvaluateInFrontendForTesting`

## `WebInspectorUIExtensionController` - UI -> WebContent

`WebProcess/Inspector/WebInspectorUIExtensionController.messages.in` - direction: annotated

`RegisterExtension`, `UnregisterExtension`, `CreateTabForExtension`, `EvaluateScriptForExtension`, `ReloadForExtension`, `ShowExtensionTab`, `NavigateTabForExtension`, `EvaluateScriptInExtensionTab`

## `WebNotificationManager` - UI -> WebContent

`WebProcess/Notifications/WebNotificationManager.messages.in` - direction: observed send sites

`DidShowNotification`, `DidClickNotification`, `DidCloseNotifications`, `DidUpdateNotificationDecision`, `DidRemoveNotificationDecisions`

## `WebPage` - UI, Networking -> WebContent

`WebProcess/WebPage/WebPage.messages.in` - direction: annotated (exception comment)

`SetInitialFocus`, `SetActivityState`, `SetLayerHostingMode`, `SetBackgroundColor`, `AddConsoleMessage`, `EnqueueSecurityPolicyViolationEvent`, `SendReportToEndpoints`, `NotifyReportObservers`, `TestProcessIncomingSyncMessagesWhenWaitingForSyncReply` (sync), `SetTopContentInsetFenced`, `SetTopContentInset`, `SetUnderlayColor`, `SetUnderPageBackgroundColorOverride`, `ViewWillStartLiveResize`, `ViewWillEndLiveResize`, `ExecuteEditCommandWithCallback`, `KeyEvent`, `MouseEvent`, `SetLastKnownMousePosition`, `SetSceneIdentifier`, `SetViewportConfigurationViewLayoutSize`, `SetDeviceOrientation`, `SetOverrideViewportArguments`, `DynamicViewportSizeUpdate`, `SetScreenIsBeingCaptured`, `SetInsertionPointColor`, `AttemptSyntheticClick`, `PotentialTapAtPosition`, `CommitPotentialTap`, `CancelPotentialTap`, `TapHighlightAtPosition`, `DidRecognizeLongPress`, `HandleDoubleTapForDoubleClickAtPoint`, `InspectorNodeSearchMovedToPosition`, `InspectorNodeSearchEndedAtPosition`, `BlurFocusedElement`, `SelectWithGesture`, `UpdateSelectionWithTouches`, `SelectWithTwoTouches`, `ExtendSelection`, `SelectWordBackward`, `ExtendSelectionForReplacement`, `MoveSelectionByOffset`, `SelectTextWithGranularityAtPoint`, `SelectPositionAtBoundaryWithDirection`, `MoveSelectionAtBoundaryWithDirection`, `SelectPositionAtPoint`, `BeginSelectionInDirection`, `UpdateSelectionWithExtentPoint`, `UpdateSelectionWithExtentPointAndBoundary`, `DidReleaseAllTouchPoints`, `ClearSelectionAfterTappingSelectionHighlightIfNeeded`, `RequestRVItemInCurrentSelectedRange`, `PrepareSelectionForContextMenuWithLocationInView`, `WillInsertFinalDictationResult`, `DidInsertFinalDictationResult`, `ReplaceDictatedText`, `ReplaceSelectedText`, `RequestAutocorrectionData`, `ApplyAutocorrection`, `SyncApplyAutocorrection` (sync), `HandleAutocorrectionContextRequest`, `RequestEvasionRectsAboveSelection`, `RequestPositionInformation`, `StartInteractionWithElementContextOrPosition`, `StopInteraction`, `PerformActionOnElement`, `PerformActionOnElements`, `FocusNextFocusedElement`, `AutofillLoginCredentials`, `SetFocusedElementValue`, `SetFocusedElementSelectedIndex`, `ApplicationWillResignActive`, `ApplicationDidEnterBackground`, `ApplicationDidFinishSnapshottingAfterEnteringBackground`, `ApplicationWillEnterForeground`, `ApplicationDidBecomeActive`, `ApplicationDidEnterBackgroundForMedia`, `ApplicationWillEnterForegroundForMedia`, `ContentSizeCategoryDidChange`, `GetSelectionContext`, `SetAllowsMediaDocumentInlinePlayback`, `HandleTwoFingerTapAtPoint`, `SetForceAlwaysUserScalable`, `GetRectsForGranularityWithSelectionOffset`, `GetRectsAtSelectionOffsetWithText`, `StoreSelectionForAccessibility`, `StartAutoscrollAtPosition`, `CancelAutoscroll`, `RequestFocusedElementInformation`, `HardwareKeyboardAvailabilityChanged`, `SetIsShowingInputViewForFocusedElement`, `UpdateSelectionWithDelta`, `RequestDocumentEditingContext`, `GenerateSyntheticEditingCommand`, `SetShouldRevealCurrentSelectionAfterInsertion`, `TextInputContextsInRect`, `FocusTextInputContextAndPlaceCaret`, `ClearServiceWorkerEntitlementOverride`, `RequestImageBitmap`, `SetControlledByAutomation`, `ConnectInspector`, `DisconnectInspector`, `SendMessageToTargetBackend`, `SetIndicating`, `DidBeginTouchPoint`, `TouchEvent`, `CancelPointer`, `TouchWithIdentifierWasRemoved`, `DidEndColorPicker`, `DidChooseColor`, `DidSelectDataListOption`, `DidCloseSuggestions`, `DidChooseDate`, `DidEndDateTimePicker`, `ScrollBy`, `CenterSelectionInVisibleArea`, `GoToBackForwardItem`, `GoToBackForwardItemWaitingForProcessLaunch`, `TryRestoreScrollPosition`, `LoadURLInFrame`, `LoadDataInFrame`, `LoadRequest`, `CreateProvisionalFrame`, `DestroyProvisionalFrame`, `LoadDidCommitInAnotherProcess`, `LoadRequestWaitingForProcessLaunch`, `LoadData`, `LoadSimulatedRequestAndResponse`, `LoadAlternateHTML`, `CreateRemoteSubframe`, `GetFrameInfo`, `GetFrameTree`, `DidFinishLoadInAnotherProcess`, `FrameWasRemovedInAnotherProcess`, `ProcessSyncDataChangedInAnotherProcess`, `TopDocumentSyncDataChangedInAnotherProcess`, `NavigateToPDFLinkWithSimulatedClick`, `GetPDFFirstPageSize`, `Reload`, `StopLoading`, `StopLoadingDueToProcessSwap`, `SetCurrentHistoryItemForReattach`, `DidRemoveBackForwardItem`, `UpdateWebsitePolicies`, `ClearSelection`, `RestoreSelectionInFocusedEditableElement`, `GetContentsAsString`, `GetContentsAsAttributedString`, `GetContentsAsMHTMLData`, `GetMainResourceDataOfFrame`, `GetResourceDataFromFrame`, `GetRenderTreeExternalRepresentation`, `GetSelectionOrContentsAsString`, `GetSelectionAsWebArchiveData`, `GetSourceForFrame`, `GetWebArchiveOfFrame`, `GetWebArchiveOfFrameWithFileName`, `RunJavaScriptInFrameInScriptWorld`, `GetAccessibilityTreeData`, `UpdateRenderingWithForcedRepaint`, `SelectAll`, `ScheduleFullEditorStateUpdate`, `PerformDictionaryLookupAtLocation`, `DetectDataInAllFrames`, `RemoveDataDetectedLinks`, `ChangeFont`, `ChangeFontAttributes`, `PreferencesDidChange`, `PreferencesDidChangeDuringDOMPrintOperation`, `SetUserAgent`, `SetHasCustomUserAgent`, `SetCustomTextEncodingName`, `SuspendActiveDOMObjectsAndAnimations`, `ResumeActiveDOMObjectsAndAnimations`, `Suspend`, `Resume`, `Close`, `TryClose`, `SetEditable`, `ValidateCommand`, `ExecuteEditCommand`, `IncreaseListLevel`, `DecreaseListLevel`, `ChangeListType`, `SetBaseWritingDirection`, `SetNeedsFontAttributes`, `RequestFontAttributesAtSelectionStart`, `DidRemoveEditCommand`, `ReapplyEditCommand`, `UnapplyEditCommand`, `DidSetPageZoomFactor`, `DidSetTextZoomFactor`, `WindowScreenDidChange`, `AccessibilitySettingsDidChange`, `DidScalePage`, `DidScalePageInViewCoordinates`, `DidScalePageRelativeToScrollPosition`, `DidScaleView`, `SetPluginScaleFactor`, `SetUseFixedLayout`, `SetFixedLayoutSize`, `SetDefaultUnobscuredSize`, `SetMinimumUnobscuredSize`, `SetMaximumUnobscuredSize`, `ListenForLayoutMilestones`, `SetSuppressScrollbarAnimations`, `SetEnableVerticalRubberBanding`, `SetEnableHorizontalRubberBanding`, `SetBackgroundExtendsBeyondPage`, `SetPaginationMode`, `SetPaginationBehavesLikeColumns`, `SetPageLength`, `SetGapBetweenPages`, `PostInjectedBundleMessage`, `FindString`, `FindStringIncludingImages`, `FindStringMatches`, `GetImageForFindMatch`, `SelectFindMatch`, `IndicateFindMatch`, `HideFindUI`, `CountStringMatches`, `ReplaceMatches`, `FindRectsForStringMatches`, `HideFindIndicator`, `FindTextRangesForStringMatches`, `ReplaceFoundTextRangeWithString`, `DecorateTextRangeWithStyle`, `ScrollTextRangeToVisible`, `ClearAllDecoratedFoundText`, `DidBeginTextSearchOperation`, `RequestRectForFoundTextRange`, `AddLayerForFindOverlay`, `RemoveLayerForFindOverlay`, `PerformDragControllerAction`, `PerformDragControllerAction`, `PerformDragOperation`, `DidStartDrag`, `DragEnded`, `DragCancelled`, `RequestDragStart`, `RequestAdditionalItemsForDragSession`, `InsertDroppedImagePlaceholders`, `DidConcludeDrop`, `InsertTextPlaceholder`, `RemoveTextPlaceholder`, `DidChangeSelectedIndexForActivePopupMenu`, `SetTextForActivePopupMenu`, `FailedToShowPopupMenu`, `DidDismissContextMenu`, `DidSelectItemFromActiveContextMenu`, `ContextMenuForKeyEvent`, `DidChooseFilesForOpenPanelWithDisplayStringAndIcon`, `DidChooseFilesForOpenPanel`, `DidCancelForOpenPanel`, `ExtendSandboxForFilesFromOpenPanel`, `AdvanceToNextMisspelling`, `ChangeSpellingToWord`, `DidFinishCheckingText`, `DidCancelCheckingText`, `UppercaseWord`, `LowercaseWord`, `CapitalizeWord`, `SetSmartInsertDeleteEnabled`, `DidReceiveGeolocationPermissionDecision`, `UserMediaAccessWasGranted`, `UserMediaAccessWasDenied`, `CaptureDevicesChanged`, `VoiceActivityDetected`, `SetOrientationForMediaCapture`, `SetMockCaptureDevicesInterrupted`, `MediaKeySystemWasGranted`, `MediaKeySystemWasDenied`, `RequestMediaPlaybackState`, `PauseAllMediaPlayback`, `SuspendAllMediaPlayback`, `ResumeAllMediaPlayback`, `SwipeAnimationDidStart`, `SwipeAnimationDidEnd`, `BeginPrinting`, `BeginPrintingDuringDOMPrintOperation`, `EndPrinting`, `EndPrintingDuringDOMPrintOperation`, `ComputePagesForPrinting`, `ComputePagesForPrintingDuringDOMPrintOperation`, `DrawRectToImage`, `DrawRectToImageDuringDOMPrintOperation`, `DrawPagesToPDF`, `DrawPagesToPDFDuringDOMPrintOperation`, `ComputePagesForPrintingiOS` (sync), `DrawToPDFiOS`, `DrawToImage`, `DrawToPDF`, `DrawRemoteToPDF`, `DrawPagesForPrinting`, `DrawPagesForPrintingDuringDOMPrintOperation`, `SetMediaVolume`, `SetMuted`, `SetMayStartMediaWhenInWindow`, `StopMediaCapture`, `SetCanRunBeforeUnloadConfirmPanel`, `SetCanRunModal`, `CancelComposition`, `DeleteSurrounding`, `CollapseSelectionInFrame`, `CopyLinkWithHighlight`, `BindRemoteAccessibilityFrames` (sync), `UpdateRemotePageAccessibilityOffset`, `ResolveAccessibilityHitTestForTesting`, `EnableAccessibility`, `WindowAndViewFramesChanged`, `SetMainFrameIsScrollable`, `RegisterUIProcessAccessibilityTokens`, `GetStringSelectionForPasteboard` (sync), `GetDataSelectionForPasteboard` (sync), `ReadSelectionFromPasteboard` (sync), `ReplaceSelectionWithPasteboardData`, `InsertMultiRepresentationHEIC`, `ShouldDelayWindowOrderingEvent` (sync), `SetTextAsync`, `InsertTextAsync`, `InsertDictatedTextAsync`, `AddDictationAlternative`, `DictationAlternativesAtSelection`, `ClearDictationAlternatives`, `HasMarkedText`, `GetMarkedRangeAsync`, `GetSelectedRangeAsync`, `CharacterIndexForPointAsync`, `FirstRectForCharacterRangeAsync`, `SetCompositionAsync`, `SetWritingSuggestion`, `ConfirmCompositionAsync`, `AttributedSubstringForCharacterRangeAsync`, `RequestAcceptsFirstMouse`, `SetCaretAnimatorType`, `SetCaretBlinkingSuspended`, `ReplaceImageForRemoveBackground`, `ShouldAllowRemoveBackground`, `SetAlwaysShowsHorizontalScroller`, `SetAlwaysShowsVerticalScroller`, `SetMinimumSizeForAutoLayout`, `SetSizeToContentAutoSizeMaximumSize`, `SetAutoSizingShouldExpandToViewHeight`, `SetViewportSizeForCSSViewportUnits`, `HandleAlternativeTextUIResult`, `WillStartUserTriggeredZooming`, `DidEndUserTriggeredZooming`, `SetScrollPinningBehavior`, `SetScrollbarOverlayStyle`, `GetBytecodeProfile`, `GetSamplingProfilerOutput`, `TakeSnapshot`, `PerformImmediateActionHitTestAtLocation`, `ImmediateActionDidUpdate`, `ImmediateActionDidCancel`, `ImmediateActionDidComplete`, `DataDetectorsDidPresentUI`, `DataDetectorsDidChangeUI`, `DataDetectorsDidHideUI`, `HandleAcceptedCandidate`, `SemanticContextDidChange`, `SetHeaderBannerHeight`, `SetFooterBannerHeight`, `DidBeginMagnificationGesture`, `DidEndMagnificationGesture`, `StartDeferringResizeEvents`, `FlushDeferredResizeEvents`, `StartDeferringScrollEvents`, `FlushDeferredScrollEvents`, `FlushDeferredDidReceiveMouseEvent`, `PerformHitTestForMouseEvent`, `SetUseColorAppearance`, `SetAccentColor`, `RequestActiveNowPlayingSessionInfo`, `SetShouldDispatchFakeMouseMoveEvents`, `PlaybackTargetSelected`, `PlaybackTargetAvailabilityDidChange`, `SetShouldPlayToPlaybackTarget`, `PlaybackTargetPickerWasDismissed`, `DidAcquirePointerLock`, `DidNotAcquirePointerLock`, `DidLosePointerLock`, `SetShouldScaleViewToFitDocument`, `SetUserInterfaceLayoutDirection`, `DidGetLoadDecisionForIcon`, `SetUseIconLoadingClient`, `GamepadActivity`, `AllowGamepadAccess`, `RegisterURLSchemeHandler`, `URLSchemeTaskWillPerformRedirection`, `URLSchemeTaskDidPerformRedirection`, `URLSchemeTaskDidReceiveResponse`, `URLSchemeTaskDidReceiveData`, `URLSchemeTaskDidComplete`, `SetIsSuspended`, `InsertAttachment`, `UpdateAttachmentAttributes`, `UpdateAttachmentThumbnail`, `UpdateAttachmentIcon`, `GetApplicationManifest`, `GetTextFragmentMatch`, `ZoomPDFIn`, `ZoomPDFOut`, `SavePDF`, `OpenPDFWithPreview`, `UpdateCurrentModifierState`, `SimulateDeviceOrientationChange`, `SpeakingErrorOccurred`, `BoundaryEventOccurred`, `VoicesDidChange`, `SetCanShowPlaceholder`, `WasLoadedWithDataTransferFromPrevalentResource`, `ClearLoadedSubresourceDomains`, `GetLoadedSubresourceDomains`, `SystemPreviewActionTriggered`, `SendMessageToWebProcessExtension`, `SendMessageToWebProcessExtensionWithReply`, `PreferredBufferFormatsDidChange`, `StartTextManipulations`, `CompleteTextManipulation`, `SetOverriddenMediaType`, `GetProcessDisplayName`, `UpdateCORSDisablingPatterns`, `SetIsTakingSnapshotsForApplicationSuspension`, `SetNeedsDOMWindowResizeEvent`, `SetHasResourceLoadClient`, `SetCanUseCredentialStorage`, `CreateAppHighlightInSelectedRange`, `RestoreAppHighlightsAndScrollToIndex`, `SetAppHighlightsVisibility`, `HandleWheelEvent`, `DispatchWheelEventWithoutScrolling`, `LastNavigationWasAppInitiated`, `CreateMediaSessionCoordinator`, `UpdateWithTextRecognitionResult`, `StartVisualTranslation`, `ScrollToRect`, `NavigateServiceWorkerClient`, `ModelInlinePreviewDidLoad`, `ModelInlinePreviewDidFailToLoad`, `SetIsWindowResizingEnabled`, `SetInteractionRegionsEnabled`, `GenerateTestReport`, `SetLinkDecorationFilteringData`, `SetAllowedQueryParametersForAdvancedPrivacyProtections`, `PauseAllAnimations`, `PlayAllAnimations`, `UseRedirectionForCurrentNavigation`, `UpdateFrameScrollingMode`, `UpdateFrameSize`, `DispatchLoadEventToFrameOwnerElement`, `FrameWasFocusedInAnotherProcess`, `RemotePostMessage`, `RenderTreeAsTextForTesting` (sync), `LayerTreeAsTextForTesting` (sync), `FrameTextForTesting` (sync), `RequestAllTextAndRects`, `RequestTargetedElement`, `RequestAllTargetableElements`, `RequestTextExtraction`, `ShouldDismissKeyboardAfterTapAtPoint`, `SetMediaEnvironment`, `WillBeginWritingToolsSession`, `DidBeginWritingToolsSession`, `ProofreadingSessionDidReceiveSuggestions`, `ProofreadingSessionDidUpdateStateForSuggestion`, `WillEndWritingToolsSession`, `DidEndWritingToolsSession`, `CompositionSessionDidReceiveTextWithReplacementRange`, `WritingToolsSessionDidReceiveAction`, `ProofreadingSessionSuggestionTextRectsInRootViewCoordinates`, `UpdateTextVisibilityForActiveWritingToolsSession`, `TextPreviewDataForActiveWritingToolsSession`, `SetSelectionForActiveWritingToolsSession`, `DecorateTextReplacementsForActiveWritingToolsSession`, `CreateTextIndicatorForTextAnimationID`, `UpdateUnderlyingTextVisibilityForTextAnimationID`, `IntelligenceTextAnimationsDidComplete`, `CreateTextIndicatorForElementWithID`, `TakeSnapshotForTargetedElement`, `ResetVisibilityAdjustmentsForTargetedElements`, `AdjustVisibilityForTargetedElements`, `NumberOfVisibilityAdjustmentRects`, `RemoteViewRectToRootView`, `RemoteViewPointToRootView`, `RemoteDictionaryPopupInfoToRootView`, `SetDefaultSpatialTrackingLabel`, `StartObservingNowPlayingMetadata`, `StopObservingNowPlayingMetadata`, `LoadAndDecodeImage`, `GetInformationFromImageData`, `CreateBitmapsFromImageData`, `DecodeImageData`, `FrameNameWasChangedInAnotherProcess`, `StartPlayingPredominantVideo`, `CloseCurrentTypingCommand`, `SimulateClickOverFirstMatchingTextInViewportWithUserInteraction`, `UpdateOpener`, `SetPresentingApplicationAuditTokenAndBundleIdentifier`

## `WebPageTesting` - UI -> WebContent

`WebProcess/WebPage/WebPageTesting.messages.in` - direction: annotated

`IsLayerTreeFrozen`, `SetPermissionLevel`, `IsEditingCommandEnabled` (sync), `ClearNotificationPermissionState`, `ClearWheelEventTestMonitor`, `ResetStateBetweenTests`, `SetTopContentInset`, `ClearCachedBackForwardListCounts`, `SetTracksRepaints`, `DisplayAndTrackRepaints`

## `WebPaymentCoordinator` - UI -> WebContent

`WebProcess/ApplePay/WebPaymentCoordinator.messages.in` - direction: annotated

`ValidateMerchant`, `DidAuthorizePayment`, `DidSelectShippingMethod`, `DidSelectShippingContact`, `DidSelectPaymentMethod`, `DidChangeCouponCode`, `DidCancelPaymentSession`

## `WebPermissionController` - UI -> WebContent

`WebProcess/WebCoreSupport/WebPermissionController.messages.in` - direction: annotated

`permissionChanged`

## `WebProcess` - UI -> WebContent

`WebProcess/WebProcess.messages.in` - direction: annotated

`InitializeWebProcess`, `SetWebsiteDataStoreParameters`, `CreateWebPage`, `PrewarmWithDomainInformation`, `SetCacheModel`, `RegisterURLSchemeAsEmptyDocument`, `RegisterURLSchemeAsSecure`, `RegisterURLSchemeAsBypassingContentSecurityPolicy`, `SetDomainRelaxationForbiddenForURLScheme`, `RegisterURLSchemeAsLocal`, `RegisterURLSchemeAsNoAccess`, `RegisterURLSchemeAsDisplayIsolated`, `RegisterURLSchemeAsCORSEnabled`, `RegisterURLSchemeAsCachePartitioned`, `RegisterURLSchemeAsCanDisplayOnlyIfCanRequest`, `RegisterURLSchemeAsWebExtension`, `SetDefaultRequestTimeoutInterval`, `SetAlwaysUsesComplexTextCodePath`, `SetDisableFontSubpixelAntialiasingForTesting`, `SetTrackingPreventionEnabled`, `ClearResourceLoadStatistics`, `UserPreferredLanguagesChanged`, `FullKeyboardAccessModeChanged`, `UpdateStorageAccessUserAgentStringQuirks`, `SetOptInCookiePartitioningEnabled`, `SetHasMouseDevice`, `SetHasStylusDevice`, `StartMemorySampler`, `StopMemorySampler`, `SetTextCheckerState`, `SetEnhancedAccessibility`, `BindAccessibilityFrameWithData`, `GarbageCollectJavaScriptObjects`, `SetJavaScriptGarbageCollectorTimerEnabled`, `SetInjectedBundleParameter`, `SetInjectedBundleParameters`, `HandleInjectedBundleMessage`, `FetchWebsiteData`, `DeleteWebsiteData`, `DeleteWebsiteDataForOrigins`, `DeleteWebsiteDataForOrigin`, `ReloadExecutionContextsForOrigin`, `DeleteAllCookies`, `SetHiddenPageDOMTimerThrottlingIncreaseLimit`, `SetMemoryCacheDisabled`, `SetEnabledServices`, `EnsureAutomationSessionProxy`, `DestroyAutomationSessionProxy`, `PrepareToSuspend`, `ProcessDidResume`, `BackgroundResponsivenessPing`, `SetInitialGamepads`, `GamepadConnected`, `GamepadDisconnected`, `EstablishRemoteWorkerContextConnectionToNetworkProcess`, `RegisterServiceWorkerClients`, `SetHasSuspendedPageProxy`, `SetIsInProcessCache`, `MarkIsNoLongerPrewarmed`, `GetActivePagesOriginsForTesting`, `SetScreenProperties`, `ScrollerStylePreferenceChanged`, `UserInterfaceIdiomDidChange`, `BacklightLevelDidChange`, `ColorPreferencesDidChange`, `IsJITEnabled`, `SetMediaMIMETypes`, `EnableRemoteWebInspector`, `AddMockMediaDevice`, `ClearMockMediaDevices`, `RemoveMockMediaDevice`, `SetMockMediaDeviceIsEphemeral`, `ResetMockMediaDevices`, `GrantUserMediaDeviceSandboxExtensions`, `RevokeUserMediaDeviceSandboxExtensions`, `ClearCurrentModifierStateForTesting`, `SetBackForwardCacheCapacity`, `ClearCachedPage`, `SendMessageToWebProcessExtension`, `SeedResourceLoadStatisticsForTesting`, `SetThirdPartyCookieBlockingMode`, `SetDomainsWithUserInteraction`, `SetDomainsWithCrossPageStorageAccess`, `SendResourceLoadStatisticsDataImmediately`, `UpdateDomainsWithStorageAccessQuirks`, `UpdateScriptTelemetryFilter`, `GrantAccessToAssetServices`, `RevokeAccessToAssetServices`, `SwitchFromStaticFontRegistryToUserFontRegistry`, `DisableURLSchemeCheckInDataDetectors`, `UnblockServicesRequiredByAccessibility`, `PowerSourceDidChange`, `SetUseSystemAppearanceForScrollbars`, `DidWriteToPasteboardAsynchronously`, `DisplayDidRefresh`, `SystemWillPowerOn`, `SystemWillSleep`, `SystemDidWake`, `ConsumeAudioComponentRegistrations`, `AccessibilityPreferencesDidChange`, `SetMediaAccessibilityPreferences`, `OpenDirectoryCacheInvalidated`, `ReleaseMemory`, `PostNotification`, `PostObserverNotification`, `GetNotifyStateForTesting`, `SetResourceMonitorContentRuleList`, `SetResourceMonitorContentRuleListAsync`, `RegisterAdditionalFonts`

## `WebScreenOrientationManager` - UI -> WebContent

`WebProcess/WebCoreSupport/WebScreenOrientationManager.messages.in` - direction: annotated

`OrientationDidChange`

## `WebSharedWorkerContextManagerConnection` - UI -> WebContent

`WebProcess/Storage/WebSharedWorkerContextManagerConnection.messages.in` - direction: annotated (exception comment)

`LaunchSharedWorker`, `PostConnectEvent`, `TerminateSharedWorker`, `UpdatePreferencesStore`, `SetUserAgent`, `Close`, `SuspendSharedWorker`, `ResumeSharedWorker`

## `WebSpeechRecognitionConnection` - UI -> WebContent

`WebProcess/WebCoreSupport/WebSpeechRecognitionConnection.messages.in` - direction: annotated

`DidReceiveUpdate`

## `WebUserContentController` - UI -> WebContent

`WebProcess/UserContent/WebUserContentController.messages.in` - direction: annotated

`AddContentWorlds`, `RemoveContentWorlds`, `AddUserScripts`, `RemoveUserScript`, `RemoveAllUserScripts`, `AddUserStyleSheets`, `RemoveUserStyleSheet`, `RemoveAllUserStyleSheets`, `AddUserScriptMessageHandlers`, `RemoveUserScriptMessageHandler`, `RemoveAllUserScriptMessageHandlersForWorlds`, `RemoveAllUserScriptMessageHandlers`, `AddContentRuleLists`, `RemoveContentRuleList`, `RemoveAllContentRuleLists`

## `GPUProcess` - UI -> GPU

`GPUProcess/GPUProcess.messages.in` - direction: annotated-on-main

`InitializeGPUProcess`, `CreateGPUConnectionToWebProcess`, `SharedPreferencesForWebProcessDidChange`, `UpdateGPUProcessPreferences`, `UpdateSandboxAccess`, `PrepareToSuspend`, `ProcessDidResume`, `AddSession`, `RemoveSession`, `SetMockCaptureDevicesEnabled`, `SetOrientationForMediaCapture`, `RotationAngleForCaptureDeviceChanged`, `UpdateCaptureAccess`, `UpdateCaptureOrigin`, `AddMockMediaDevice`, `ClearMockMediaDevices`, `RemoveMockMediaDevice`, `SetMockMediaDeviceIsEphemeral`, `ResetMockMediaDevices`, `SetMockCaptureDevicesInterrupted`, `TriggerMockCaptureConfigurationChange`, `SetShouldListenToVoiceActivity`, `EnableMicrophoneMuteStatusAPI`, `SetUseSCContentSharingPicker`, `SetScreenProperties`, `PromptForGetDisplayMedia`, `CancelGetDisplayMediaPrompt`, `RequestBitmapImageForCurrentTime`, `OpenDirectoryCacheInvalidated`, `ConsumeAudioComponentRegistrations`, `EnablePowerLogging`, `UserPreferredLanguagesChanged`, `WebProcessConnectionCountForTesting`, `ResolveBookmarkDataForCacheDirectory`, `WebXRPromptAccepted`, `SetPresentingApplicationAuditToken`, `RequestSharedSimulationConnection`

## `AuthenticationManager` - UI -> Networking

`NetworkProcess/Authentication/AuthenticationManager.messages.in` - direction: annotated-on-main

`CompleteAuthenticationChallenge`

## `LegacyCustomProtocolManager` - UI -> Networking

`NetworkProcess/CustomProtocols/LegacyCustomProtocolManager.messages.in` - direction: annotated-on-main

`DidFailWithError`, `DidLoadData`, `DidReceiveResponse`, `DidFinishLoading`, `WasRedirectedToRequest`, `RegisterScheme`, `UnregisterScheme`

## `NetworkContentRuleListManager` - UI -> Networking

`NetworkProcess/NetworkContentRuleListManager.messages.in` - direction: annotated-on-main

`Remove`, `AddContentRuleLists`, `RemoveContentRuleList`, `RemoveAllContentRuleLists`

## `NetworkProcess` - UI -> Networking

`NetworkProcess/NetworkProcess.messages.in` - direction: annotated-on-main

`InitializeNetworkProcess`, `CreateNetworkConnectionToWebProcess`, `SharedPreferencesForWebProcessDidChange`, `AddAllowedFirstPartyForCookies`, `SetIgnoreTLSErrors`, `UserPreferredLanguagesChanged`, `SetNetworkProxySettings`, `PrefetchDNS`, `SetPersistentCredentialStorageEnabled`, `SetNetworkProxySettings`, `AddWebsiteDataStore`, `DestroySession`, `EnsureSessionWithDataStoreIdentifierRemoved`, `FetchWebsiteData`, `DeleteWebsiteData`, `DeleteWebsiteDataForOrigins`, `RenameOriginInWebsiteData`, `WebsiteDataOriginDirectoryForTesting`, `DownloadRequest`, `ResumeDownload`, `CancelDownload`, `PublishDownloadProgress`, `PublishDownloadProgress`, `DataTaskWithRequest`, `CancelDataTask`, `ApplicationDidEnterBackground`, `ApplicationWillEnterForeground`, `FlushCookies`, `AllowSpecificHTTPSCertificateForHost`, `AllowTLSCertificateChainForLocalPCMTesting`, `SetCacheModel`, `SetCacheModelSynchronouslyForTesting` (sync), `ProcessWillSuspendImminentlyForTestingSync` (sync), `PrepareToSuspend`, `ProcessDidResume`, `NotifyMediaStreamingActivity`, `PreconnectTo`, `SetInspectionForServiceWorkersAllowed`, `ClearPrevalentResource`, `ClearUserInteraction`, `DumpResourceLoadStatistics`, `SetTrackingPreventionEnabled`, `UpdateStorageAccessPromptQuirks`, `SetResourceLoadStatisticsLogTestingEvent`, `UpdatePrevalentDomainsToBlockCookiesFor`, `IsGrandfathered`, `IsPrevalentResource`, `IsVeryPrevalentResource`, `SetLastSeen`, `MergeStatisticForTesting`, `InsertExpiredStatisticForTesting`, `SetPrevalentResource`, `SetPrevalentResourceForDebugMode`, `IsResourceLoadStatisticsEphemeral`, `HadUserInteraction`, `IsRelationshipOnlyInDatabaseOnce`, `HasLocalStorage`, `GetAllStorageAccessEntries`, `IsRegisteredAsRedirectingTo`, `IsRegisteredAsSubFrameUnder`, `IsRegisteredAsSubresourceUnder`, `DomainIDExistsInDatabase`, `LogFrameNavigation`, `LogUserInteraction`, `ResetParametersToDefaultValues`, `ScheduleClearInMemoryAndPersistent`, `ScheduleCookieBlockingUpdate`, `ScheduleStatisticsAndDataRecordsProcessing`, `StatisticsDatabaseHasAllTables`, `SetCacheMaxAgeCapForPrevalentResources`, `SetGrandfathered`, `GetResourceLoadStatisticsDataSummary`, `SetGrandfatheringTime`, `SetMaxStatisticsEntries`, `SetMinimumTimeBetweenDataRecordsRemoval`, `SetPruneEntriesDownTo`, `SetShouldClassifyResourcesBeforeDataRecordsRemoval`, `SetResourceLoadStatisticsTimeAdvanceForTesting`, `SetIsRunningResourceLoadStatisticsTest`, `SetResourceLoadStatisticsDebugMode`, `SetVeryPrevalentResource`, `SetSubframeUnderTopFrameDomain`, `SetSubresourceUnderTopFrameDomain`, `SetSubresourceUniqueRedirectTo`, `SetSubresourceUniqueRedirectFrom`, `SetTimeToLiveUserInteraction`, `SetTopFrameUniqueRedirectTo`, `SetTopFrameUniqueRedirectFrom`, `ResetCacheMaxAgeCapForPrevalentResources`, `DidCommitCrossSiteLoadWithDataTransfer`, `SetCrossSiteLoadWithLinkDecorationForTesting`, `ResetCrossSiteLoadsWithLinkDecorationForTesting`, `GrantStorageAccessForTesting`, `DeleteCookiesForTesting`, `HasIsolatedSession`, `CloseITPDatabase`, `SetAppBoundDomainsForResourceLoadStatistics`, `SetManagedDomainsForResourceLoadStatistics`, `SetShouldDowngradeReferrerForTesting`, `SetThirdPartyCookieBlockingMode`, `SetShouldEnbleSameSiteStrictEnforcementForTesting`, `SetFirstPartyWebsiteDataRemovalModeForTesting`, `SetToSameSiteStrictCookiesForTesting`, `SetFirstPartyHostCNAMEDomainForTesting`, `SetThirdPartyCNAMEDomainForTesting`, `SetPrivateClickMeasurementDebugMode`, `SetBlobRegistryTopOriginPartitioningEnabled`, `SetShouldSendPrivateTokenIPCForTesting`, `SetOptInCookiePartitioningEnabled`, `SetSessionIsControlledByAutomation`, `RegisterURLSchemeAsSecure`, `RegisterURLSchemeAsBypassingContentSecurityPolicy`, `RegisterURLSchemeAsLocal`, `RegisterURLSchemeAsNoAccess`, `SyncLocalStorage`, `StoreServiceWorkerRegistrations`, `StorePrivateClickMeasurement`, `DumpPrivateClickMeasurement`, `ClearPrivateClickMeasurement`, `SetPrivateClickMeasurementOverrideTimerForTesting`, `MarkAttributedPrivateClickMeasurementsAsExpiredForTesting`, `SetPrivateClickMeasurementEphemeralMeasurementForTesting`, `SimulatePrivateClickMeasurementSessionRestart`, `SetPrivateClickMeasurementTokenPublicKeyURLForTesting`, `SetPrivateClickMeasurementTokenSignatureURLForTesting`, `SetPrivateClickMeasurementAttributionReportURLsForTesting`, `MarkPrivateClickMeasurementsAsExpiredForTesting`, `SetPCMFraudPreventionValuesForTesting`, `SetPrivateClickMeasurementAppBundleIDForTesting`, `ClosePCMDatabase`, `SetServiceWorkerFetchTimeoutForTesting` (sync), `ResetServiceWorkerFetchTimeoutForTesting` (sync), `TerminateIdleServiceWorkers`, `ResetQuota`, `SetOriginQuotaRatioEnabledForTesting`, `SetBackupExclusionPeriodForTesting`, `ResetStoragePersistedState`, `CloneSessionStorageForWebPage`, `DidIncreaseQuota`, `HasAppBoundSession`, `ClearAppBoundSession`, `DisableServiceWorkerEntitlement`, `ClearServiceWorkerEntitlementOverride`, `UpdateBundleIdentifier`, `ClearBundleIdentifier`, `AppPrivacyReportTestingData`, `ClearAppPrivacyReportTestingData`, `AddWebPageNetworkParameters`, `RemoveWebPageNetworkParameters`, `CountNonDefaultSessionSets`, `AllowFileAccessFromWebProcess`, `AllowFilesAccessFromWebProcess`, `TerminateRemoteWorkerContextConnectionWhenPossible`, `RunningOrTerminatingServiceWorkerCountForTesting`, `GetPendingPushMessage`, `GetPendingPushMessages`, `ProcessPushMessage`, `ProcessNotificationEvent`, `GetAllBackgroundFetchIdentifiers`, `GetBackgroundFetchState`, `AbortBackgroundFetch`, `PauseBackgroundFetch`, `ResumeBackgroundFetch`, `ClickBackgroundFetch`, `SetPushAndNotificationsEnabledForOrigin`, `RemovePushSubscriptionsForOrigin`, `HasPushSubscriptionForTesting`, `SetEmulatedConditions`, `ClearProxyConfigData`, `SetProxyConfigData`, `SetStorageSiteValidationEnabled`, `SetPersistedDomains`, `GetAppBadgeForTesting`, `FetchLocalStorage`, `RestoreLocalStorage`, `FetchSessionStorage`, `RestoreSessionStorage`, `SetShouldRelaxThirdPartyCookieBlockingForPage`

## `WebCookieManager` - UI -> Networking

`NetworkProcess/Cookies/WebCookieManager.messages.in` - direction: annotated-on-main

`GetHostnamesWithCookies`, `DeleteCookiesForHostnames`, `DeleteAllCookies`, `SetCookie`, `SetCookies`, `GetAllCookies`, `GetCookies`, `DeleteCookie`, `DeleteAllCookiesModifiedSince`, `SetHTTPCookieAcceptPolicy`, `GetHTTPCookieAcceptPolicy`, `StartObservingCookieChanges`, `StopObservingCookieChanges`, `ReplaceCookies`, `SetCookiePersistentStorage`

## `ModelProcess` - UI -> Model

`ModelProcess/ModelProcess.messages.in` - direction: annotated-on-main

`InitializeModelProcess`, `CreateModelConnectionToWebProcess`, `SharedPreferencesForWebProcessDidChange`, `PrepareToSuspend`, `ProcessDidResume`, `AddSession`, `RemoveSession`, `WebProcessConnectionCountForTesting`

## `GPUProcessConnection` - GPU -> WebContent

`WebProcess/GPU/GPUProcessConnection.messages.in` - direction: annotated

`DidInitialize`, `DidReceiveRemoteCommand`, `BeginRoutingArbitrationWithCategory`, `EndRoutingArbitration`, `ResetAudioMediaStreamTrackRendererInternalUnit`

## `LibWebRTCCodecs` - GPU -> WebContent

`WebProcess/GPU/webrtc/LibWebRTCCodecs.messages.in` - direction: annotated

`FailedDecoding`, `CompletedDecoding`, `CompletedDecodingCV`, `CompletedEncoding`, `SetEncodingConfiguration`

## `MediaPlayerPrivateRemote` - GPU -> WebContent

`WebProcess/GPU/media/MediaPlayerPrivateRemote.messages.in` - direction: annotated

`NetworkStateChanged`, `ReadyStateChanged`, `FirstVideoFrameAvailable`, `VolumeChanged`, `MuteChanged`, `Seeked`, `TimeChanged`, `DurationChanged`, `RateChanged`, `PlaybackStateChanged`, `EngineFailedToLoad`, `UpdateCachedState`, `UpdatePlaybackQualityMetrics`, `CharacteristicChanged`, `SizeChanged`, `RenderingModeChanged`, `CurrentTimeChanged`, `AddRemoteAudioTrack`, `RemoveRemoteAudioTrack`, `RemoteAudioTrackConfigurationChanged`, `AddRemoteVideoTrack`, `RemoveRemoteVideoTrack`, `RemoteVideoTrackConfigurationChanged`, `AddRemoteTextTrack`, `RemoveRemoteTextTrack`, `RemoteTextTrackConfigurationChanged`, `ParseWebVTTFileHeader`, `ParseWebVTTCueData`, `ParseWebVTTCueDataStruct`, `AddDataCue`, `AddDataCueWithType`, `UpdateDataCue`, `RemoveDataCue`, `AddGenericCue`, `UpdateGenericCue`, `RemoveGenericCue`, `RequestResource`, `RemoveResource`, `SendH2Ping`, `ResourceNotSupported`, `ActiveSourceBuffersChanged`, `WaitingForKeyChanged`, `InitializationDataEncountered`, `MediaPlayerKeyNeeded`, `CurrentPlaybackTargetIsWirelessChanged`, `GetRawCookies`, `PushVideoFrameMetadata`, `LayerHostingContextIdChanged`, `CommitAllTransactions`

## `MediaSourcePrivateRemoteMessageReceiver` - GPU -> WebContent

`WebProcess/GPU/media/MediaSourcePrivateRemoteMessageReceiver.messages.in` - direction: annotated

`ProxyWaitForTarget`, `ProxySeekToTime`

## `RemoteAudioHardwareListener` - GPU -> WebContent

`WebProcess/GPU/media/RemoteAudioHardwareListener.messages.in` - direction: annotated

`AudioHardwareDidBecomeActive`, `AudioHardwareDidBecomeInactive`, `AudioOutputDeviceChanged`

## `RemoteAudioSession` - GPU -> WebContent

`WebProcess/GPU/media/RemoteAudioSession.messages.in` - direction: annotated

`ConfigurationChanged`, `BeginInterruptionRemote`, `EndInterruptionRemote`

## `RemoteAudioSourceProviderManager` - GPU -> WebContent

`WebProcess/GPU/media/RemoteAudioSourceProviderManager.messages.in` - direction: annotated

`AudioStorageChanged`, `AudioSamplesAvailable`

## `RemoteCDMInstance` - GPU -> WebContent

`WebProcess/GPU/media/RemoteCDMInstance.messages.in` - direction: annotated

`UnrequestedInitializationDataReceived`

## `RemoteCDMInstanceSession` - GPU -> WebContent

`WebProcess/GPU/media/RemoteCDMInstanceSession.messages.in` - direction: annotated

`UpdateKeyStatuses`, `SendMessage`, `SessionIdChanged`

## `RemoteCaptureSampleManager` - GPU -> WebContent

`WebProcess/cocoa/RemoteCaptureSampleManager.messages.in` - direction: annotated-on-main

`AudioStorageChanged`, `VideoFrameAvailable`, `VideoFrameAvailableCV`

## `RemoteGPUProxy` - GPU -> WebContent

`WebProcess/GPU/graphics/WebGPU/RemoteGPUProxy.messages.in` - direction: annotated

`WasCreated`

## `RemoteGraphicsContextGLProxy` - GPU -> WebContent

`WebProcess/GPU/graphics/RemoteGraphicsContextGLProxy.messages.in` - direction: annotated

`WasCreated`, `WasLost`, `addDebugMessage`

## `RemoteImageBufferProxy` - GPU -> WebContent

`WebProcess/GPU/graphics/RemoteImageBufferProxy.messages.in` - direction: annotated

`DidCreateBackend`

## `RemoteImageBufferSetProxy` - GPU -> WebContent

`WebProcess/GPU/graphics/RemoteImageBufferSetProxy.messages.in` - direction: annotated

`DidPrepareForDisplay`

## `RemoteImageDecoderAVFManager` - GPU -> WebContent

`WebProcess/GPU/media/RemoteImageDecoderAVFManager.messages.in` - direction: annotated

`EncodedDataStatusChanged`

## `RemoteLegacyCDMSession` - GPU -> WebContent

`WebProcess/GPU/media/RemoteLegacyCDMSession.messages.in` - direction: annotated

`SendMessage`, `SendError`

## `RemoteMediaSessionHelper` - GPU -> WebContent

`WebProcess/GPU/media/ios/RemoteMediaSessionHelper.messages.in` - direction: annotated-on-main

`ApplicationWillEnterForeground`, `ApplicationDidEnterBackground`, `ApplicationWillBecomeInactive`, `ApplicationDidBecomeActive`, `ExternalOutputDeviceAvailableDidChange`, `IsPlayingToAutomotiveHeadUnitDidChange`, `ActiveAudioRouteDidChange`, `ActiveVideoRouteDidChange`, `ActiveAudioRouteSupportsSpatialPlaybackDidChange`

## `RemoteRemoteCommandListener` - GPU -> WebContent

`WebProcess/GPU/media/RemoteRemoteCommandListener.messages.in` - direction: annotated

`DidReceiveRemoteControlCommand`

## `RemoteRenderingBackendProxy` - GPU -> WebContent

`WebProcess/GPU/graphics/RemoteRenderingBackendProxy.messages.in` - direction: annotated

`DidFinalizeRenderingUpdate`, `DidInitialize`, `DidMarkLayersAsVolatile`

## `RemoteVideoFrameObjectHeapProxyProcessor` - GPU -> WebContent

`WebProcess/GPU/webrtc/RemoteVideoFrameObjectHeapProxyProcessor.messages.in` - direction: annotated

`SetSharedVideoFrameSemaphore`, `SetSharedVideoFrameMemory`, `NewVideoFrameBuffer`, `NewConvertedVideoFrameBuffer`

## `SampleBufferDisplayLayer` - GPU -> WebContent

`WebProcess/GPU/webrtc/SampleBufferDisplayLayer.messages.in` - direction: annotated

`SetDidFail`

## `SourceBufferPrivateRemoteMessageReceiver` - GPU -> WebContent

`WebProcess/GPU/media/SourceBufferPrivateRemoteMessageReceiver.messages.in` - direction: annotated

`SourceBufferPrivateDidReceiveInitializationSegment`, `TakeOwnershipOfMemory`, `SourceBufferPrivateHighestPresentationTimestampChanged`, `SourceBufferPrivateBufferedChanged`, `SourceBufferPrivateDurationChanged`, `SourceBufferPrivateDidDropSample`, `SourceBufferPrivateDidReceiveRenderingError`, `SourceBufferPrivateEvictionDataChanged`, `SourceBufferPrivateDidAttach`

## `GPUProcessProxy` - GPU -> UI

`UIProcess/GPU/GPUProcessProxy.messages.in` - direction: annotated-on-main

`DidCreateContextForVisibilityPropagation`, `SetHasVP9HardwareDecoder`, `SetHasAV1HardwareDecoder`, `VoiceActivityDetected`, `StartMonitoringCaptureDeviceRotation`, `StopMonitoringCaptureDeviceRotation`, `MicrophoneMuteStatusChanged`, `StatusBarWasTapped`, `ProcessIsReadyToExit`, `TerminateWebProcess`, `DidDrawRemoteToPDF`

## `LibWebRTCNetwork` - Networking -> WebContent

`WebProcess/Network/webrtc/LibWebRTCNetwork.messages.in` - direction: annotated

`SignalReadPacket`, `SignalSentPacket`, `SignalAddressReady`, `SignalConnect`, `SignalClose`, `SignalUsedInterface`

## `NetworkProcessConnection` - Networking -> WebContent

`WebProcess/Network/NetworkProcessConnection.messages.in` - direction: annotated

`DidCacheResource`, `DidFinishPingLoad`, `DidFinishPreconnection`, `SetOnLineState`, `CookieAcceptPolicyChanged`, `UpdateCachedCookiesEnabled`, `CookiesAdded`, `CookiesDeleted`, `AllCookiesDeleted`, `ConnectToRTCDataChannelRemoteSource`, `MessagesAvailableForPort`, `BroadcastConsoleMessage`, `LoadCancelledDownloadRedirectRequestInFrame`

## `RTCDataChannelRemoteManager` - Networking -> WebContent

`WebProcess/Network/webrtc/RTCDataChannelRemoteManager.messages.in` - direction: annotated

`SendData`, `Close`, `ChangeReadyState`, `ReceiveData`, `DetectError`, `BufferedAmountIsDecreasing`

## `StorageAreaMap` - Networking -> WebContent

`WebProcess/WebStorage/StorageAreaMap.messages.in` - direction: annotated

`DispatchStorageEvent`, `ClearCache`

## `WebBroadcastChannelRegistry` - Networking -> WebContent

`WebProcess/WebCoreSupport/WebBroadcastChannelRegistry.messages.in` - direction: annotated

`PostMessageToRemote`

## `WebFileSystemStorageConnection` - Networking -> WebContent

`WebProcess/WebCoreSupport/WebFileSystemStorageConnection.messages.in` - direction: annotated

`InvalidateAccessHandle`

## `WebIDBConnectionToServer` - Networking -> WebContent

`WebProcess/Databases/IndexedDB/WebIDBConnectionToServer.messages.in` - direction: annotated

`DidDeleteDatabase`, `DidOpenDatabase`, `DidAbortTransaction`, `DidCommitTransaction`, `DidCreateObjectStore`, `DidDeleteObjectStore`, `DidRenameObjectStore`, `DidClearObjectStore`, `DidCreateIndex`, `DidDeleteIndex`, `DidRenameIndex`, `DidPutOrAdd`, `DidGetRecord`, `DidGetAllRecords`, `DidGetCount`, `DidDeleteRecord`, `DidOpenCursor`, `DidIterateCursor`, `FireVersionChangeEvent`, `DidStartTransaction`, `DidCloseFromServer`, `NotifyOpenDBRequestBlocked`, `DidGetAllDatabaseNamesAndVersions`

## `WebRTCMonitor` - Networking -> WebContent

`WebProcess/Network/webrtc/WebRTCMonitor.messages.in` - direction: annotated

`NetworksChanged`

## `WebRTCResolver` - Networking -> WebContent

`WebProcess/Network/webrtc/WebRTCResolver.messages.in` - direction: annotated

`SetResolvedAddress`, `ResolvedAddressError`

## `WebResourceLoader` - Networking -> WebContent

`WebProcess/Network/WebResourceLoader.messages.in` - direction: annotated

`WillSendRequest`, `SetWorkerStart`, `DidSendData`, `DidReceiveResponse`, `DidReceiveData`, `DidFinishResourceLoad`, `DidFailResourceLoad`, `DidFailServiceWorkerLoad`, `ServiceWorkerDidNotHandle`, `DidBlockAuthenticationChallenge`, `StopLoadingAfterXFrameOptionsOrContentSecurityPolicyDenied`, `DidReceiveResource`, `ContentFilterDidBlockLoad`

## `WebSWClientConnection` - Networking -> WebContent

`WebProcess/Storage/WebSWClientConnection.messages.in` - direction: annotated

`JobRejectedInServer`, `RegistrationJobResolvedInServer`, `StartScriptFetchForServer`, `UpdateRegistrationState`, `UpdateWorkerState`, `FireUpdateFoundEvent`, `SetRegistrationLastUpdateTime`, `SetRegistrationUpdateViaCache`, `NotifyClientsOfControllerChange`, `UpdateBackgroundFetchRegistration`, `SetSWOriginTableIsImported`, `SetSWOriginTableSharedMemory`, `PostMessageToServiceWorkerClient`, `SetServiceWorkerClientIsControlled`, `FocusServiceWorkerClient`, `NotifyRecordResponseBodyChunk`, `NotifyRecordResponseBodyEnd`

## `WebSWContextManagerConnection` - Networking, UI -> WebContent

`WebProcess/Storage/WebSWContextManagerConnection.messages.in` - direction: observed send sites

`InstallServiceWorker`, `UpdateAppInitiatedValue`, `StartFetch`, `CancelFetch`, `ContinueDidReceiveFetchResponse`, `PostMessageToServiceWorker`, `FireInstallEvent`, `FireActivateEvent`, `FirePushEvent`, `FireNotificationEvent`, `FireBackgroundFetchEvent`, `FireBackgroundFetchClickEvent`, `TerminateWorker`, `DidSaveScriptsToDisk`, `SetUserAgent`, `UpdatePreferencesStore`, `Close`, `SetThrottleState`, `SetInspectable`, `ConvertFetchToDownload`, `NavigationPreloadIsReady`, `NavigationPreloadFailed`, `UpdateRegistrationState`, `UpdateWorkerState`, `FireUpdateFoundEvent`, `SetRegistrationLastUpdateTime`, `SetRegistrationUpdateViaCache`

## `WebSharedWorkerObjectConnection` - Networking -> WebContent

`WebProcess/Storage/WebSharedWorkerObjectConnection.messages.in` - direction: annotated

`FetchScriptInClient`, `NotifyWorkerObjectOfLoadCompletion`, `PostErrorToWorkerObject`

## `WebSocketChannel` - Networking -> WebContent

`WebProcess/Network/WebSocketChannel.messages.in` - direction: annotated

`DidConnect`, `DidClose`, `DidReceiveText`, `DidReceiveBinaryData`, `DidReceiveMessageError`, `DidSendHandshakeRequest`, `DidReceiveHandshakeResponse`

## `WebTransportSession` - Networking -> WebContent

`WebProcess/Network/WebTransportSession.messages.in` - direction: annotated

`ReceiveDatagram`, `ReceiveIncomingUnidirectionalStream`, `ReceiveBidirectionalStream`, `StreamReceiveBytes`

## `DownloadProxy` - Networking -> UI

`UIProcess/Downloads/DownloadProxy.messages.in` - direction: annotated

`DidStart`, `DidReceiveAuthenticationChallenge`, `WillSendRequest`, `DecideDestinationWithSuggestedFilename`, `DidReceiveData`, `DidCreateDestination`, `DidFinish`, `DidFail`, `DidReceivePlaceholderURL`, `DidReceiveFinalURL`, `DidStartUpdatingProgress`

## `LegacyCustomProtocolManagerProxy` - Networking -> UI

`UIProcess/Network/CustomProtocols/LegacyCustomProtocolManagerProxy.messages.in` - direction: annotated-on-main

`StartLoading`, `StopLoading`

## `NetworkProcessProxy` - Networking -> UI

`UIProcess/Network/NetworkProcessProxy.messages.in` - direction: annotated-on-main

`DidReceiveAuthenticationChallenge`, `NegotiatedLegacyTLS`, `DidNegotiateModernTLS`, `DidBlockLoadToKnownTracker`, `TestProcessIncomingSyncMessagesWhenWaitingForSyncReply` (sync), `ProcessHasUnresponseServiceWorker`, `LogDiagnosticMessage`, `LogDiagnosticMessageWithResult`, `LogDiagnosticMessageWithValue`, `LogTestingEvent`, `RequestStorageAccessConfirm`, `DeleteWebsiteDataInUIProcessForRegistrableDomains`, `DidCommitCrossSiteLoadWithDataTransferFromPrevalentResource`, `SetDomainsWithUserInteraction`, `SetDomainsWithCrossPageStorageAccess`, `ContentExtensionRules`, `TerminateWebProcess`, `StartServiceWorkerBackgroundProcessing`, `EndServiceWorkerBackgroundProcessing`, `RequestBackgroundFetchPermission`, `NotifyBackgroundFetchChange`, `EstablishRemoteWorkerContextConnectionToNetworkProcess`, `RemoteWorkerContextConnectionNoLongerNeeded`, `RegisterRemoteWorkerClientProcess`, `UnregisterRemoteWorkerClientProcess`, `SetWebProcessHasUploads`, `GetAppBoundDomains`, `IncreaseQuota`, `ResourceLoadDidSendRequest`, `ResourceLoadDidPerformHTTPRedirection`, `ResourceLoadDidReceiveChallenge`, `ResourceLoadDidReceiveResponse`, `ResourceLoadDidCompleteWithError`, `DidAllowPrivateTokenUsageByThirdPartyForTesting`, `TriggerBrowsingContextGroupSwitchForNavigation`, `DidExceedMemoryLimit`, `GetWindowSceneAndBundleIdentifierForPaymentPresentation`, `GetPaymentCoordinatorEmbeddingUserAgent`, `DataTaskReceivedChallenge`, `DataTaskWillPerformHTTPRedirection`, `DataTaskDidReceiveResponse`, `DataTaskDidReceiveData`, `DataTaskDidCompleteWithError`, `OpenWindowFromServiceWorker`, `NavigateServiceWorkerClient`, `ReportConsoleMessage`, `CookiesDidChange`, `DeleteWebsiteDataInWebProcessesForOrigin`, `ReloadExecutionContextsForOrigin`, `WakeUpWebProcessForIPC`, `ReportNetworkIssue`

## `SecItemShimProxy` - Networking -> UI

`UIProcess/mac/SecItemShimProxy.messages.in` - direction: annotated-on-main

`SecItemRequestSync` (sync), `SecItemRequest`

## `PushClientConnection` - Networking, UI -> webpushd

`webpushd/PushClientConnection.messages.in` - direction: observed send sites

`SetPushAndNotificationsEnabledForOrigin`, `GetPendingPushMessage`, `GetPendingPushMessages`, `InitializeConnection`, `InjectPushMessageForTesting`, `InjectEncryptedPushMessageForTesting`, `SubscribeToPushService`, `UnsubscribeFromPushService`, `GetPushSubscription`, `GetPushPermissionState`, `IncrementSilentPushCount`, `RemoveAllPushSubscriptions`, `RemovePushSubscriptionsForOrigin`, `SetPublicTokenForTesting`, `GetPushTopicsForTesting`, `ShowNotification`, `GetNotifications`, `CancelNotification`, `RequestPushPermission`, `SetAppBadge`, `GetAppBadgeForTesting`, `SetProtocolVersionForTesting`

## `ModelProcessConnection` - Model -> WebContent

`WebProcess/Model/ModelProcessConnection.messages.in` - direction: annotated-on-main

`DidInitialize`

## `ModelProcessModelPlayer` - Model -> WebContent

`WebProcess/Model/ModelProcessModelPlayer.messages.in` - direction: annotated-on-main

`DidCreateLayer`, `DidFinishLoading`, `DidUpdateEntityTransform`, `DidUpdateAnimationPlaybackState`, `DidFinishEnvironmentMapLoading`

## `ModelProcessProxy` - Model -> UI

`UIProcess/Model/ModelProcessProxy.messages.in` - direction: annotated-on-main

`TerminateWebProcess`, `DidCreateContextForVisibilityPropagation`, `ProcessIsReadyToExit`, `RequestSharedSimulationConnection`

## `IPCConnectionTester` - test harness -> any process

`Shared/IPCConnectionTester.messages.in` - testing only - direction: manual: IPC testing API only

`AsyncMessage`, `SyncMessage` (sync)

## `IPCStreamTester` - test harness -> any process

`Shared/IPCStreamTester.messages.in` - testing only, stream - direction: manual: IPC testing API only

`SyncMessage` (sync), `SyncMessageNotStreamEncodableReply` (sync), `SyncMessageNotStreamEncodableBoth` (sync), `SyncMessageReturningSharedMemory1` (sync), `SyncMessageEmptyReply` (sync), `SyncCrashOnZero` (sync), `CheckAutoreleasePool` (sync), `AsyncPing`, `EmptyMessage`

## `IPCStreamTesterProxy` - test harness -> any process

`Shared/IPCStreamTesterProxy.messages.in` - testing only - direction: manual: IPC testing API only

`WasCreated`

## `IPCTester` - test harness -> any process

`Shared/IPCTester.messages.in` - testing only - direction: manual: IPC testing API only

`StartMessageTesting`, `StopMessageTesting` (sync), `CreateStreamTester`, `ReleaseStreamTester` (sync), `CreateConnectionTester`, `CreateConnectionTesterAndSendAsyncMessages`, `ReleaseConnectionTester` (sync), `SendSameSemaphoreBack`, `SendSemaphoreBackAndSignalProtocol`, `AsyncPing`, `SyncPing` (sync), `SyncPingEmptyReply` (sync), `SendAsyncMessageToReceiver`, `AsyncOptionalExceptionData`

## `IPCTesterReceiver` - test harness -> any process

`Shared/IPCTesterReceiver.messages.in` - testing only - direction: manual: IPC testing API only

`AsyncMessage`
