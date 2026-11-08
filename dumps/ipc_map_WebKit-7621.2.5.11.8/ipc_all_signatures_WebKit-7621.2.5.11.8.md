# WebKit IPC message signatures - WebKit-7621.2.5.11.8

Every message of every interface with its arguments and, after `->`, its reply. Generated from every `*.messages.in` in `Source/WebKit` with WebKit's own parser (code-generator test fixtures excluded).

## `AcceleratedBackingStoreDMABuf` - WebContent -> UI

`UIProcess/dmabuf/AcceleratedBackingStoreDMABuf.messages.in`

- `DidCreateBuffer(uint64_t id, WebCore::IntSize size, uint32_t format, Vector<UnixFileDescriptor> fds, Vector<uint32_t> offsets, Vector<uint32_t> strides, uint64_t modifier, WebKit::DMABufRendererBufferFormat::Usage usage)`
- `DidCreateBufferSHM(uint64_t id, WebCore::ShareableBitmapHandle handle)`
- `DidDestroyBuffer(uint64_t id)`
- `Frame(uint64_t id, WebCore::Region damage, UnixFileDescriptor syncFD)`

## `AudioSessionRoutingArbitratorProxy` - WebContent -> UI

`UIProcess/Media/AudioSessionRoutingArbitratorProxy.messages.in`

- `BeginRoutingArbitrationWithCategory(WebCore::AudioSessionCategory category) -> (WebCore::AudioSessionRoutingArbitrationError error, WebCore::AudioSessionRoutingArbitrationClient::DefaultRouteChanged defaultRouteChanged)`
- `EndRoutingArbitration()`

## `DigitalCredentialsCoordinatorProxy` - WebContent -> UI

`UIProcess/DigitalCredentials/DigitalCredentialsCoordinatorProxy.messages.in`

- `RequestDigitalCredential(WebCore::FrameIdentifier frameID, WebKit::FrameInfoData frameInfo, WebCore::DigitalCredentialRequestOptions options) -> (WebCore::ExceptionData exception)`
- `Cancel() -> ()`

## `DrawingAreaProxy` - WebContent -> UI

`UIProcess/DrawingAreaProxy.messages.in`

- `EnterAcceleratedCompositingMode(uint64_t backingStoreStateID, WebKit::LayerTreeContext context)`
- `UpdateAcceleratedCompositingMode(uint64_t backingStoreStateID, WebKit::LayerTreeContext context)`
- `DidFirstLayerFlush(uint64_t backingStoreStateID, WebKit::LayerTreeContext context)`
- `DispatchPresentationCallbacksAfterFlushingLayers(Vector<IPC::AsyncReplyID> callbackIDs)`
- `Update(uint64_t stateID, WebKit::UpdateInfo updateInfo)` (CanDispatchOutOfOrder, if USE(COORDINATED_GRAPHICS) || USE(TEXTURE_MAPPER))
- `ExitAcceleratedCompositingMode(uint64_t backingStoreStateID, WebKit::UpdateInfo updateInfo)` (if USE(COORDINATED_GRAPHICS) || USE(TEXTURE_MAPPER))

## `LogStream` - WebContent -> UI

`Shared/LogStream.messages.in`

- `LogOnBehalfOfWebContent(std::span<const uint8_t> logChannel, std::span<const uint8_t> logCategory, std::span<const uint8_t> logString, uint8_t logType)`

## `NotificationManagerMessageHandler` - WebContent -> UI, Networking

`Shared/Notifications/NotificationManagerMessageHandler.messages.in`

- `ShowNotification(WebCore::NotificationData notificationData, RefPtr<WebCore::NotificationResources> notificationResources) -> ()` (if ENABLE(NOTIFICATIONS))
- `CancelNotification(WebCore::SecurityOriginData origin, WTF::UUID notificationID)` (if ENABLE(NOTIFICATIONS))
- `ClearNotifications(Vector<WTF::UUID> notificationIDs)` (if ENABLE(NOTIFICATIONS))
- `DidDestroyNotification(WTF::UUID notificationID)` (if ENABLE(NOTIFICATIONS))
- `PageWasNotifiedOfNotificationPermission()` (if ENABLE(NOTIFICATIONS))
- `RequestPermission(WebCore::SecurityOriginData origin) -> (bool granted)` (if ENABLE(NOTIFICATIONS))
- `SetAppBadge(WebCore::SecurityOriginData origin, std::optional<uint64_t> badge)` (if ENABLE(WEB_PUSH_NOTIFICATIONS))
- `GetPermissionState(WebCore::SecurityOriginData origin) -> (WebCore::PushPermissionState permission)` (if ENABLE(WEB_PUSH_NOTIFICATIONS))
- `GetPermissionStateSync(WebCore::SecurityOriginData origin) -> (WebCore::PushPermissionState permission)` (sync, if ENABLE(WEB_PUSH_NOTIFICATIONS))

## `PlatformXRSystem` - WebContent -> UI

`UIProcess/XR/PlatformXRSystem.messages.in`

- `EnumerateImmersiveXRDevices() -> (Vector<WebKit::XRDeviceInfo> devicesInfos)`
- `RequestPermissionOnSessionFeatures(WebCore::SecurityOriginData origin, PlatformXR::SessionMode mode, Vector<PlatformXR::SessionFeature> granted, Vector<PlatformXR::SessionFeature> consentRequired, Vector<PlatformXR::SessionFeature> consentOptional, Vector<PlatformXR::SessionFeature> requiredFeaturesRequested, Vector<PlatformXR::SessionFeature> optionalFeaturesRequested) -> (std::optional<Vector<PlatformXR::SessionFeature>> userGranted)`
- `InitializeTrackingAndRendering()`
- `ShutDownTrackingAndRendering()`
- `RequestFrame(std::optional<PlatformXR::RequestData> requestData) -> (PlatformXR::FrameData frameData)`
- `SubmitFrame()`
- `DidCompleteShutdownTriggeredBySystem()`

## `PlaybackSessionManagerProxy` - WebContent -> UI

`UIProcess/Cocoa/PlaybackSessionManagerProxy.messages.in`

- `CurrentTimeChanged(WebKit::PlaybackSessionContextIdentifier contextId, double currentTime, double hostTime)`
- `BufferedTimeChanged(WebKit::PlaybackSessionContextIdentifier contextId, double bufferedTime)`
- `SeekableRangesVectorChanged(WebKit::PlaybackSessionContextIdentifier contextId, Vector<std::pair<double, double>> ranges, double lastModifiedTime, double liveUpdateInterval)`
- `CanPlayFastReverseChanged(WebKit::PlaybackSessionContextIdentifier contextId, bool value)`
- `AudioMediaSelectionOptionsChanged(WebKit::PlaybackSessionContextIdentifier contextId, Vector<WebCore::MediaSelectionOption> options, uint64_t selectedIndex)`
- `LegibleMediaSelectionOptionsChanged(WebKit::PlaybackSessionContextIdentifier contextId, Vector<WebCore::MediaSelectionOption> options, uint64_t selectedIndex)`
- `AudioMediaSelectionIndexChanged(WebKit::PlaybackSessionContextIdentifier contextId, uint64_t selectedIndex)`
- `LegibleMediaSelectionIndexChanged(WebKit::PlaybackSessionContextIdentifier contextId, uint64_t selectedIndex)`
- `ExternalPlaybackPropertiesChanged(WebKit::PlaybackSessionContextIdentifier contextId, bool enabled, WebCore::PlaybackSessionModelExternalPlaybackTargetType targetType, String localizedDeviceName)`
- `WirelessVideoPlaybackDisabledChanged(WebKit::PlaybackSessionContextIdentifier contextId, bool disabled)`
- `DurationChanged(WebKit::PlaybackSessionContextIdentifier contextId, double duration)`
- `PlaybackStartedTimeChanged(WebKit::PlaybackSessionContextIdentifier contextId, double playbackStartedTime)`
- `RateChanged(WebKit::PlaybackSessionContextIdentifier contextId, OptionSet<WebCore::PlaybackSessionModelPlaybackState> playbackState, double rate, double defaultPlaybackRate)`
- `MutedChanged(WebKit::PlaybackSessionContextIdentifier contextId, bool muted)`
- `VolumeChanged(WebKit::PlaybackSessionContextIdentifier contextId, double volume)`
- `PictureInPictureSupportedChanged(WebKit::PlaybackSessionContextIdentifier contextId, bool pictureInPictureSupported)`
- `IsInWindowFullscreenActiveChanged(WebKit::PlaybackSessionContextIdentifier contextId, bool isInWindow)`
- `SupportsLinearMediaPlayerChanged(WebKit::PlaybackSessionContextIdentifier contextId, bool supportsLinearMediaPlayer)` (if ENABLE(LINEAR_MEDIA_PLAYER))
- `SpatialVideoMetadataChanged(WebKit::PlaybackSessionContextIdentifier contextId, std::optional<WebCore::SpatialVideoMetadata> metadata)` (if ENABLE(LINEAR_MEDIA_PLAYER))
- `SetUpPlaybackControlsManagerWithID(WebKit::PlaybackSessionContextIdentifier contextId, bool isVideo)`
- `ClearPlaybackControlsManager()`
- `SwapFullscreenModes(WebKit::PlaybackSessionContextIdentifier firstContextId, WebKit::PlaybackSessionContextIdentifier secondContextId)`
- `HandleControlledElementIDResponse(WebKit::PlaybackSessionContextIdentifier contextId, String id)`
- `SetLogIdentifier(WebKit::PlaybackSessionContextIdentifier contextId, uint64_t logIdentifier)` (if !RELEASE_LOG_DISABLED)

## `RemoteLayerTreeDrawingAreaProxy` - WebContent -> UI

`UIProcess/RemoteLayerTree/RemoteLayerTreeDrawingAreaProxy.messages.in`

- `SetPreferredFramesPerSecond(unsigned preferredFramesPerSecond)`
- `WillCommitLayerTree(WebKit::TransactionID transactionID)`
- `CommitLayerTreeNotTriggered(WebKit::TransactionID nextCommitTransactionID)`
- `CommitLayerTree(Vector<std::pair<WebKit::RemoteLayerTreeTransaction, WebKit::RemoteScrollingCoordinatorTransaction>> transactions, HashMap<WebKit::RemoteImageBufferSetIdentifier, std::unique_ptr<WebKit::BufferSetBackendHandle>> handlesMap)` (CanDispatchOutOfOrder)
- `AsyncSetLayerContents(WebCore::PlatformLayerIdentifier layer, WebKit::ImageBufferBackendHandle handle, WebCore::RenderingResourceIdentifier identifier)`

## `RemoteMediaSessionCoordinatorProxy` - WebContent -> UI

`UIProcess/Media/RemoteMediaSessionCoordinatorProxy.messages.in`

- `Join() -> (std::optional<WebCore::ExceptionData> error)`
- `Leave()`
- `CoordinateSeekTo(double time) -> (std::optional<WebCore::ExceptionData> error)`
- `CoordinatePlay() -> (std::optional<WebCore::ExceptionData> error)`
- `CoordinatePause() -> (std::optional<WebCore::ExceptionData> error)`
- `CoordinateSetTrack(String trackIdentifier) -> (std::optional<WebCore::ExceptionData> error)`
- `PositionStateChanged(std::optional<WebCore::MediaPositionState> state)`
- `ReadyStateChanged(WebCore::MediaSessionReadyState state)`
- `PlaybackStateChanged(WebCore::MediaSessionPlaybackState state)`
- `TrackIdentifierChanged(String trackIdentifier)` (final)

## `RemoteWebInspectorUIProxy` - WebContent -> UI

`UIProcess/Inspector/RemoteWebInspectorUIProxy.messages.in`

- `FrontendLoaded()`
- `FrontendDidClose()`
- `Reopen()`
- `ResetState()`
- `BringToFront()`
- `Save(Vector<WebCore::InspectorFrontendClient::SaveData> saveDatas, bool forceSaveAs)`
- `Load(String path) -> (String content)`
- `PickColorFromScreen() -> (std::optional<WebCore::Color> color)`
- `SetForcedAppearance(WebCore::InspectorFrontendClient::Appearance appearance)`
- `SetSheetRect(WebCore::FloatRect rect)`
- `StartWindowDrag()`
- `OpenURLExternally(String url)`
- `RevealFileExternally(String path)`
- `ShowCertificate(WebCore::CertificateInfo certificateInfo)`
- `SendMessageToBackend(String message)`
- `SetInspectorPageDeveloperExtrasEnabled(bool enabled)`

## `SmartMagnificationController` - WebContent -> UI

`UIProcess/ios/SmartMagnificationController.messages.in`

- `DidCollectGeometryForSmartMagnificationGesture(WebCore::FloatPoint origin, WebCore::FloatRect renderRect, WebCore::FloatRect visibleContentBounds, bool fitEntireRect, double viewportMinimumScale, double viewportMaximumScale)`
- `ScrollToRect(WebCore::FloatPoint origin, WebCore::FloatRect targetRect)`

## `SpeechRecognitionRemoteRealtimeMediaSourceManager` - WebContent -> UI

`UIProcess/SpeechRecognitionRemoteRealtimeMediaSourceManager.messages.in`

- `RemoteAudioSamplesAvailable(WebCore::RealtimeMediaSourceIdentifier identifier, MediaTime time, uint64_t numberOfFrames)`
- `RemoteCaptureFailed(WebCore::RealtimeMediaSourceIdentifier identifier)`
- `RemoteSourceStopped(WebCore::RealtimeMediaSourceIdentifier identifier)`
- `SetStorage(WebCore::RealtimeMediaSourceIdentifier identifier, WebKit::ConsumerSharedCARingBufferHandle storageHandle, WebCore::CAAudioStreamDescription description)` (if PLATFORM(COCOA))

## `SpeechRecognitionServer` - WebContent -> UI

`UIProcess/SpeechRecognitionServer.messages.in`

- `Start(WebCore::SpeechRecognitionConnectionClientIdentifier identifier, String lang, bool continuous, bool interimResults, uint64_t maxAlternatives, WebCore::ClientOrigin origin, WebCore::FrameIdentifier frameIdentifier)`
- `Stop(WebCore::SpeechRecognitionConnectionClientIdentifier identifier)`
- `Abort(WebCore::SpeechRecognitionConnectionClientIdentifier identifier)`
- `Invalidate(WebCore::SpeechRecognitionConnectionClientIdentifier identifier)`

## `VideoPresentationManagerProxy` - WebContent -> UI

`UIProcess/Cocoa/VideoPresentationManagerProxy.messages.in`

- `SetHasVideo(WebKit::PlaybackSessionContextIdentifier contextId, bool hasVideo)`
- `SetDocumentVisibility(WebKit::PlaybackSessionContextIdentifier contextId, bool isDocumentVisible)`
- `AudioSessionCategoryChanged(WebKit::PlaybackSessionContextIdentifier contextId, WebCore::AudioSessionCategory category, WebCore::AudioSessionMode mode, WebCore::RouteSharingPolicy policy)`
- `SetVideoDimensions(WebKit::PlaybackSessionContextIdentifier contextId, WebCore::FloatSize videoDimensions)`
- `SetupFullscreenWithID(WebKit::PlaybackSessionContextIdentifier contextId, WebKit::LayerHostingContextID videoLayerID, WebCore::FloatRect screenRect, WebCore::FloatSize initialSize, WebCore::FloatSize videoDimensions, float hostingScaleFactor, WebCore::MediaPlayerEnums::VideoFullscreenMode videoFullscreenMode, bool allowsPictureInPicture, bool standby, bool blocksReturnToFullscreenFromPictureInPicture)`
- `SetPlayerIdentifier(WebKit::PlaybackSessionContextIdentifier contextId, std::optional<WebCore::MediaPlayerIdentifier> playerIdentifier)`
- `EnterFullscreen(WebKit::PlaybackSessionContextIdentifier contextId)` (if !PLATFORM(IOS_FAMILY))
- `ExitFullscreen(WebKit::PlaybackSessionContextIdentifier contextId, WebCore::FloatRect finalRect) -> (bool success)`
- `SetInlineRect(WebKit::PlaybackSessionContextIdentifier contextId, WebCore::FloatRect inlineRect, bool visible)`
- `SetHasVideoContentLayer(WebKit::PlaybackSessionContextIdentifier contextId, bool value)`
- `CleanupFullscreen(WebKit::PlaybackSessionContextIdentifier contextId)`
- `PreparedToReturnToInline(WebKit::PlaybackSessionContextIdentifier contextId, bool visible, WebCore::FloatRect inlineRect)`
- `PreparedToExitFullscreen(WebKit::PlaybackSessionContextIdentifier contextId)`
- `ExitFullscreenWithoutAnimationToMode(WebKit::PlaybackSessionContextIdentifier contextId, WebCore::MediaPlayerEnums::VideoFullscreenMode videoFullscreenMode)`
- `SetVideoFullscreenMode(WebKit::PlaybackSessionContextIdentifier contextId, WebCore::MediaPlayerEnums::VideoFullscreenMode mode)`
- `ClearVideoFullscreenMode(WebKit::PlaybackSessionContextIdentifier contextId, WebCore::MediaPlayerEnums::VideoFullscreenMode mode)`
- `TextTrackRepresentationUpdate(WebKit::PlaybackSessionContextIdentifier contextId, WebCore::ShareableBitmapHandle textTrack)`
- `TextTrackRepresentationSetContentsScale(WebKit::PlaybackSessionContextIdentifier contextId, float scale)`
- `TextTrackRepresentationSetHidden(WebKit::PlaybackSessionContextIdentifier contextId, bool hidden)`

## `ViewGestureController` - WebContent -> UI

`UIProcess/ViewGestureController.messages.in`

- `DidCollectGeometryForSmartMagnificationGesture(WebCore::FloatPoint origin, WebCore::FloatRect renderRect, WebCore::FloatRect visibleContentBounds, bool fitEntireRect, double viewportMinimumScale, double viewportMaximumScale)` (if PLATFORM(MAC))
- `DidCollectGeometryForMagnificationGesture(WebCore::FloatRect visibleContentBounds, bool frameHandlesMagnificationGesture)` (if !PLATFORM(IOS_FAMILY))
- `DidHitRenderTreeSizeThreshold()` (if !PLATFORM(IOS_FAMILY))

## `VisitedLinkStore` - WebContent -> UI

`UIProcess/VisitedLinkStore.messages.in`

- `AddVisitedLinkHashFromPage(WebKit::WebPageProxyIdentifier pageProxyID, WebCore::SharedStringHash linkHash)`

## `WebAuthenticatorCoordinatorProxy` - WebContent -> UI

`UIProcess/WebAuthentication/WebAuthenticatorCoordinatorProxy.messages.in`

- `MakeCredential(WebCore::FrameIdentifier frameID, WebKit::FrameInfoData frameInfo, WebCore::PublicKeyCredentialCreationOptions options, WebCore::MediationRequirement mediation) -> (WebCore::AuthenticatorResponseData data, WebCore::AuthenticatorAttachment attachment, WebCore::ExceptionData exception)`
- `GetAssertion(WebCore::FrameIdentifier frameID, WebKit::FrameInfoData frameInfo, WebCore::PublicKeyCredentialRequestOptions options, WebCore::MediationRequirement mediation, std::optional<WebCore::SecurityOriginData> parentOrigin) -> (WebCore::AuthenticatorResponseData data, WebCore::AuthenticatorAttachment attachment, WebCore::ExceptionData exception)`
- `isConditionalMediationAvailable(WebCore::SecurityOriginData origin) -> (bool result)`
- `IsUserVerifyingPlatformAuthenticatorAvailable(WebCore::SecurityOriginData origin) -> (bool result)`
- `GetClientCapabilities(WebCore::SecurityOriginData origin) -> (Vector<KeyValuePair<String, bool>> result)`
- `Cancel() -> ()`

## `WebAutomationSession` - WebContent -> UI

`UIProcess/Automation/WebAutomationSession.messages.in`

- `LogEntryAdded(JSC::MessageSource messageSource, JSC::MessageLevel messageLevel, String messageText, JSC::MessageType messageType, WallTime timestamp)`

## `WebDeviceOrientationUpdateProviderProxy` - WebContent -> UI

`UIProcess/ios/WebDeviceOrientationUpdateProviderProxy.messages.in`

- `StartUpdatingDeviceOrientation()`
- `StopUpdatingDeviceOrientation()`
- `StartUpdatingDeviceMotion()`
- `StopUpdatingDeviceMotion()`

## `WebExtensionContext` - WebContent -> UI

`UIProcess/Extensions/WebExtensionContext.messages.in`

- `ActionGetTitle(std::optional<WebKit::WebExtensionWindowIdentifier> windowIdentifier, std::optional<WebKit::WebExtensionTabIdentifier> tabIdentifier) -> (Expected<String, WebKit::WebExtensionError> result)`
- `ActionSetTitle(std::optional<WebKit::WebExtensionWindowIdentifier> windowIdentifier, std::optional<WebKit::WebExtensionTabIdentifier> tabIdentifier, String title) -> (Expected<void, WebKit::WebExtensionError> result)`
- `ActionSetIcon(std::optional<WebKit::WebExtensionWindowIdentifier> windowIdentifier, std::optional<WebKit::WebExtensionTabIdentifier> tabIdentifier, String iconsJSON) -> (Expected<void, WebKit::WebExtensionError> result)`
- `ActionGetPopup(std::optional<WebKit::WebExtensionWindowIdentifier> windowIdentifier, std::optional<WebKit::WebExtensionTabIdentifier> tabIdentifier) -> (Expected<String, WebKit::WebExtensionError> result)`
- `ActionSetPopup(std::optional<WebKit::WebExtensionWindowIdentifier> windowIdentifier, std::optional<WebKit::WebExtensionTabIdentifier> tabIdentifier, String popupPath) -> (Expected<void, WebKit::WebExtensionError> result)`
- `ActionOpenPopup(WebKit::WebPageProxyIdentifier identifier, std::optional<WebKit::WebExtensionWindowIdentifier> windowIdentifier, std::optional<WebKit::WebExtensionTabIdentifier> tabIdentifier) -> (Expected<void, WebKit::WebExtensionError> result)`
- `ActionGetBadgeText(std::optional<WebKit::WebExtensionWindowIdentifier> windowIdentifier, std::optional<WebKit::WebExtensionTabIdentifier> tabIdentifier) -> (Expected<String, WebKit::WebExtensionError> result)`
- `ActionSetBadgeText(std::optional<WebKit::WebExtensionWindowIdentifier> windowIdentifier, std::optional<WebKit::WebExtensionTabIdentifier> tabIdentifier, String text) -> (Expected<void, WebKit::WebExtensionError> result)`
- `ActionGetEnabled(std::optional<WebKit::WebExtensionWindowIdentifier> windowIdentifier, std::optional<WebKit::WebExtensionTabIdentifier> tabIdentifier) -> (Expected<bool, WebKit::WebExtensionError> result)`
- `ActionSetEnabled(std::optional<WebKit::WebExtensionTabIdentifier> tabIdentifier, bool enabled) -> (Expected<void, WebKit::WebExtensionError> result)`
- `AlarmsCreate(String name, Seconds initialInterval, Seconds repeatInterval)`
- `AlarmsGet(String name) -> (std::optional<WebKit::WebExtensionAlarmParameters> alarmInfo)`
- `AlarmsClear(String name) -> ()`
- `AlarmsGetAll() -> (Vector<WebKit::WebExtensionAlarmParameters> alarms)`
- `AlarmsClearAll() -> ()`
- `CommandsGetAll() -> (Vector<WebKit::WebExtensionCommandParameters> commands)`
- `CookiesGet(std::optional<PAL::SessionID> sessionID, String name, URL url) -> (Expected<std::optional<WebKit::WebExtensionCookieParameters>, WebKit::WebExtensionError> result)`
- `CookiesGetAll(std::optional<PAL::SessionID> sessionID, URL url, WebKit::WebExtensionCookieFilterParameters filterParameters) -> (Expected<Vector<WebKit::WebExtensionCookieParameters>, WebKit::WebExtensionError> result)`
- `CookiesSet(std::optional<PAL::SessionID> sessionID, WebKit::WebExtensionCookieParameters cookie) -> (Expected<std::optional<WebKit::WebExtensionCookieParameters>, WebKit::WebExtensionError> result)`
- `CookiesRemove(std::optional<PAL::SessionID> sessionID, String name, URL url) -> (Expected<std::optional<WebKit::WebExtensionCookieParameters>, WebKit::WebExtensionError> result)`
- `CookiesGetAllCookieStores() -> (Expected<HashMap<PAL::SessionID, Vector<WebKit::WebExtensionTabIdentifier>>, WebKit::WebExtensionError> result)`
- `DeclarativeNetRequestGetEnabledRulesets() -> (Vector<String> rulesetIdentifiers)`
- `DeclarativeNetRequestUpdateEnabledRulesets(Vector<String> rulesetIdentifiersToEnable, Vector<String> rulesetIdentifiersToDisable) -> (Expected<void, WebKit::WebExtensionError> result)`
- `DeclarativeNetRequestDisplayActionCountAsBadgeText(bool result) -> (Expected<void, WebKit::WebExtensionError> result)`
- `DeclarativeNetRequestIncrementActionCount(WebKit::WebExtensionTabIdentifier tabIdentifier, double increment) -> (Expected<void, WebKit::WebExtensionError> result)`
- `DeclarativeNetRequestGetMatchedRules(std::optional<WebKit::WebExtensionTabIdentifier> tabIdentifier, std::optional<WallTime> minTimeStamp) -> (Expected<Vector<WebKit::WebExtensionMatchedRuleParameters>, WebKit::WebExtensionError> result)`
- `DeclarativeNetRequestGetDynamicRules(Vector<double> ruleIDs) -> (Expected<String, WebKit::WebExtensionError> result)`
- `DeclarativeNetRequestUpdateDynamicRules(String rulesToAddJSON, Vector<double> ruleIdsToRemove) -> (Expected<void, WebKit::WebExtensionError> result)`
- `DeclarativeNetRequestGetSessionRules(Vector<double> ruleIDs) -> (Expected<String, WebKit::WebExtensionError> result)`
- `DeclarativeNetRequestUpdateSessionRules(String rulesToAddJSON, Vector<double> ruleIdsToRemove) -> (Expected<void, WebKit::WebExtensionError> result)`
- `DevToolsPanelsCreate(WebKit::WebPageProxyIdentifier webPageProxyIdentifier, String title, String iconPath, String pagePath) -> (Expected<Inspector::ExtensionTabID, WebKit::WebExtensionError> result)` (if ENABLE(INSPECTOR_EXTENSIONS))
- `DevToolsInspectedWindowEval(WebKit::WebPageProxyIdentifier webPageProxyIdentifier, String scriptSource, std::optional<URL> frameURL) -> (Expected<Expected<std::span<const uint8_t>, WebCore::ExceptionDetails>, WebKit::WebExtensionError> result)` (if ENABLE(INSPECTOR_EXTENSIONS))
- `DevToolsInspectedWindowReload(WebKit::WebPageProxyIdentifier webPageProxyIdentifier, std::optional<bool> ignoreCache)` (if ENABLE(INSPECTOR_EXTENSIONS))
- `AddListener(WebCore::FrameIdentifier frameIdentifier, WebKit::WebExtensionEventListenerType listenerType, WebKit::WebExtensionContentWorldType contentWorldType)`
- `RemoveListener(WebCore::FrameIdentifier frameIdentifier, WebKit::WebExtensionEventListenerType listenerType, WebKit::WebExtensionContentWorldType contentWorldType, size_t removedCount)`
- `ExtensionIsAllowedIncognitoAccess() -> (bool result)`
- `MenusCreate(WebKit::WebExtensionMenuItemParameters parameters) -> (Expected<void, WebKit::WebExtensionError> result)`
- `MenusUpdate(String identifier, WebKit::WebExtensionMenuItemParameters parameters) -> (Expected<void, WebKit::WebExtensionError> result)`
- `MenusRemove(String identifier) -> (Expected<void, WebKit::WebExtensionError> result)`
- `MenusRemoveAll() -> (Expected<void, WebKit::WebExtensionError> result)`
- `PermissionsGetAll() -> (Vector<String> permissions, Vector<String> origins)`
- `PermissionsContains(HashSet<String> permissions, HashSet<String> origins) -> (bool containsPermissions)`
- `PermissionsRequest(HashSet<String> permissions, HashSet<String> origins) -> (bool success)`
- `PermissionsRemove(HashSet<String> permissions, HashSet<String> origins) -> (bool success)`
- `PortPostMessage(WebKit::WebExtensionContentWorldType sourceContentWorldType, WebKit::WebExtensionContentWorldType targetContentWorldType, std::optional<WebKit::WebPageProxyIdentifier> sendingPageProxyIdentifier, WebKit::WebExtensionPortChannelIdentifier channelIdentifier, String messageJSON)`
- `PortRemoved(WebKit::WebExtensionContentWorldType sourceContentWorldType, WebKit::WebExtensionContentWorldType targetContentWorldType, WebKit::WebPageProxyIdentifier pageProxyIdentifier, WebKit::WebExtensionPortChannelIdentifier channelIdentifier)`
- `RuntimeGetBackgroundPage() -> (Expected<std::optional<WebCore::PageIdentifier>, WebKit::WebExtensionError> result)`
- `RuntimeOpenOptionsPage() -> (Expected<void, WebKit::WebExtensionError> result)`
- `RuntimeReload()`
- `RuntimeSendMessage(String extensionID, String messageJSON, WebKit::WebExtensionMessageSenderParameters senderParameters) -> (Expected<String, WebKit::WebExtensionError> result)`
- `RuntimeConnect(String extensionID, WebKit::WebExtensionPortChannelIdentifier channelIdentifier, String name, WebKit::WebExtensionMessageSenderParameters senderParameters) -> (Expected<void, WebKit::WebExtensionError> result)`
- `RuntimeSendNativeMessage(String applicationID, String messageJSON) -> (Expected<String, WebKit::WebExtensionError> result)`
- `RuntimeConnectNative(String applicationID, WebKit::WebExtensionPortChannelIdentifier channelIdentifier, WebKit::WebPageProxyIdentifier pageProxyIdentifier) -> (Expected<void, WebKit::WebExtensionError> result)`
- `RuntimeWebPageSendMessage(String extensionID, String messageJSON, WebKit::WebExtensionMessageSenderParameters senderParameters) -> (Expected<String, WebKit::WebExtensionError> result)`
- `RuntimeWebPageConnect(String extensionID, WebKit::WebExtensionPortChannelIdentifier channelIdentifier, String name, WebKit::WebExtensionMessageSenderParameters senderParameters) -> (Expected<void, WebKit::WebExtensionError> result)`
- `ScriptingExecuteScript(WebKit::WebExtensionScriptInjectionParameters parameters) -> (Expected<Vector<WebKit::WebExtensionScriptInjectionResultParameters>, WebKit::WebExtensionError> result)`
- `ScriptingInsertCSS(WebKit::WebExtensionScriptInjectionParameters parameters) -> (Expected<void, WebKit::WebExtensionError> result)`
- `ScriptingRemoveCSS(WebKit::WebExtensionScriptInjectionParameters parameters) -> (Expected<void, WebKit::WebExtensionError> result)`
- `ScriptingRegisterContentScripts(Vector<WebKit::WebExtensionRegisteredScriptParameters> scripts) -> (Expected<void, WebKit::WebExtensionError> result)`
- `ScriptingUpdateRegisteredScripts(Vector<WebKit::WebExtensionRegisteredScriptParameters> scripts) -> (Expected<void, WebKit::WebExtensionError> result)`
- `ScriptingGetRegisteredScripts(Vector<String> scriptIDs) -> (Expected<Vector<WebKit::WebExtensionRegisteredScriptParameters>, WebKit::WebExtensionError> result)`
- `ScriptingUnregisterContentScripts(Vector<String> scriptIDs) -> (Expected<void, WebKit::WebExtensionError> result)`
- `SidebarOpen(std::optional<WebKit::WebExtensionWindowIdentifier> windowIdentifier, std::optional<WebKit::WebExtensionTabIdentifier> tabIdentifier) -> (Expected<void, WebKit::WebExtensionError> result)` (if ENABLE(WK_WEB_EXTENSIONS_SIDEBAR))
- `SidebarIsOpen(std::optional<WebKit::WebExtensionWindowIdentifier> windowIdentifier) -> (Expected<bool, WebKit::WebExtensionError> result)` (if ENABLE(WK_WEB_EXTENSIONS_SIDEBAR))
- `SidebarClose() -> (Expected<void, WebKit::WebExtensionError> result)` (if ENABLE(WK_WEB_EXTENSIONS_SIDEBAR))
- `SidebarToggle() -> (Expected<void, WebKit::WebExtensionError> result)` (if ENABLE(WK_WEB_EXTENSIONS_SIDEBAR))
- `SidebarGetOptions(std::optional<WebKit::WebExtensionWindowIdentifier> windowIdentifier, std::optional<WebKit::WebExtensionTabIdentifier> tabIdentifier) -> (Expected<WebKit::WebExtensionSidebarParameters, WebKit::WebExtensionError> result)` (if ENABLE(WK_WEB_EXTENSIONS_SIDEBAR))
- `SidebarSetOptions(std::optional<WebKit::WebExtensionWindowIdentifier> windowIdentifier, std::optional<WebKit::WebExtensionTabIdentifier> tabIdentifier, std::optional<String> panelSourcePath, std::optional<bool> enabled) -> (Expected<void, WebKit::WebExtensionError> result)` (if ENABLE(WK_WEB_EXTENSIONS_SIDEBAR))
- `SidebarGetTitle(std::optional<WebKit::WebExtensionWindowIdentifier> windowIdentifier, std::optional<WebKit::WebExtensionTabIdentifier> tabIdentifier) -> (Expected<String, WebKit::WebExtensionError> result)` (if ENABLE(WK_WEB_EXTENSIONS_SIDEBAR))
- `SidebarSetTitle(std::optional<WebKit::WebExtensionWindowIdentifier> windowIdentifier, std::optional<WebKit::WebExtensionTabIdentifier> tabIdentifier, std::optional<String> title) -> (Expected<void, WebKit::WebExtensionError> result)` (if ENABLE(WK_WEB_EXTENSIONS_SIDEBAR))
- `SidebarSetIcon(std::optional<WebKit::WebExtensionWindowIdentifier> windowIdentifier, std::optional<WebKit::WebExtensionTabIdentifier> tabIdentifier, String iconsJSON) -> (Expected<void, WebKit::WebExtensionError> result)` (if ENABLE(WK_WEB_EXTENSIONS_SIDEBAR))
- `SidebarSetActionClickBehavior(WebKit::WebExtensionActionClickBehavior actionClickBehavior) -> (Expected<void, WebKit::WebExtensionError> result)` (if ENABLE(WK_WEB_EXTENSIONS_SIDEBAR))
- `SidebarGetActionClickBehavior() -> (Expected<WebKit::WebExtensionActionClickBehavior, WebKit::WebExtensionError> result)` (if ENABLE(WK_WEB_EXTENSIONS_SIDEBAR))
- `StorageGet(WebKit::WebPageProxyIdentifier webPageProxyIdentifier, WebKit::WebExtensionDataType dataType, Vector<String> keys) -> (Expected<String, WebKit::WebExtensionError> result)`
- `StorageGetKeys(WebKit::WebPageProxyIdentifier webPageProxyIdentifier, WebKit::WebExtensionDataType dataType) -> (Expected<Vector<String>, WebKit::WebExtensionError> result)`
- `StorageGetBytesInUse(WebKit::WebPageProxyIdentifier webPageProxyIdentifier, WebKit::WebExtensionDataType dataType, Vector<String> keys) -> (Expected<size_t, WebKit::WebExtensionError> result)`
- `StorageSet(WebKit::WebPageProxyIdentifier webPageProxyIdentifier, WebKit::WebExtensionDataType dataType, String dataJSON) -> (Expected<void, WebKit::WebExtensionError> result)`
- `StorageRemove(WebKit::WebPageProxyIdentifier webPageProxyIdentifier, WebKit::WebExtensionDataType dataType, Vector<String> keys) -> (Expected<void, WebKit::WebExtensionError> result)`
- `StorageClear(WebKit::WebPageProxyIdentifier webPageProxyIdentifier, WebKit::WebExtensionDataType dataType) -> (Expected<void, WebKit::WebExtensionError> result)`
- `StorageSetAccessLevel(WebKit::WebPageProxyIdentifier webPageProxyIdentifier, WebKit::WebExtensionDataType dataType, WebKit::WebExtensionStorageAccessLevel accessLevel) -> (Expected<void, WebKit::WebExtensionError> result)`
- `TabsCreate(std::optional<WebKit::WebPageProxyIdentifier> webPageProxyIdentifier, WebKit::WebExtensionTabParameters creationParameters) -> (Expected<std::optional<WebKit::WebExtensionTabParameters>, WebKit::WebExtensionError> result)`
- `TabsUpdate(WebKit::WebPageProxyIdentifier webPageProxyIdentifier, std::optional<WebKit::WebExtensionTabIdentifier> tabIdentifier, WebKit::WebExtensionTabParameters updateParameters) -> (Expected<std::optional<WebKit::WebExtensionTabParameters>, WebKit::WebExtensionError> result)`
- `TabsDuplicate(WebKit::WebExtensionTabIdentifier tabIdentifier, WebKit::WebExtensionTabParameters creationParameters) -> (Expected<std::optional<WebKit::WebExtensionTabParameters>, WebKit::WebExtensionError> result)`
- `TabsGet(WebKit::WebExtensionTabIdentifier tabIdentifier) -> (Expected<std::optional<WebKit::WebExtensionTabParameters>, WebKit::WebExtensionError> result)`
- `TabsGetCurrent(WebKit::WebPageProxyIdentifier webPageProxyIdentifier) -> (Expected<std::optional<WebKit::WebExtensionTabParameters>, WebKit::WebExtensionError> result)`
- `TabsQuery(WebKit::WebPageProxyIdentifier webPageProxyIdentifier, WebKit::WebExtensionTabQueryParameters queryParameters) -> (Expected<Vector<WebKit::WebExtensionTabParameters>, WebKit::WebExtensionError> result)`
- `TabsReload(WebKit::WebPageProxyIdentifier webPageProxyIdentifier, std::optional<WebKit::WebExtensionTabIdentifier> tabIdentifier, WebKit::WebExtensionContext::ReloadFromOrigin reloadFromOrigin) -> (Expected<void, WebKit::WebExtensionError> result)`
- `TabsGoBack(WebKit::WebPageProxyIdentifier webPageProxyIdentifier, std::optional<WebKit::WebExtensionTabIdentifier> tabIdentifier) -> (Expected<void, WebKit::WebExtensionError> result)`
- `TabsGoForward(WebKit::WebPageProxyIdentifier webPageProxyIdentifier, std::optional<WebKit::WebExtensionTabIdentifier> tabIdentifier) -> (Expected<void, WebKit::WebExtensionError> result)`
- `TabsDetectLanguage(WebKit::WebPageProxyIdentifier webPageProxyIdentifier, std::optional<WebKit::WebExtensionTabIdentifier> tabIdentifier) -> (Expected<String, WebKit::WebExtensionError> result)`
- `TabsToggleReaderMode(WebKit::WebPageProxyIdentifier webPageProxyIdentifier, std::optional<WebKit::WebExtensionTabIdentifier> tabIdentifier) -> (Expected<void, WebKit::WebExtensionError> result)`
- `TabsCaptureVisibleTab(WebKit::WebPageProxyIdentifier webPageProxyIdentifier, std::optional<WebKit::WebExtensionWindowIdentifier> windowIdentifier, WebKit::WebExtensionTabImageFormat imageFormat, uint8_t imageQuality) -> (Expected<URL, WebKit::WebExtensionError> result)`
- `TabsSendMessage(WebKit::WebExtensionTabIdentifier tabIdentifier, String messageJSON, WebKit::WebExtensionMessageTargetParameters targetParameters, WebKit::WebExtensionMessageSenderParameters senderParameters) -> (Expected<String, WebKit::WebExtensionError> result)`
- `TabsConnect(WebKit::WebExtensionTabIdentifier tabIdentifier, WebKit::WebExtensionPortChannelIdentifier channelIdentifier, String name, WebKit::WebExtensionMessageTargetParameters targetParameters, WebKit::WebExtensionMessageSenderParameters senderParameters) -> (Expected<void, WebKit::WebExtensionError> result)`
- `TabsGetZoom(WebKit::WebPageProxyIdentifier webPageProxyIdentifier, std::optional<WebKit::WebExtensionTabIdentifier> tabIdentifier) -> (Expected<double, WebKit::WebExtensionError> result)`
- `TabsSetZoom(WebKit::WebPageProxyIdentifier webPageProxyIdentifier, std::optional<WebKit::WebExtensionTabIdentifier> tabIdentifier, double zoomFactor) -> (Expected<void, WebKit::WebExtensionError> result)`
- `TabsRemove(Vector<WebKit::WebExtensionTabIdentifier> tabIdentifiers) -> (Expected<void, WebKit::WebExtensionError> result)`
- `TabsExecuteScript(WebKit::WebPageProxyIdentifier webPageProxyIdentifier, std::optional<WebKit::WebExtensionTabIdentifier> tabIdentifier, WebKit::WebExtensionScriptInjectionParameters parameters) -> (Expected<Vector<WebKit::WebExtensionScriptInjectionResultParameters>, WebKit::WebExtensionError> result)`
- `TabsInsertCSS(WebKit::WebPageProxyIdentifier webPageProxyIdentifier, std::optional<WebKit::WebExtensionTabIdentifier> tabIdentifier, WebKit::WebExtensionScriptInjectionParameters parameters) -> (Expected<void, WebKit::WebExtensionError> result)`
- `TabsRemoveCSS(WebKit::WebPageProxyIdentifier webPageProxyIdentifier, std::optional<WebKit::WebExtensionTabIdentifier> tabIdentifier, WebKit::WebExtensionScriptInjectionParameters parameters) -> (Expected<void, WebKit::WebExtensionError> result)`
- `WebNavigationGetAllFrames(WebKit::WebExtensionTabIdentifier tabIdentifier) -> (Expected<Vector<WebKit::WebExtensionFrameParameters>, WebKit::WebExtensionError> result)`
- `WebNavigationGetFrame(WebKit::WebExtensionTabIdentifier tabIdentifier, WebKit::WebExtensionFrameIdentifier frameIdentifier) -> (Expected<std::optional<WebKit::WebExtensionFrameParameters>, WebKit::WebExtensionError> result)`
- `WindowsCreate(WebKit::WebExtensionWindowParameters creationParameters) -> (Expected<std::optional<WebKit::WebExtensionWindowParameters>, WebKit::WebExtensionError> result)`
- `WindowsGet(WebKit::WebPageProxyIdentifier webPageProxyIdentifier, WebKit::WebExtensionWindowIdentifier windowIdentifier, OptionSet<WebKit::WebExtensionWindowTypeFilter> filter, WebKit::WebExtensionWindow::PopulateTabs populate) -> (Expected<WebKit::WebExtensionWindowParameters, WebKit::WebExtensionError> result)`
- `WindowsGetLastFocused(OptionSet<WebKit::WebExtensionWindowTypeFilter> filter, WebKit::WebExtensionWindow::PopulateTabs populate) -> (Expected<WebKit::WebExtensionWindowParameters, WebKit::WebExtensionError> result)`
- `WindowsGetAll(OptionSet<WebKit::WebExtensionWindowTypeFilter> filter, WebKit::WebExtensionWindow::PopulateTabs populate) -> (Expected<Vector<WebKit::WebExtensionWindowParameters>, WebKit::WebExtensionError> result)`
- `WindowsUpdate(WebKit::WebExtensionWindowIdentifier windowIdentifier, WebKit::WebExtensionWindowParameters updateParameters) -> (Expected<WebKit::WebExtensionWindowParameters, WebKit::WebExtensionError> result)`
- `WindowsRemove(WebKit::WebExtensionWindowIdentifier windowIdentifier) -> (Expected<void, WebKit::WebExtensionError> result)`

## `WebExtensionController` - WebContent -> UI

`UIProcess/Extensions/WebExtensionController.messages.in`

- `DidStartProvisionalLoadForFrame(WebKit::WebPageProxyIdentifier pageID, WebKit::WebExtensionFrameParameters frameParameters, WallTime timestamp)`
- `DidCommitLoadForFrame(WebKit::WebPageProxyIdentifier pageID, WebKit::WebExtensionFrameParameters frameParameters, WallTime timestamp)`
- `DidFinishLoadForFrame(WebKit::WebPageProxyIdentifier pageID, WebKit::WebExtensionFrameParameters frameParameters, WallTime timestamp)`
- `DidFailLoadForFrame(WebKit::WebPageProxyIdentifier pageID, WebKit::WebExtensionFrameParameters frameParameters, WallTime timestamp)`
- `TestResult(bool result, String message, String sourceURL, unsigned lineNumber)`
- `TestEqual(bool result, String expected, String actual, String message, String sourceURL, unsigned lineNumber)`
- `TestLogMessage(String message, String sourceURL, unsigned lineNumber)`
- `TestSentMessage(String message, String argument, String sourceURL, unsigned lineNumber)`
- `TestFinished(bool result, String message, String sourceURL, unsigned lineNumber)`

## `WebFullScreenManagerProxy` - WebContent -> UI

`UIProcess/WebFullScreenManagerProxy.messages.in`

- `EnterFullScreen(bool blocksReturnToFullscreenFromPictureInPicture, WebKit::FullScreenMediaDetails mediaDetails) -> (bool success)`
- `UpdateImageSource(WebKit::FullScreenMediaDetails mediaDetails)` (if ENABLE(QUICKLOOK_FULLSCREEN))
- `ExitFullScreen()`
- `BeganEnterFullScreen(WebCore::IntRect initialRect, WebCore::IntRect finalRect)`
- `BeganExitFullScreen(WebCore::IntRect initialRect, WebCore::IntRect finalRect)`
- `Close()`

## `WebGeolocationManagerProxy` - WebContent -> UI

`UIProcess/WebGeolocationManagerProxy.messages.in`

- `StartUpdating(WebCore::RegistrableDomain registrableDomain, WebKit::WebPageProxyIdentifier pageProxyID, String authorizationToken, bool enableHighAccuracy)`
- `StopUpdating(WebCore::RegistrableDomain registrableDomain)`
- `SetEnableHighAccuracy(WebCore::RegistrableDomain registrableDomain, bool enabled)`

## `WebInspectorUIExtensionControllerProxy` - WebContent -> UI

`UIProcess/Inspector/WebInspectorUIExtensionControllerProxy.messages.in`

- `DidShowExtensionTab(String extensionID, String extensionTabID, WebCore::FrameIdentifier frameID)`
- `DidHideExtensionTab(String extensionID, String extensionTabID)`
- `DidNavigateExtensionTab(String extensionID, String extensionTabID, URL newURL)`
- `InspectedPageDidNavigate(URL newURL)`

## `WebInspectorUIProxy` - WebContent -> UI

`UIProcess/Inspector/WebInspectorUIProxy.messages.in`

- `RequestOpenLocalInspectorFrontend()`
- `SetFrontendConnection(IPC::ConnectionHandle connectionHandle)`
- `SendMessageToBackend(String message)`
- `FrontendLoaded()`
- `DidClose()`
- `BringToFront()`
- `Reopen()`
- `ResetState()`
- `SetForcedAppearance(WebCore::InspectorFrontendClient::Appearance appearance)`
- `EffectiveAppearanceDidChange(WebCore::InspectorFrontendClient::Appearance appearance)`
- `OpenURLExternally(String url)`
- `RevealFileExternally(String path)`
- `InspectedURLChanged(String urlString)`
- `ShowCertificate(WebCore::CertificateInfo certificateInfo)`
- `ElementSelectionChanged(bool active)`
- `TimelineRecordingChanged(bool active)`
- `SetDeveloperPreferenceOverride(WebCore::InspectorClientDeveloperPreference developerPreference, std::optional<bool> overrideValue)`
- `SetEmulatedConditions(std::optional<int64_t> bytesPerSecondLimit)` (if ENABLE(INSPECTOR_NETWORK_THROTTLING))
- `Save(Vector<WebCore::InspectorFrontendClient::SaveData> saveDatas, bool forceSaveAs)`
- `Load(String path) -> (String content)`
- `PickColorFromScreen() -> (std::optional<WebCore::Color> color)`
- `AttachBottom()`
- `AttachRight()`
- `AttachLeft()`
- `Detach()`
- `AttachAvailabilityChanged(bool available)`
- `SetAttachedWindowHeight(unsigned height)`
- `SetAttachedWindowWidth(unsigned width)`
- `SetSheetRect(WebCore::FloatRect rect)`
- `StartWindowDrag()`
- `SetInspectorPageDeveloperExtrasEnabled(bool enabled)`

## `WebLockRegistryProxy` - WebContent -> UI

`UIProcess/WebLockRegistryProxy.messages.in`

- `RequestLock(WebCore::ClientOrigin clientOrigin, WebCore::WebLockIdentifier identifier, WebCore::ScriptExecutionContextIdentifier clientID, String name, WebCore::WebLockMode mode, bool steal, bool ifAvailable)`
- `ReleaseLock(WebCore::ClientOrigin clientOrigin, WebCore::WebLockIdentifier identifier, WebCore::ScriptExecutionContextIdentifier clientID, String name)`
- `AbortLockRequest(WebCore::ClientOrigin clientOrigin, WebCore::WebLockIdentifier identifier, WebCore::ScriptExecutionContextIdentifier clientID, String name) -> (bool wasAborted)`
- `Snapshot(WebCore::ClientOrigin clientOrigin) -> (WebCore::WebLockManagerSnapshot snapshot)`
- `ClientIsGoingAway(WebCore::ClientOrigin clientOrigin, WebCore::ScriptExecutionContextIdentifier clientId)`

## `WebPageProxy` - WebContent -> UI

`UIProcess/WebPageProxy.messages.in`

- `CreateNewPage(WebCore::WindowFeatures windowFeatures, WebKit::NavigationActionData navigationActionData) -> (std::optional<WebCore::PageIdentifier> newPageID, std::optional<WebKit::WebPageCreationParameters> newPageParameters)` (sync)
- `ShowPage()`
- `ClosePage()`
- `RunJavaScriptAlert(WebCore::FrameIdentifier frameID, WebKit::FrameInfoData frameInfo, String message) -> ()` (sync)
- `RunJavaScriptConfirm(WebCore::FrameIdentifier frameID, WebKit::FrameInfoData frameInfo, String message) -> (bool result)` (sync)
- `RunJavaScriptPrompt(WebCore::FrameIdentifier frameID, WebKit::FrameInfoData frameInfo, String message, String defaultValue) -> (String result)` (sync)
- `MouseDidMoveOverElement(WebKit::WebHitTestResultData hitTestResultData, OptionSet<WebKit::WebEventModifier> modifiers, WebKit::UserData userData)`
- `DidReceiveEvent(WebKit::WebEventType eventType, bool handled, std::optional<WebCore::RemoteUserInputEventData> remoteUserInputEventData)`
- `SetCursor(WebCore::Cursor cursor)`
- `SetCursorHiddenUntilMouseMoves(bool hiddenUntilMouseMoves)`
- `SetFocus(bool focused)`
- `TakeFocus(WebCore::FocusDirection direction)`
- `FocusFromServiceWorker() -> ()`
- `FocusedFrameChanged(std::optional<WebCore::FrameIdentifier> frameID)`
- `SetRenderTreeSize(uint64_t treeSize)`
- `SetToolbarsAreVisible(bool toolbarsAreVisible)`
- `GetToolbarsAreVisible() -> (bool toolbarsAreVisible)` (sync)
- `SetMenuBarIsVisible(bool menuBarIsVisible)`
- `GetMenuBarIsVisible() -> (bool menuBarIsVisible)` (sync)
- `SetStatusBarIsVisible(bool statusBarIsVisible)`
- `GetStatusBarIsVisible() -> (bool statusBarIsVisible)` (sync)
- `SetIsResizable(bool isResizable)`
- `SetWindowFrame(WebCore::FloatRect windowFrame)`
- `GetWindowFrame() -> (WebCore::FloatRect windowFrame)` (sync)
- `ScreenToRootView(WebCore::IntPoint screenPoint) -> (WebCore::IntPoint windowPoint)` (sync)
- `RootViewPointToScreen(WebCore::IntPoint rect) -> (WebCore::IntPoint viewPoint)` (sync)
- `RootViewRectToScreen(WebCore::IntRect rect) -> (WebCore::IntRect screenFrame)` (sync)
- `AccessibilityScreenToRootView(WebCore::IntPoint screenPoint) -> (WebCore::IntPoint windowPoint)` (sync)
- `RootViewToAccessibilityScreen(WebCore::IntRect rect) -> (WebCore::IntRect screenFrame)` (sync)
- `RelayAccessibilityNotification(String notificationName, std::span<const uint8_t> notificationData)` (if PLATFORM(IOS_FAMILY))
- `EnableAccessibilityForAllProcesses()`
- `ShowValidationMessage(WebCore::IntRect anchorRect, String message)` (if PLATFORM(COCOA) || PLATFORM(GTK))
- `HideValidationMessage()` (if PLATFORM(COCOA) || PLATFORM(GTK))
- `RunBeforeUnloadConfirmPanel(WebCore::FrameIdentifier frameID, WebKit::FrameInfoData frameInfo, String message) -> (bool shouldClose)` (sync)
- `PageDidScroll(WebCore::IntPoint scrollPosition)`
- `SetHasActiveAnimatedScrolls(bool hasActiveAnimatedScrolls)`
- `RunOpenPanel(WebCore::FrameIdentifier frameID, WebKit::FrameInfoData frameInfo, WebCore::FileChooserSettings parameters)`
- `ShowShareSheet(WebCore::ShareDataWithParsedURL shareData) -> (bool granted)`
- `ShowContactPicker(WebCore::ContactsRequestData requestData) -> (std::optional<Vector<WebCore::ContactInfo>> info)`
- `PrintFrame(WebCore::FrameIdentifier frameID, String title, WebCore::FloatSize pdfFirstPageSize) -> ()` (sync)
- `RunModal()`
- `NotifyScrollerThumbIsVisibleInRect(WebCore::IntRect scrollerThumb)`
- `RecommendedScrollbarStyleDidChange(int32_t newStyle)`
- `DidChangeScrollbarsForMainFrame(bool hasHorizontalScrollbar, bool hasVerticalScrollbar)`
- `DidChangeScrollOffsetPinningForMainFrame(WebCore::RectEdges<bool> pinnedState)`
- `DidChangePageCount(unsigned pageCount)`
- `ThemeColorChanged(WebCore::Color themeColor)` (if PLATFORM(MAC))
- `PageExtendedBackgroundColorDidChange(WebCore::Color backgroundColor)`
- `SampledPageTopColorChanged(WebCore::Color sampledPageTopColor)`
- `SetCanShortCircuitHorizontalWheelEvents(bool canShortCircuitHorizontalWheelEvents)`
- `DidChangeContentSize(WebCore::IntSize newSize)`
- `DidChangeIntrinsicContentSize(WebCore::IntSize newIntrinsicContentSize)`
- `ShowColorPicker(WebCore::Color initialColor, WebCore::IntRect elementRect, WebKit::ColorControlSupportsAlpha supportsAlpha, Vector<WebCore::Color> suggestions)`
- `SetColorPickerColor(WebCore::Color color)`
- `EndColorPicker()`
- `ShowDataListSuggestions(WebCore::DataListSuggestionInformation suggestionInformation)`
- `HandleKeydownInDataList(String key)`
- `EndDataListSuggestions()`
- `ShowDateTimePicker(WebCore::DateTimeChooserParameters params)`
- `EndDateTimePicker()`
- `DecidePolicyForResponse(WebKit::FrameInfoData frameInfo, std::optional<WebCore::NavigationIdentifier> navigationID, WebCore::ResourceResponse response, WebCore::ResourceRequest request, bool canShowMIMEType, String downloadAttribute, bool isShowingInitialAboutBlank, WebCore::CrossOriginOpenerPolicyValue activeDocumentCOOPValue) -> (WebKit::PolicyDecision PolicyDecision)`
- `DecidePolicyForNavigationActionAsync(WebKit::NavigationActionData data) -> (WebKit::PolicyDecision PolicyDecision)`
- `DecidePolicyForNavigationActionSync(WebKit::NavigationActionData data) -> (WebKit::PolicyDecision PolicyDecision)` (sync)
- `DecidePolicyForNewWindowAction(WebKit::NavigationActionData navigationActionData, String frameName) -> (WebKit::PolicyDecision PolicyDecision)`
- `DidChangeProgress(double value)`
- `DidFinishProgress()`
- `DidStartProgress()`
- `SetNetworkRequestsInProgress(bool networkRequestsInProgress)`
- `StartNetworkRequestsForPageLoadTiming(WebCore::FrameIdentifier frameID)`
- `EndNetworkRequestsForPageLoadTiming(WebCore::FrameIdentifier frameID, WallTime timestamp)`
- `DidCreateSubframe(WebCore::FrameIdentifier parent, WebCore::FrameIdentifier newFrameID, String frameName, WebCore::SandboxFlags sandboxFlags, WebCore::ScrollbarMode scrollingMode)` (CanDispatchOutOfOrder)
- `DidDestroyFrame(WebCore::FrameIdentifier frameID)`
- `DidStartProvisionalLoadForFrame(WebCore::FrameIdentifier frameID, WebKit::FrameInfoData frameInfo, WebCore::ResourceRequest request, std::optional<WebCore::NavigationIdentifier> navigationID, URL url, URL unreachableURL, WebKit::UserData userData, WallTime timestamp)`
- `DidReceiveServerRedirectForProvisionalLoadForFrame(WebCore::FrameIdentifier frameID, std::optional<WebCore::NavigationIdentifier> navigationID, WebCore::ResourceRequest request, WebKit::UserData userData)`
- `WillPerformClientRedirectForFrame(WebCore::FrameIdentifier frameID, String url, double delay, WebCore::LockBackForwardList lockBackForwardList)`
- `DidCancelClientRedirectForFrame(WebCore::FrameIdentifier frameID)`
- `DidChangeProvisionalURLForFrame(WebCore::FrameIdentifier frameID, std::optional<WebCore::NavigationIdentifier> navigationID, URL url)`
- `DidFailProvisionalLoadForFrame(WebKit::FrameInfoData frameInfo, WebCore::ResourceRequest request, std::optional<WebCore::NavigationIdentifier> navigationID, String provisionalURL, WebCore::ResourceError error, WebCore::WillContinueLoading willContinueLoading, WebKit::UserData userData, WebCore::WillInternallyHandleFailure willInternallyHandleFailure)`
- `DidCommitLoadForFrame(WebCore::FrameIdentifier frameID, WebKit::FrameInfoData frameInfo, WebCore::ResourceRequest request, std::optional<WebCore::NavigationIdentifier> navigationID, String mimeType, bool hasCustomContentProvider, WebCore::FrameLoadType loadType, WebCore::CertificateInfo certificateInfo, bool usedLegacyTLS, bool wasPrivateRelayed, String proxyName, WebCore::ResourceResponseSource source, bool containsPluginDocument, WebCore::HasInsecureContent hasInsecureContent, WebCore::MouseEventPolicy mouseEventPolicy, WebKit::UserData userData)`
- `DidFailLoadForFrame(WebCore::FrameIdentifier frameID, WebKit::FrameInfoData frameInfo, WebCore::ResourceRequest request, std::optional<WebCore::NavigationIdentifier> navigationID, WebCore::ResourceError error, WebKit::UserData userData)`
- `DidFinishDocumentLoadForFrame(WebCore::FrameIdentifier frameID, std::optional<WebCore::NavigationIdentifier> navigationID, WebKit::UserData userData, WallTime timestamp)`
- `DidFinishLoadForFrame(WebCore::FrameIdentifier frameID, WebKit::FrameInfoData frameInfo, WebCore::ResourceRequest request, std::optional<WebCore::NavigationIdentifier> navigationID, WebKit::UserData userData)`
- `DidFirstLayoutForFrame(WebCore::FrameIdentifier frameID, WebKit::UserData userData)`
- `DidFirstVisuallyNonEmptyLayoutForFrame(WebCore::FrameIdentifier frameID, WebKit::UserData userData, WallTime timestamp)`
- `DidReachLayoutMilestone(OptionSet<WebCore::LayoutMilestone> layoutMilestones, WallTime timestamp)`
- `DidReceiveTitleForFrame(WebCore::FrameIdentifier frameID, String title, WebKit::UserData userData)`
- `DidDisplayInsecureContentForFrame(WebCore::FrameIdentifier frameID, WebKit::UserData userData)`
- `DidRunInsecureContentForFrame(WebCore::FrameIdentifier frameID, WebKit::UserData userData)`
- `DidSameDocumentNavigationForFrame(WebCore::FrameIdentifier frameID, std::optional<WebCore::NavigationIdentifier> navigationID, WebKit::SameDocumentNavigationType type, URL url, WebKit::UserData userData)`
- `DidSameDocumentNavigationForFrameViaJS(WebKit::SameDocumentNavigationType type, URL url, WebKit::NavigationActionData navigationActionData, WebKit::UserData userData)`
- `DidChangeMainDocument(WebCore::FrameIdentifier frameID, std::optional<WebCore::NavigationIdentifier> navigationID)`
- `DidExplicitOpenForFrame(WebCore::FrameIdentifier frameID, URL url, String mimeType)`
- `DidDestroyNavigation(WebCore::NavigationIdentifier navigationID)`
- `UpdateSandboxFlags(WebCore::FrameIdentifier frameID, WebCore::SandboxFlags sandboxFlags)`
- `UpdateOpener(WebCore::FrameIdentifier frameID, WebCore::FrameIdentifier newOpener)`
- `UpdateScrollingMode(WebCore::FrameIdentifier frameID, WebCore::ScrollbarMode scrollingMode)`
- `UpdateRemoteFrameSize(WebCore::FrameIdentifier frameID, WebCore::IntSize size)`
- `ResolveAccessibilityHitTestForTesting(WebCore::FrameIdentifier frameID, WebCore::IntPoint point) -> (String result)`
- `MainFramePluginHandlesPageScaleGestureDidChange(bool mainFramePluginHandlesPageScaleGesture, double minScale, double maxScale)`
- `DidInitiateLoadForResource(WebCore::ResourceLoaderIdentifier resourceID, WebCore::FrameIdentifier frameID, WebCore::ResourceRequest request)` (if PLATFORM(GTK) || PLATFORM(WPE))
- `DidSendRequestForResource(WebCore::ResourceLoaderIdentifier resourceID, WebCore::FrameIdentifier frameID, WebCore::ResourceRequest request, WebCore::ResourceResponse redirectResponse)` (if PLATFORM(GTK) || PLATFORM(WPE))
- `DidReceiveResponseForResource(WebCore::ResourceLoaderIdentifier resourceID, WebCore::FrameIdentifier frameID, WebCore::ResourceResponse response)` (if PLATFORM(GTK) || PLATFORM(WPE))
- `DidFinishLoadForResource(WebCore::ResourceLoaderIdentifier resourceID, WebCore::FrameIdentifier frameID, WebCore::ResourceError error)` (if PLATFORM(GTK) || PLATFORM(WPE))
- `DidNavigateWithNavigationData(WebKit::WebNavigationDataStore store, WebCore::FrameIdentifier frameID)`
- `DidPerformClientRedirect(String sourceURLString, String destinationURLString, WebCore::FrameIdentifier frameID)`
- `DidPerformServerRedirect(String sourceURLString, String destinationURLString, WebCore::FrameIdentifier frameID)`
- `DidUpdateHistoryTitle(String title, String url, WebCore::FrameIdentifier frameID)`
- `DidFinishLoadingDataForCustomContentProvider(String suggestedFilename, std::span<const uint8_t> data)`
- `WillSubmitForm(WebCore::FrameIdentifier frameID, WebCore::FrameIdentifier sourceFrameID, Vector<std::pair<String, String>> textFieldValues, WebKit::UserData userData) -> ()`
- `InterpretKeyEvent(WebKit::EditorState state, bool isCharEvent) -> (bool handled)` (sync, if PLATFORM(IOS_FAMILY))
- `DidReceivePositionInformation(WebKit::InteractionInformationAtPosition information)` (CanDispatchOutOfOrder, if PLATFORM(IOS_FAMILY))
- `SaveImageToLibrary(WebCore::SharedMemory::Handle handle, String authorizationToken)` (if PLATFORM(IOS_FAMILY))
- `ShowPlaybackTargetPicker(bool hasVideo, WebCore::IntRect elementRect, WebCore::RouteSharingPolicy policy, String routingContextUID)` (if PLATFORM(IOS_FAMILY))
- `CommitPotentialTapFailed()` (if PLATFORM(IOS_FAMILY))
- `DidNotHandleTapAsClick(WebCore::IntPoint point)` (if PLATFORM(IOS_FAMILY))
- `DidCompleteSyntheticClick()` (if PLATFORM(IOS_FAMILY))
- `DidHandleTapAsHover()` (if PLATFORM(IOS_FAMILY))
- `DisableDoubleTapGesturesDuringTapIfNecessary(WebKit::TapIdentifier requestID)` (if PLATFORM(IOS_FAMILY))
- `HandleSmartMagnificationInformationForPotentialTap(WebKit::TapIdentifier requestID, WebCore::FloatRect renderRect, bool fitEntireRect, double viewportMinimumScale, double viewportMaximumScale, bool nodeIsRootLevel)` (if PLATFORM(IOS_FAMILY))
- `IsPotentialTapInProgress() -> (bool result)` (if PLATFORM(IOS_FAMILY))
- `SetDataDetectionResult(WebKit::DataDetectionResult dataDetectionResult)` (if ENABLE(DATA_DETECTION))
- `HandleClickForDataDetectionResult(WebCore::DataDetectorElementInfo info, WebCore::IntPoint location)` (if ENABLE(DATA_DETECTION))
- `PageScaleFactorDidChange(double scaleFactor)`
- `ViewScaleFactorDidChange(double scaleFactor)`
- `PluginScaleFactorDidChange(double zoomFactor)`
- `PluginZoomFactorDidChange(double zoomFactor)`
- `BindAccessibilityTree(String plugID)` (if PLATFORM(GTK) || PLATFORM(WPE))
- `SetInputMethodState(std::optional<WebKit::InputMethodState> state)` (if PLATFORM(GTK) || PLATFORM(WPE))
- `BackForwardAddItem(Ref<WebKit::FrameState> navigatedFrameState)`
- `BackForwardSetChildItem(WebCore::BackForwardFrameItemIdentifier frameItemID, Ref<WebKit::FrameState> frameState)`
- `BackForwardClearChildren(WebCore::BackForwardItemIdentifier itemID, WebCore::BackForwardFrameItemIdentifier frameItemID)`
- `BackForwardUpdateItem(Ref<WebKit::FrameState> frameState)`
- `BackForwardGoToItem(WebCore::BackForwardItemIdentifier itemID) -> (WebKit::WebBackForwardListCounts counts)` (sync)
- `BackForwardItemAtIndex(int32_t itemIndex, WebCore::FrameIdentifier frameID) -> (RefPtr<WebKit::FrameState> frameState)` (sync)
- `BackForwardListContainsItem(WebCore::BackForwardItemIdentifier itemID) -> (bool contains)` (sync)
- `BackForwardListCounts() -> (WebKit::WebBackForwardListCounts counts)` (sync)
- `ShouldGoToBackForwardListItemSync(WebCore::BackForwardItemIdentifier itemID, bool isBackForwardCache) -> (bool shouldGoToItem)` (sync)
- `RegisterEditCommandForUndo(uint64_t commandID, String label)` (AllowedWhenWaitingForSyncReply)
- `ClearAllEditCommands()`
- `RegisterInsertionUndoGrouping()`
- `CanUndoRedo(WebKit::UndoOrRedo undoOrRedo) -> (bool result)` (sync)
- `ExecuteUndoRedo(WebKit::UndoOrRedo undoOrRedo) -> ()` (sync)
- `LogDiagnosticMessageFromWebProcess(String message, String description, WebCore::ShouldSample shouldSample)`
- `LogDiagnosticMessageWithResultFromWebProcess(String message, String description, uint32_t result, WebCore::ShouldSample shouldSample)`
- `LogDiagnosticMessageWithValueFromWebProcess(String message, String description, double value, unsigned significantFigures, WebCore::ShouldSample shouldSample)`
- `LogDiagnosticMessageWithEnhancedPrivacyFromWebProcess(String message, String description, WebCore::ShouldSample shouldSample)`
- `LogDiagnosticMessageWithValueDictionaryFromWebProcess(String message, String description, WebCore::DiagnosticLoggingDictionary value, WebCore::ShouldSample shouldSample)`
- `LogDiagnosticMessageWithDomainFromWebProcess(String message, WebCore::DiagnosticLoggingDomain domain)`
- `LogScrollingEvent(uint32_t eventType, MonotonicTime timestamp, uint64_t data)`
- `EditorStateChanged(WebKit::EditorState editorState)`
- `CompositionWasCanceled()`
- `SetHasFocusedElementWithUserInteraction(bool hasFocusedElement)`
- `RequestTextRecognition(URL imageURL, WebCore::ShareableBitmapHandle imageData, String source, String target) -> (WebCore::TextRecognitionResult result)` (if ENABLE(IMAGE_ANALYSIS))
- `HandleContextMenuTranslation(WebCore::TranslationContextMenuInfo info)` (if HAVE(TRANSLATION_UI_SERVICES) && ENABLE(CONTEXT_MENUS))
- `ProofreadingSessionShowDetailsForSuggestionWithIDRelativeToRect(WebCore::WritingTools::TextSuggestion::ID replacementID, WebCore::IntRect selectionBoundsInRootView)` (if ENABLE(WRITING_TOOLS))
- `ProofreadingSessionUpdateStateForSuggestionWithID(WebCore::WritingTools::TextSuggestionState state, WebCore::WritingTools::TextSuggestion::ID replacementID)` (if ENABLE(WRITING_TOOLS))
- `AddTextAnimationForAnimationID(WTF::UUID uuid, WebCore::TextAnimationData styleData, WebCore::TextIndicatorData indicatorData)` (if ENABLE(WRITING_TOOLS))
- `AddTextAnimationForAnimationIDWithCompletionHandler(WTF::UUID uuid, WebCore::TextAnimationData styleData, WebCore::TextIndicatorData indicatorData) -> (WebCore::TextAnimationRunMode runMode)` (if ENABLE(WRITING_TOOLS))
- `RemoveTextAnimationForAnimationID(WTF::UUID uuid)` (if ENABLE(WRITING_TOOLS))
- `DidEndPartialIntelligenceTextAnimation()` (if ENABLE(WRITING_TOOLS))
- `ShowMediaControlsContextMenu(WebCore::FloatRect targetFrame, Vector<WebCore::MediaControlsContextMenuItem> items) -> (WebCore::MediaControlsContextMenuItem::ID selectedItemID)` (if ENABLE(MEDIA_CONTROLS_CONTEXT_MENUS) && USE(UICONTEXTMENU))
- `SetIsTouchBarUpdateSuppressedForHiddenContentEditable(bool isTouchBarUpdateSuppressed)` (if HAVE(TOUCH_BAR))
- `SetIsNeverRichlyEditableForTouchBar(bool isNeverRichlyEditable)` (if HAVE(TOUCH_BAR))
- `RequestDOMPasteAccess(WebCore::DOMPasteAccessCategory pasteAccessCategory, WebCore::FrameIdentifier frameID, WebCore::IntRect elementRect, String originIdentifier) -> (WebCore::DOMPasteAccessResponse response)` (sync)
- `SetTextIndicatorFromFrame(WebCore::FrameIdentifier frameID, WebCore::TextIndicatorData indicator, uint64_t lifetime)`
- `ClearTextIndicator()`
- `DidGetImageForFindMatch(WebCore::ImageBufferParameters parameters, WebCore::ShareableBitmapHandle contentImageHandle, uint32_t matchIndex)`
- `ShowPopupMenuFromFrame(WebCore::FrameIdentifier frameID, WebCore::IntRect rect, uint64_t textDirection, Vector<WebKit::WebPopupItem> items, int32_t selectedIndex, WebKit::PlatformPopupMenuData data)`
- `HidePopupMenu()`
- `ShowContextMenu(WebKit::ContextMenuContextData contextMenuContextData, WebKit::UserData userData)` (if ENABLE(CONTEXT_MENUS))
- `ShowContextMenuFromFrame(WebCore::FrameIdentifier frameID, WebKit::ContextMenuContextData contextMenuContextData, WebKit::UserData userData)` (if ENABLE(CONTEXT_MENUS))
- `DidFinishServiceWorkerPageRegistration(bool success)`
- `ExceededDatabaseQuota(WebCore::FrameIdentifier frameID, String originIdentifier, String databaseName, String databaseDisplayName, uint64_t currentQuota, uint64_t currentOriginUsage, uint64_t currentDatabaseUsage, uint64_t expectedUsage) -> (uint64_t newQuota)` (sync)
- `RequestGeolocationPermissionForFrame(WebKit::GeolocationIdentifier geolocationID, WebKit::FrameInfoData frameInfo)`
- `RevokeGeolocationAuthorizationToken(String authorizationToken)`
- `RequestUserMediaPermissionForFrame(WebCore::UserMediaRequestIdentifier userMediaID, WebCore::FrameIdentifier frameID, WebCore::SecurityOriginData userMediaDocumentOriginIdentifier, WebCore::SecurityOriginData topLevelDocumentOriginIdentifier, WebCore::MediaStreamRequest request)` (if ENABLE(MEDIA_STREAM))
- `EnumerateMediaDevicesForFrame(WebCore::FrameIdentifier frameID, WebCore::SecurityOriginData userMediaDocumentOriginIdentifier, WebCore::SecurityOriginData topLevelDocumentOriginIdentifier) -> (Vector<WebCore::CaptureDeviceWithCapabilities> devices, WebCore::MediaDeviceHashSalts mediaDeviceIdentifierHashSalts)` (if ENABLE(MEDIA_STREAM))
- `BeginMonitoringCaptureDevices()` (if ENABLE(MEDIA_STREAM))
- `ValidateCaptureStateUpdate(WebCore::UserMediaRequestIdentifier userMediaID, WebCore::ClientOrigin clientOrigin, WebCore::FrameIdentifier frameID, bool isActive, WebCore::MediaProducerMediaCaptureKind kind) -> (std::optional<WebCore::Exception> result)` (if ENABLE(MEDIA_STREAM))
- `SetShouldListenToVoiceActivity(bool shouldListen)` (if ENABLE(MEDIA_STREAM))
- `RequestMediaKeySystemPermissionForFrame(WebCore::MediaKeySystemRequestIdentifier mediaKeySystemID, WebCore::FrameIdentifier frameID, WebCore::SecurityOriginData topLevelDocumentOriginIdentifier, String keySystem)` (if ENABLE(ENCRYPTED_MEDIA))
- `RequestNotificationPermission(String originIdentifier) -> (bool allowed)`
- `CheckTextOfParagraph(String text, OptionSet<WebCore::TextCheckingType> checkingTypes, int32_t insertionPoint) -> (Vector<WebCore::TextCheckingResult> results)` (sync, if USE(UNIFIED_TEXT_CHECKING))
- `CheckSpellingOfString(String text) -> (int32_t misspellingLocation, int32_t misspellingLength)` (sync)
- `CheckGrammarOfString(String text) -> (Vector<WebCore::GrammarDetail> results, int32_t badGrammarLocation, int32_t badGrammarLength)` (sync)
- `SpellingUIIsShowing() -> (bool isShowing)` (sync)
- `UpdateSpellingUIWithMisspelledWord(String misspelledWord)`
- `UpdateSpellingUIWithGrammarString(String badGrammarPhrase, WebCore::GrammarDetail grammarDetail)`
- `GetGuessesForWord(String word, String context, int32_t insertionPoint) -> (Vector<String> guesses)` (sync)
- `LearnWord(String word)`
- `IgnoreWord(String word)`
- `RequestCheckingOfString(WebKit::TextCheckerRequestID requestID, WebCore::TextCheckingRequestData request, int32_t insertionPoint)`
- `StartDrag(WebCore::DragItem dragItem, WebCore::ShareableBitmapHandle dragImage)` (if PLATFORM(COCOA) && ENABLE(DRAG_SUPPORT))
- `SetPromisedDataForImage(String pasteboardName, WebCore::SharedMemory::Handle imageHandle, String filename, String extension, String title, String url, String visibleURL, WebCore::SharedMemory::Handle archiveHandle, String originIdentifier)` (if PLATFORM(COCOA) && ENABLE(DRAG_SUPPORT))
- `StartDrag(WebCore::SelectionData selectionData, OptionSet<WebCore::DragOperation> dragOperationMask, std::optional<WebCore::ShareableBitmapHandle> dragImage, WebCore::IntPoint dragImageHotspot)` (if PLATFORM(GTK) && ENABLE(DRAG_SUPPORT))
- `DidHandleDragStartRequest(bool started)` (if PLATFORM(IOS_FAMILY) && ENABLE(DRAG_SUPPORT))
- `DidHandleAdditionalDragItemsRequest(bool added)` (if PLATFORM(IOS_FAMILY) && ENABLE(DRAG_SUPPORT))
- `WillReceiveEditDragSnapshot()` (if PLATFORM(IOS_FAMILY) && ENABLE(DRAG_SUPPORT))
- `DidReceiveEditDragSnapshot(std::optional<WebCore::TextIndicatorData> textIndicator)` (if PLATFORM(IOS_FAMILY) && ENABLE(DRAG_SUPPORT))
- `DidPerformDictionaryLookup(WebCore::DictionaryPopupInfo dictionaryPopupInfo)` (if PLATFORM(COCOA))
- `ExecuteSavedCommandBySelector(String selector) -> (bool handled)` (sync, if PLATFORM(COCOA))
- `RegisterWebProcessAccessibilityToken(std::span<const uint8_t> data)` (if PLATFORM(COCOA))
- `GetIsSpeaking() -> (bool isSpeaking)` (sync, if PLATFORM(COCOA))
- `MakeFirstResponder()` (if PLATFORM(COCOA))
- `AssistiveTechnologyMakeFirstResponder()` (if PLATFORM(COCOA))
- `SearchTheWeb(String string)` (if PLATFORM(COCOA))
- `SubstitutionsPanelIsShowing() -> (bool isShowing)` (sync, if USE(APPKIT))
- `toggleSmartInsertDelete()` (if USE(AUTOMATIC_TEXT_REPLACEMENT))
- `toggleAutomaticQuoteSubstitution()` (if USE(AUTOMATIC_TEXT_REPLACEMENT))
- `toggleAutomaticLinkDetection()` (if USE(AUTOMATIC_TEXT_REPLACEMENT))
- `toggleAutomaticDashSubstitution()` (if USE(AUTOMATIC_TEXT_REPLACEMENT))
- `toggleAutomaticTextReplacement()` (if USE(AUTOMATIC_TEXT_REPLACEMENT))
- `ShowCorrectionPanel(WebCore::AlternativeTextType panelType, WebCore::FloatRect boundingBoxOfReplacedString, String replacedString, String replacementString, Vector<String> alternativeReplacementStrings)` (if PLATFORM(MAC))
- `DismissCorrectionPanel(WebCore::ReasonForDismissingAlternativeText reason)` (if PLATFORM(MAC))
- `DismissCorrectionPanelSoon(WebCore::ReasonForDismissingAlternativeText reason) -> (String result)` (sync, if PLATFORM(MAC))
- `RecordAutocorrectionResponse(WebCore::AutocorrectionResponse response, String replacedString, String replacementString)` (if PLATFORM(MAC))
- `SetEditableElementIsFocused(bool editableElementIsFocused)` (if PLATFORM(MAC))
- `HandleAcceptsFirstMouse(bool acceptsFirstMouse)` (CanDispatchOutOfOrder, if PLATFORM(MAC))
- `DidUpdateRenderingAfterCommittingLoad()`
- `ShowDictationAlternativeUI(WebCore::FloatRect boundingBoxOfDictatedText, WebCore::DictationContext dictationContext)` (if USE(DICTATION_ALTERNATIVES))
- `RemoveDictationAlternatives(WebCore::DictationContext dictationContext)` (if USE(DICTATION_ALTERNATIVES))
- `DictationAlternatives(WebCore::DictationContext dictationContext) -> (Vector<String> alternatives)` (sync, if USE(DICTATION_ALTERNATIVES))
- `BeginTextRecognitionForVideoInElementFullScreen(WebCore::MediaPlayerIdentifier identifier, WebCore::FloatRect videoBounds)` (if ENABLE(IMAGE_ANALYSIS) && ENABLE(VIDEO))
- `CancelTextRecognitionForVideoInElementFullScreen()` (if ENABLE(IMAGE_ANALYSIS) && ENABLE(VIDEO))
- `CouldNotRestorePageState()` (if PLATFORM(IOS_FAMILY))
- `RestorePageState(std::optional<WebCore::FloatPoint> scrollPosition, WebCore::FloatPoint scrollOrigin, WebCore::FloatBoxExtent obscuredInsetsOnSave, double scale)` (if PLATFORM(IOS_FAMILY))
- `RestorePageCenterAndScale(std::optional<WebCore::FloatPoint> unobscuredCenter, double scale)` (if PLATFORM(IOS_FAMILY))
- `DidGetTapHighlightGeometries(WebKit::TapIdentifier requestID, WebCore::Color color, Vector<WebCore::FloatQuad> geometries, WebCore::IntSize topLeftRadius, WebCore::IntSize topRightRadius, WebCore::IntSize bottomLeftRadius, WebCore::IntSize bottomRightRadius, bool nodeHasBuiltInClickHandling)` (if PLATFORM(IOS_FAMILY))
- `ElementDidFocus(WebKit::FocusedElementInformation information, bool userIsInteracting, bool blurPreviousNode, OptionSet<WebCore::ActivityState> activityStateChanges, WebKit::UserData userData)` (if PLATFORM(IOS_FAMILY))
- `ElementDidBlur()` (if PLATFORM(IOS_FAMILY))
- `UpdateInputContextAfterBlurringAndRefocusingElement()` (if PLATFORM(IOS_FAMILY))
- `DidProgrammaticallyClearFocusedElement(WebCore::ElementContext context)` (if PLATFORM(IOS_FAMILY))
- `UpdateFocusedElementInformation(WebKit::FocusedElementInformation information)` (if PLATFORM(IOS_FAMILY))
- `FocusedElementDidChangeInputMode(WebCore::InputMode mode)` (if PLATFORM(IOS_FAMILY))
- `ScrollingNodeScrollWillStartScroll(std::optional<WebCore::ScrollingNodeID> nodeID)` (if PLATFORM(IOS_FAMILY))
- `ScrollingNodeScrollDidEndScroll(std::optional<WebCore::ScrollingNodeID> nodeID)` (if PLATFORM(IOS_FAMILY))
- `ShowInspectorHighlight(WebCore::InspectorOverlayHighlight highlight)` (if PLATFORM(IOS_FAMILY))
- `HideInspectorHighlight()` (if PLATFORM(IOS_FAMILY))
- `ShowInspectorIndication()` (if PLATFORM(IOS_FAMILY))
- `HideInspectorIndication()` (if PLATFORM(IOS_FAMILY))
- `EnableInspectorNodeSearch()` (if PLATFORM(IOS_FAMILY))
- `DisableInspectorNodeSearch()` (if PLATFORM(IOS_FAMILY))
- `UpdateStringForFind(String findString)` (if PLATFORM(IOS_FAMILY))
- `HandleAutocorrectionContext(WebKit::WebAutocorrectionContext context)` (CanDispatchOutOfOrder, if PLATFORM(IOS_FAMILY))
- `ShowDataDetectorsUIForPositionInformation(WebKit::InteractionInformationAtPosition information)` (if PLATFORM(IOS_FAMILY))
- `DidChangeInspectorFrontendCount(uint32_t count)`
- `CreateInspectorTarget(String targetId, Inspector::InspectorTargetType type)`
- `DestroyInspectorTarget(String targetId)`
- `SendMessageToInspectorFrontend(String targetId, String message)`
- `SaveRecentSearches(String name, Vector<WebCore::RecentSearch> searchItems)`
- `LoadRecentSearches(String name) -> (Vector<WebCore::RecentSearch> result)` (sync)
- `DidUpdateActivityState()` (CanDispatchOutOfOrder)
- `WrapCryptoKey(Vector<uint8_t> key) -> (std::optional<Vector<uint8_t>> wrappedKey)` (sync)
- `SerializeAndWrapCryptoKey(WebCore::CryptoKeyData key) -> (std::optional<Vector<uint8_t>> wrappedKey)` (sync)
- `UnwrapCryptoKey(WebCore::WrappedCryptoKey wrappedKey) -> (std::optional<Vector<uint8_t>> key)` (sync)
- `ShowTelephoneNumberMenu(String telephoneNumber, WebCore::IntPoint point, WebCore::IntRect rect)` (if (ENABLE(TELEPHONE_NUMBER_DETECTION) && PLATFORM(MAC)))
- `DidStartLoadForQuickLookDocumentInMainFrame(String fileName, String uti)` (if USE(QUICK_LOOK))
- `DidFinishLoadForQuickLookDocumentInMainFrame(WebCore::ShareableResourceHandle resource)` (if USE(QUICK_LOOK))
- `RequestPasswordForQuickLookDocumentInMainFrame(String fileName) -> (String password)` (if USE(QUICK_LOOK))
- `ContentFilterDidBlockLoadForFrame(WebCore::ContentFilterUnblockHandler unblockHandler, WebCore::FrameIdentifier frameID)` (if ENABLE(CONTENT_FILTERING))
- `IsAnyAnimationAllowedToPlayDidChange(bool anyAnimationCanPlay)` (if ENABLE(ACCESSIBILITY_ANIMATION_CONTROL))
- `IsPlayingMediaDidChange(OptionSet<WebCore::MediaProducerMediaState> state)`
- `HandleAutoplayEvent(WebCore::AutoplayEvent event, OptionSet<WebCore::AutoplayEventFlags> flags)`
- `DidPerformImmediateActionHitTest(WebKit::WebHitTestResultData result, bool contentPreventsDefault, WebKit::UserData userData)` (CanDispatchOutOfOrder, if PLATFORM(MAC))
- `HandleMessage(String messageName, WebKit::UserData messageBody)`
- `HandleMessageWithAsyncReply(String messageName, WebKit::UserData messageBody) -> (WebKit::UserData reply)`
- `HandleSynchronousMessage(String messageName, WebKit::UserData messageBody) -> (WebKit::UserData returnData)` (sync)
- `HandleAutoFillButtonClick(WebKit::UserData userData)`
- `DidResignInputElementStrongPasswordAppearance(WebKit::UserData userData)`
- `PerformSwitchHapticFeedback()`
- `ContentRuleListNotification(URL url, WebCore::ContentRuleListResults results)` (if ENABLE(CONTENT_EXTENSIONS))
- `AddPlaybackTargetPickerClient(WebCore::PlaybackTargetClientContextIdentifier contextId)` (if ENABLE(WIRELESS_PLAYBACK_TARGET) && !PLATFORM(IOS_FAMILY))
- `RemovePlaybackTargetPickerClient(WebCore::PlaybackTargetClientContextIdentifier contextId)` (if ENABLE(WIRELESS_PLAYBACK_TARGET) && !PLATFORM(IOS_FAMILY))
- `ShowPlaybackTargetPicker(WebCore::PlaybackTargetClientContextIdentifier contextId, WebCore::FloatRect pickerLocation, bool hasVideo)` (if ENABLE(WIRELESS_PLAYBACK_TARGET) && !PLATFORM(IOS_FAMILY))
- `PlaybackTargetPickerClientStateDidChange(WebCore::PlaybackTargetClientContextIdentifier contextId, OptionSet<WebCore::MediaProducerMediaState> mediaState)` (if ENABLE(WIRELESS_PLAYBACK_TARGET) && !PLATFORM(IOS_FAMILY))
- `SetMockMediaPlaybackTargetPickerEnabled(bool enabled)` (if ENABLE(WIRELESS_PLAYBACK_TARGET) && !PLATFORM(IOS_FAMILY))
- `SetMockMediaPlaybackTargetPickerState(String name, WebCore::MediaPlaybackTargetContextMockState pickerState)` (if ENABLE(WIRELESS_PLAYBACK_TARGET) && !PLATFORM(IOS_FAMILY))
- `MockMediaPlaybackTargetPickerDismissPopup()` (if ENABLE(WIRELESS_PLAYBACK_TARGET) && !PLATFORM(IOS_FAMILY))
- `SetMockVideoPresentationModeEnabled(bool enabled)` (if ENABLE(VIDEO_PRESENTATION_MODE))
- `RequestPointerLock()` (if ENABLE(POINTER_LOCK))
- `RequestPointerUnlock()` (if ENABLE(POINTER_LOCK))
- `DidFailToSuspendAfterProcessSwap()`
- `DidSuspendAfterProcessSwap()`
- `ImageOrMediaDocumentSizeChanged(WebCore::IntSize newSize)`
- `UseFixedLayoutDidChange(bool useFixedLayout)`
- `FixedLayoutSizeDidChange(WebCore::IntSize fixedLayoutSize)`
- `DidRestoreScrollPosition()`
- `RequestScrollToRect(WebCore::FloatRect targetRect, WebCore::FloatPoint origin)`
- `GetLoadDecisionForIcon(WebCore::LinkIcon icon, WebKit::CallbackID callbackID)`
- `StartURLSchemeTask(WebKit::URLSchemeTaskParameters parameters)`
- `StopURLSchemeTask(WebKit::WebURLSchemeHandlerIdentifier handlerIdentifier, WebCore::ResourceLoaderIdentifier taskIdentifier)`
- `LoadSynchronousURLSchemeTask(WebKit::URLSchemeTaskParameters parameters) -> (WebCore::ResourceResponse response, WebCore::ResourceError error, Vector<uint8_t> data)` (sync)
- `ShouldAllowDeviceOrientationAndMotionAccess(WebCore::FrameIdentifier frameID, WebKit::FrameInfoData frameInfo, bool mayPrompt) -> (WebCore::DeviceOrientationOrMotionPermissionState permissionState)` (if ENABLE(DEVICE_ORIENTATION))
- `RegisterAttachmentIdentifierFromData(String identifier, String contentType, String preferredFileName, IPC::SharedBufferReference data)` (if ENABLE(ATTACHMENT_ELEMENT))
- `RegisterAttachmentIdentifierFromFilePath(String identifier, String contentType, String filePath)` (if ENABLE(ATTACHMENT_ELEMENT))
- `RegisterAttachmentIdentifier(String identifier)` (if ENABLE(ATTACHMENT_ELEMENT))
- `RegisterAttachmentsFromSerializedData(Vector<WebCore::SerializedAttachmentData> data)` (if ENABLE(ATTACHMENT_ELEMENT))
- `CloneAttachmentData(String fromIdentifier, String toIdentifier)` (if ENABLE(ATTACHMENT_ELEMENT))
- `DidInsertAttachmentWithIdentifier(String identifier, String source, WebCore::AttachmentAssociatedElementType associatedElementType)` (if ENABLE(ATTACHMENT_ELEMENT))
- `DidRemoveAttachmentWithIdentifier(String identifier)` (if ENABLE(ATTACHMENT_ELEMENT))
- `SerializedAttachmentDataForIdentifiers(Vector<String> identifiers) -> (Vector<WebCore::SerializedAttachmentData> seralizedData)` (sync, if ENABLE(ATTACHMENT_ELEMENT))
- `WritePromisedAttachmentToPasteboard(WebCore::PromisedAttachmentInfo info, String authorizationToken)` (if (ENABLE(ATTACHMENT_ELEMENT) && PLATFORM(IOS_FAMILY)))
- `RequestAttachmentIcon(String identifier, String contentType, String path, String title, WebCore::FloatSize size)` (if ENABLE(ATTACHMENT_ELEMENT))
- `SpeechSynthesisVoiceList() -> (Vector<WebKit::WebSpeechSynthesisVoice> voiceList)` (sync, if ENABLE(SPEECH_SYNTHESIS))
- `SpeechSynthesisSpeak(String text, String lang, float volume, float rate, float pitch, MonotonicTime startTime, String voiceURI, String voiceName, String voiceLang, bool localService, bool defaultVoice) -> ()` (if ENABLE(SPEECH_SYNTHESIS))
- `SpeechSynthesisSetFinishedCallback() -> ()` (if ENABLE(SPEECH_SYNTHESIS))
- `SpeechSynthesisCancel()` (if ENABLE(SPEECH_SYNTHESIS))
- `SpeechSynthesisPause() -> ()` (if ENABLE(SPEECH_SYNTHESIS))
- `SpeechSynthesisResume() -> ()` (if ENABLE(SPEECH_SYNTHESIS))
- `SpeechSynthesisResetState()` (if ENABLE(SPEECH_SYNTHESIS))
- `ShowPDFContextMenu(WebKit::PDFContextMenu contextMenu, WebKit::PDFPluginIdentifier identifier) -> (std::optional<int32_t> selectedItem)` (if (ENABLE(PDF_PLUGIN) && PLATFORM(MAC)))
- `PluginDidInstallPDFDocument(double initialScale)` (if (ENABLE(PDF_PLUGIN) && PLATFORM(IOS_FAMILY)))
- `CreatePDFHUD(WebKit::PDFPluginIdentifier identifier, WebCore::IntRect boundingBox)` (if ENABLE(PDF_HUD))
- `UpdatePDFHUDLocation(WebKit::PDFPluginIdentifier identifier, WebCore::IntRect boundingBox)` (if ENABLE(PDF_HUD))
- `RemovePDFHUD(WebKit::PDFPluginIdentifier identifier)` (if ENABLE(PDF_HUD))
- `ConfigureLoggingChannel(String channelName, WTFLogChannelState state, WTFLogLevel level)`
- `ShowEmojiPicker(WebCore::IntRect caretRect) -> (String result)` (if PLATFORM(GTK))
- `DidCreateContextInWebProcessForVisibilityPropagation(WebKit::LayerHostingContextID contextID)` (if HAVE(VISIBILITY_PROPAGATION_VIEW))
- `SetMockWebAuthenticationConfiguration(WebCore::MockWebAuthenticationConfiguration configuration)` (if ENABLE(WEB_AUTHN))
- `SendMessageToWebView(WebKit::UserMessage userMessage)` (if PLATFORM(GTK) || PLATFORM(WPE))
- `SendMessageToWebViewWithReply(WebKit::UserMessage userMessage) -> (WebKit::UserMessage replyMessage)` (if PLATFORM(GTK) || PLATFORM(WPE))
- `DidFindTextManipulationItems(Vector<WebCore::TextManipulationItem> items)`
- `AddMediaUsageManagerSession(WebCore::MediaSessionIdentifier identifier, String bundleIdentifier, URL pageURL)` (if ENABLE(MEDIA_USAGE))
- `UpdateMediaUsageManagerSessionState(WebCore::MediaSessionIdentifier identifier, WebCore::MediaUsageInfo info)` (if ENABLE(MEDIA_USAGE))
- `RemoveMediaUsageManagerSession(WebCore::MediaSessionIdentifier identifier)` (if ENABLE(MEDIA_USAGE))
- `SetHasExecutedAppBoundBehaviorBeforeNavigation()`
- `ChangeUniversalAccessZoomFocus(WebCore::IntRect viewRect, WebCore::IntRect caretRect)` (if PLATFORM(MAC))
- `TakeModelElementFullscreen(WebKit::ModelIdentifier modelIdentifier)` (if ENABLE(ARKIT_INLINE_PREVIEW_IOS))
- `ModelElementSetInteractionEnabled(WebKit::ModelIdentifier modelIdentifier, bool isInteractionEnabled)` (if ENABLE(ARKIT_INLINE_PREVIEW_IOS))
- `ModelElementCreateRemotePreview(String uuid, WebCore::FloatSize size) -> (Expected<std::pair<String, uint32_t>, WebCore::ResourceError> result)` (if ENABLE(ARKIT_INLINE_PREVIEW_MAC))
- `ModelElementLoadRemotePreview(String uuid, URL url) -> (std::optional<WebCore::ResourceError> error)` (if ENABLE(ARKIT_INLINE_PREVIEW_MAC))
- `ModelElementDestroyRemotePreview(String uuid)` (if ENABLE(ARKIT_INLINE_PREVIEW_MAC))
- `ModelElementSizeDidChange(String uuid, WebCore::FloatSize size) -> (Expected<MachSendRight, WebCore::ResourceError> result)` (if ENABLE(ARKIT_INLINE_PREVIEW_MAC))
- `HandleMouseDownForModelElement(String uuid, WebCore::LayoutPoint flippedLocationInElement, MonotonicTime timestamp)` (if ENABLE(ARKIT_INLINE_PREVIEW_MAC))
- `HandleMouseMoveForModelElement(String uuid, WebCore::LayoutPoint flippedLocationInElement, MonotonicTime timestamp)` (if ENABLE(ARKIT_INLINE_PREVIEW_MAC))
- `HandleMouseUpForModelElement(String uuid, WebCore::LayoutPoint flippedLocationInElement, MonotonicTime timestamp)` (if ENABLE(ARKIT_INLINE_PREVIEW_MAC))
- `ModelInlinePreviewUUIDs() -> (Vector<String> uuids)` (if ENABLE(ARKIT_INLINE_PREVIEW_MAC))
- `ModelElementGetCamera(WebKit::ModelIdentifier modelIdentifier) -> (Expected<WebCore::HTMLModelElementCamera, WebCore::ResourceError> result)` (if ENABLE(ARKIT_INLINE_PREVIEW))
- `ModelElementSetCamera(WebKit::ModelIdentifier modelIdentifier, WebCore::HTMLModelElementCamera camera) -> (bool success)` (if ENABLE(ARKIT_INLINE_PREVIEW))
- `ModelElementIsPlayingAnimation(WebKit::ModelIdentifier modelIdentifier) -> (Expected<bool, WebCore::ResourceError> result)` (if ENABLE(ARKIT_INLINE_PREVIEW))
- `ModelElementSetAnimationIsPlaying(WebKit::ModelIdentifier modelIdentifier, bool isPlaying) -> (bool success)` (if ENABLE(ARKIT_INLINE_PREVIEW))
- `ModelElementIsLoopingAnimation(WebKit::ModelIdentifier modelIdentifier) -> (Expected<bool, WebCore::ResourceError> result)` (if ENABLE(ARKIT_INLINE_PREVIEW))
- `ModelElementSetIsLoopingAnimation(WebKit::ModelIdentifier modelIdentifier, bool isLooping) -> (bool success)` (if ENABLE(ARKIT_INLINE_PREVIEW))
- `ModelElementAnimationDuration(WebKit::ModelIdentifier modelIdentifier) -> (Expected<Seconds, WebCore::ResourceError> result)` (if ENABLE(ARKIT_INLINE_PREVIEW))
- `ModelElementAnimationCurrentTime(WebKit::ModelIdentifier modelIdentifier) -> (Expected<Seconds, WebCore::ResourceError> result)` (if ENABLE(ARKIT_INLINE_PREVIEW))
- `ModelElementSetAnimationCurrentTime(WebKit::ModelIdentifier modelIdentifier, Seconds currentTime) -> (bool success)` (if ENABLE(ARKIT_INLINE_PREVIEW))
- `ModelElementHasAudio(WebKit::ModelIdentifier modelIdentifier) -> (Expected<bool, WebCore::ResourceError> result)` (if ENABLE(ARKIT_INLINE_PREVIEW))
- `ModelElementIsMuted(WebKit::ModelIdentifier modelIdentifier) -> (Expected<bool, WebCore::ResourceError> result)` (if ENABLE(ARKIT_INLINE_PREVIEW))
- `ModelElementSetIsMuted(WebKit::ModelIdentifier modelIdentifier, bool isMuted) -> (bool success)` (if ENABLE(ARKIT_INLINE_PREVIEW))
- `StartApplePayAMSUISession(URL originatingURL, WebCore::ApplePayAMSUIRequest request) -> (std::optional<bool> result)` (if ENABLE(APPLE_PAY_AMS_UI))
- `AbortApplePayAMSUISession()` (if ENABLE(APPLE_PAY_AMS_UI))
- `BeginSystemPreview(URL url, WebCore::SecurityOriginData topOrigin, WebCore::SystemPreviewInfo systemPreviewInfo) -> ()` (if USE(SYSTEM_PREVIEW))
- `DidCreateSleepDisabler(WebCore::SleepDisablerIdentifier identifier, String reason, bool display)`
- `DidDestroySleepDisabler(WebCore::SleepDisablerIdentifier identifier)`
- `RequestCookieConsent() -> (WebCore::CookieConsentDecisionResult result)`
- `DidAccessWindowProxyPropertyViaOpenerForFrame(WebCore::FrameIdentifier frameID, WebCore::SecurityOriginData openerOrigin, WebCore::WindowProxyProperty property)` (if ENABLE(WINDOW_PROXY_PROPERTY_ACCESS_NOTIFICATION))
- `DidApplyLinkDecorationFiltering(URL originalURL, URL adjustedURL)`
- `BroadcastProcessSyncData(WebCore::ProcessSyncData processSyncData)`
- `BroadcastTopDocumentSyncData(Ref<WebCore::DocumentSyncData> documentSyncData)`
- `DispatchLoadEventToFrameOwnerElement(WebCore::FrameIdentifier frameID)`
- `FocusRemoteFrame(WebCore::FrameIdentifier frameID)`
- `PostMessageToRemote(WebCore::FrameIdentifier source, String sourceOrigin, WebCore::FrameIdentifier target, std::optional<WebCore::SecurityOriginData> targetOrigin, WebCore::MessageWithMessagePorts message)`
- `RenderTreeAsTextForTesting(WebCore::FrameIdentifier identifier, size_t baseIndent, OptionSet<WebCore::RenderAsTextFlag> behavior) -> (String renderTreeDump)` (sync)
- `FrameTextForTesting(WebCore::FrameIdentifier frameID) -> (String text)` (sync)
- `LayerTreeAsTextForTesting(WebCore::FrameIdentifier identifier, size_t baseIndent, OptionSet<WebCore::LayerTreeAsTextOptions> options) -> (String layerTreeDump)` (sync)
- `BindRemoteAccessibilityFrames(int processIdentifier, WebCore::FrameIdentifier frameID, Vector<uint8_t> dataToken) -> (Vector<uint8_t> token, int processIdentifier)` (sync)
- `UpdateRemoteFrameAccessibilityOffset(WebCore::FrameIdentifier frameID, WebCore::IntPoint offset)`
- `DocumentURLForConsoleLog(WebCore::FrameIdentifier frameID) -> (URL url)`
- `NowPlayingMetadataChanged(WebCore::NowPlayingMetadata metadata)`
- `DidAdjustVisibilityWithSelectors(Vector<String> selectors)`
- `FrameNameChanged(WebCore::FrameIdentifier frameID, String frameName)`
- `GamepadsRecentlyAccessed()` (if ENABLE(GAMEPAD))
- `HasActiveNowPlayingSessionChanged(bool hasActiveNowPlayingSessionChanged)`
- `SetAllowsLayoutViewportHeightExpansion(bool newValue)`
- `ShouldOffloadIFrameForHost(String host) -> (bool wasGranted)` (if ENABLE(CONTENT_EXTENSIONS))

## `WebPasteboardProxy` - WebContent -> UI

`UIProcess/WebPasteboardProxy.messages.in`

- `WriteURLToPasteboard(WebCore::PasteboardURL url, String pasteboardName, std::optional<WebCore::PageIdentifier> pageID)` (if PLATFORM(IOS_FAMILY))
- `WriteWebContentToPasteboard(WebCore::PasteboardWebContent content, String pasteboardName, std::optional<WebCore::PageIdentifier> pageID)` (if PLATFORM(IOS_FAMILY))
- `WriteImageToPasteboard(WebCore::PasteboardImage pasteboardImage, String pasteboardName, std::optional<WebCore::PageIdentifier> pageID)` (if PLATFORM(IOS_FAMILY))
- `WriteStringToPasteboard(String pasteboardType, String text, String pasteboardName, std::optional<WebCore::PageIdentifier> pageID)` (if PLATFORM(IOS_FAMILY))
- `UpdateSupportedTypeIdentifiers(Vector<String> identifiers, String pasteboardName, std::optional<WebCore::PageIdentifier> pageID)` (if PLATFORM(IOS_FAMILY))
- `WriteCustomData(Vector<WebCore::PasteboardCustomData> data, String pasteboardName, std::optional<WebCore::PageIdentifier> pageID) -> (int64_t changeCount)` (sync)
- `TypesSafeForDOMToReadAndWrite(String pasteboardName, String origin, std::optional<WebCore::PageIdentifier> pageID) -> (Vector<String> types)` (sync)
- `AllPasteboardItemInfo(String pasteboardName, int64_t changeCount, std::optional<WebCore::PageIdentifier> pageID) -> (std::optional<Vector<WebCore::PasteboardItemInfo>> allInfo)` (sync)
- `InformationForItemAtIndex(size_t index, String pasteboardName, int64_t changeCount, std::optional<WebCore::PageIdentifier> pageID) -> (std::optional<WebCore::PasteboardItemInfo> info)` (sync)
- `GetPasteboardItemsCount(String pasteboardName, std::optional<WebCore::PageIdentifier> pageID) -> (uint64_t itemsCount)` (sync)
- `ReadStringFromPasteboard(size_t index, String pasteboardType, String pasteboardName, std::optional<WebCore::PageIdentifier> pageID) -> (String string)` (sync)
- `ReadURLFromPasteboard(size_t index, String pasteboardName, std::optional<WebCore::PageIdentifier> pageID) -> (String url, String title)` (sync)
- `ReadBufferFromPasteboard(std::optional<size_t> index, String pasteboardType, String pasteboardName, std::optional<WebCore::PageIdentifier> pageID) -> (RefPtr<WebCore::SharedBuffer> buffer)` (sync)
- `ContainsStringSafeForDOMToReadForType(String type, String pasteboardName, std::optional<WebCore::PageIdentifier> pageID) -> (bool result)` (sync)
- `GetNumberOfFiles(String pasteboardName, std::optional<WebCore::PageIdentifier> pageID) -> (uint64_t numberOfFiles)` (sync, if PLATFORM(COCOA))
- `GetPasteboardTypes(String pasteboardName, std::optional<WebCore::PageIdentifier> pageID) -> (Vector<String> types)` (sync, if PLATFORM(COCOA))
- `GetPasteboardPathnamesForType(String pasteboardName, String pasteboardType, std::optional<WebCore::PageIdentifier> pageID) -> (Vector<String> pathnames, Vector<WebKit::SandboxExtensionHandle> sandboxExtensions)` (sync, if PLATFORM(COCOA))
- `GetPasteboardStringForType(String pasteboardName, String pasteboardType, std::optional<WebCore::PageIdentifier> pageID) -> (String string)` (sync, if PLATFORM(COCOA))
- `GetPasteboardStringsForType(String pasteboardName, String pasteboardType, std::optional<WebCore::PageIdentifier> pageID) -> (Vector<String> strings)` (sync, if PLATFORM(COCOA))
- `GetPasteboardBufferForType(String pasteboardName, String pasteboardType, std::optional<WebCore::PageIdentifier> pageID) -> (WebCore::PasteboardBuffer pasteboardBuffer)` (sync, if PLATFORM(COCOA))
- `GetPasteboardChangeCount(String pasteboardName, std::optional<WebCore::PageIdentifier> pageID) -> (int64_t changeCount)` (sync, if PLATFORM(COCOA))
- `GetPasteboardColor(String pasteboardName, std::optional<WebCore::PageIdentifier> pageID) -> (WebCore::Color color)` (sync, if PLATFORM(COCOA))
- `GetPasteboardURL(String pasteboardName, std::optional<WebCore::PageIdentifier> pageID) -> (String urlString)` (sync, if PLATFORM(COCOA))
- `AddPasteboardTypes(String pasteboardName, Vector<String> pasteboardTypes, std::optional<WebCore::PageIdentifier> pageID) -> (int64_t changeCount)` (sync, if PLATFORM(COCOA))
- `SetPasteboardTypes(String pasteboardName, Vector<String> pasteboardTypes, std::optional<WebCore::PageIdentifier> pageID) -> (int64_t changeCount)` (sync, if PLATFORM(COCOA))
- `SetPasteboardURL(WebCore::PasteboardURL pasteboardURL, String pasteboardName, std::optional<WebCore::PageIdentifier> pageID) -> (int64_t changeCount)` (sync, if PLATFORM(COCOA))
- `SetPasteboardColor(String pasteboardName, WebCore::Color color, std::optional<WebCore::PageIdentifier> pageID) -> (int64_t changeCount)` (sync, if PLATFORM(COCOA))
- `SetPasteboardStringForType(String pasteboardName, String pasteboardType, String string, std::optional<WebCore::PageIdentifier> pageID) -> (int64_t changeCount)` (sync, if PLATFORM(COCOA))
- `SetPasteboardBufferForType(String pasteboardName, String pasteboardType, RefPtr<WebCore::SharedBuffer> buffer, std::optional<WebCore::PageIdentifier> pageID) -> (int64_t changeCount)` (sync, if PLATFORM(COCOA))
- `ContainsURLStringSuitableForLoading(String pasteboardName, std::optional<WebCore::PageIdentifier> pageID) -> (bool result)` (sync, if PLATFORM(COCOA))
- `URLStringSuitableForLoading(String pasteboardName, std::optional<WebCore::PageIdentifier> pageID) -> (String url, String title)` (sync, if PLATFORM(COCOA))
- `TestIPCSharedMemory(String pasteboardName, String pasteboardType, WebCore::SharedMemory::Handle handle, std::optional<WebCore::PageIdentifier> pageID) -> (int64_t changeCount, String buffer)` (sync, if (PLATFORM(COCOA) && ENABLE(IPC_TESTING_API)))
- `GetTypes(String pasteboardName) -> (Vector<String> types)` (sync, if PLATFORM(GTK))
- `ReadText(String pasteboardName) -> (String text)` (sync, if PLATFORM(GTK))
- `ReadFilePaths(String pasteboardName) -> (Vector<String> types)` (sync, if PLATFORM(GTK))
- `ReadBuffer(String pasteboardName, String pasteboardType) -> (RefPtr<WebCore::SharedBuffer> buffer)` (sync, if PLATFORM(GTK))
- `WriteToClipboard(String pasteboardName, WebCore::SelectionData pasteboardContent)` (if PLATFORM(GTK))
- `ClearClipboard(String pasteboardName)` (if PLATFORM(GTK))
- `GetPasteboardChangeCount(String pasteboardName) -> (int64_t changeCount)` (sync, if PLATFORM(GTK))
- `GetPasteboardTypes() -> (Vector<String> types)` (sync, if USE(LIBWPE))
- `WriteWebContentToPasteboard(WebCore::PasteboardWebContent content)` (if USE(LIBWPE))
- `WriteStringToPasteboard(String pasteboardType, String text)` (if USE(LIBWPE))

## `WebPaymentCoordinatorProxy` - WebContent -> UI

`Shared/ApplePay/WebPaymentCoordinatorProxy.messages.in`

- `CanMakePayments() -> (bool result)` (sync)
- `CanMakePaymentsWithActiveCard(String merchantIdentifier, String domainName) -> (bool canMakePayments)`
- `OpenPaymentSetup(String merchantIdentifier, String domainName) -> (bool result)`
- `ShowPaymentUI(WebCore::PageIdentifier destinationID, WebKit::WebPageProxyIdentifier webPageProxyIdentifier, String originatingURLString, Vector<String> linkIconURLStrings, WebCore::ApplePaySessionPaymentRequest paymentRequest) -> (bool result)` (sync)
- `CompleteMerchantValidation(WebCore::PaymentMerchantSession paymentMerchantSession)`
- `CompleteShippingMethodSelection(std::optional<WebCore::ApplePayShippingMethodUpdate> update)`
- `CompleteShippingContactSelection(std::optional<WebCore::ApplePayShippingContactUpdate> update)`
- `CompletePaymentMethodSelection(std::optional<WebCore::ApplePayPaymentMethodUpdate> update)`
- `CompleteCouponCodeChange(std::optional<WebCore::ApplePayCouponCodeUpdate> update)` (if ENABLE(APPLE_PAY_COUPON_CODE))
- `CompletePaymentSession(WebCore::ApplePayPaymentAuthorizationResult result)`
- `AbortPaymentSession()`
- `CancelPaymentSession()`
- `GetSetupFeatures(WebKit::PaymentSetupConfiguration configuration) -> (WebKit::PaymentSetupFeatures features)`
- `BeginApplePaySetup(WebKit::PaymentSetupConfiguration configuration, WebKit::PaymentSetupFeatures features) -> (bool result)`
- `EndApplePaySetup()`

## `WebPermissionControllerProxy` - WebContent -> UI

`UIProcess/WebPermissionControllerProxy.messages.in`

- `Query(WebCore::ClientOrigin origin, WebCore::PermissionDescriptor descriptor, std::optional<WebKit::WebPageProxyIdentifier> identifier, WebCore::PermissionQuerySource source) -> (std::optional<WebCore::PermissionState> state)`

## `WebProcessPool` - WebContent -> UI

`UIProcess/WebProcessPool.messages.in`

- `HandleMessage(String messageName, WebKit::UserData messageBody)`
- `HandleSynchronousMessage(String messageName, WebKit::UserData messageBody) -> (WebKit::UserData returnData)` (sync)
- `StartedUsingGamepads()` (if ENABLE(GAMEPAD))
- `StoppedUsingGamepads() -> ()` (if ENABLE(GAMEPAD))
- `PlayGamepadEffect(unsigned gamepadIndex, String gamepadID, WebCore::GamepadHapticEffectType type, WebCore::GamepadEffectParameters parameters) -> (bool success)` (if ENABLE(GAMEPAD))
- `StopGamepadEffects(unsigned gamepadIndex, String gamepadID) -> ()` (if ENABLE(GAMEPAD))
- `ReportWebContentCPUTime(Seconds cpuTime, uint64_t activityState)`

## `WebProcessProxy` - WebContent -> UI

`UIProcess/WebProcessProxy.messages.in`

- `DidDestroyUserGestureToken(WebCore::PageIdentifier pageID, WebCore::UserGestureTokenIdentifier userGestureTokenID)`
- `ShouldTerminate() -> (bool shouldTerminate)` (sync)
- `EnableSuddenTermination()`
- `DisableSuddenTermination()`
- `GetNetworkProcessConnection() -> (WebKit::NetworkProcessConnectionInfo connectionInfo)` (sync)
- `WaitForSharedPreferencesForWebProcessToSync(uint64_t sharedPreferencesVersion) -> (bool success)` (sync)
- `CreateGPUProcessConnection(WebKit::GPUProcessConnectionIdentifier identifier, IPC::ConnectionHandle connectionHandle)` (AllowedWhenWaitingForSyncReply, if ENABLE(GPU_PROCESS))
- `GPUProcessConnectionDidBecomeUnresponsive(WebKit::GPUProcessConnectionIdentifier identifier)` (if ENABLE(GPU_PROCESS))
- `CreateModelProcessConnection(IPC::ConnectionHandle connectionIdentifier, WebKit::ModelProcessConnectionParameters parameters)` (AllowedWhenWaitingForSyncReply, if ENABLE(MODEL_PROCESS))
- `DidExceedActiveMemoryLimit()`
- `DidExceedInactiveMemoryLimit()`
- `DidExceedMemoryFootprintThreshold(size_t footprint)`
- `DidExceedCPULimit()`
- `StopResponsivenessTimer()`
- `DidReceiveBackgroundResponsivenessPing()`
- `MemoryPressureStatusChanged(WTF::SystemMemoryPressureStatus status)`
- `DidCollectPrewarmInformation(WebCore::RegistrableDomain domain, WebCore::PrewarmInformation prewarmInformation)`
- `CacheMediaMIMETypes(Vector<String> types)` (if PLATFORM(COCOA))
- `StartDisplayLink(WebKit::DisplayLinkObserverID observerID, uint32_t displayID, unsigned preferredFramesPerSecond)` (if HAVE(DISPLAY_LINK))
- `StopDisplayLink(WebKit::DisplayLinkObserverID observerID, uint32_t displayID)` (if HAVE(DISPLAY_LINK))
- `SetDisplayLinkPreferredFramesPerSecond(WebKit::DisplayLinkObserverID observerID, uint32_t displayID, unsigned preferredFramesPerSecond)` (if HAVE(DISPLAY_LINK))
- `SendMessageToWebContext(WebKit::UserMessage userMessage)` (if PLATFORM(GTK) || PLATFORM(WPE))
- `SendMessageToWebContextWithReply(WebKit::UserMessage userMessage) -> (WebKit::UserMessage replyMessage)` (if PLATFORM(GTK) || PLATFORM(WPE))
- `CreateSpeechRecognitionServer(WebCore::PageIdentifier identifier)`
- `DestroySpeechRecognitionServer(WebCore::PageIdentifier identifier)`
- `SystemBeep()`
- `IsAXAuthenticated(WebKit::CoreIPCAuditToken auditToken) -> (bool authenticated)` (sync, if PLATFORM(MAC) || PLATFORM(MACCATALYST))
- `SetCaptionDisplayMode(WebCore::CaptionUserPreferencesDisplayMode mode)` (if HAVE(MEDIA_ACCESSIBILITY_FRAMEWORK))
- `SetCaptionLanguage(String language)` (if HAVE(MEDIA_ACCESSIBILITY_FRAMEWORK))
- `GetNotifications(URL registrationURL, String tag) -> (Vector<WebCore::NotificationData> result)` (if ENABLE(NOTIFICATION_EVENT))
- `SetAppBadge(std::optional<WebKit::WebPageProxyIdentifier> pageIdentifier, WebCore::SecurityOriginData origin, std::optional<uint64_t> badge)`
- `SetClientBadge(WebKit::WebPageProxyIdentifier pageIdentifier, WebCore::SecurityOriginData origin, std::optional<uint64_t> badge)`
- `WrapCryptoKey(Vector<uint8_t> key) -> (std::optional<Vector<uint8_t>> wrappedKey)` (sync)
- `SerializeAndWrapCryptoKey(WebCore::CryptoKeyData key) -> (std::optional<Vector<uint8_t>> wrappedKey)` (sync)
- `UnwrapCryptoKey(WebCore::WrappedCryptoKey wrappedKey) -> (std::optional<Vector<uint8_t>> key)` (sync)
- `SetupLogStream(uint32_t pid, IPC::StreamServerConnectionHandle serverConnection, WebKit::LogStreamIdentifier identifier) -> (IPC::Semaphore streamWakeUpSemaphore, IPC::Semaphore streamClientWaitSemaphore)` (if ENABLE(LOGD_BLOCKING_IN_WEBCONTENT))

## `WebScreenOrientationManagerProxy` - WebContent -> UI

`UIProcess/WebScreenOrientationManagerProxy.messages.in`

- `CurrentOrientation() -> (WebCore::ScreenOrientationType orientation)` (sync)
- `Lock(WebCore::ScreenOrientationLockType orientation) -> (std::optional<WebCore::Exception> exception)`
- `Unlock()`
- `SetShouldSendChangeNotification(bool shouldSend)`

## `WebUserContentControllerProxy` - WebContent -> UI

`UIProcess/UserContent/WebUserContentControllerProxy.messages.in`

- `DidPostMessage(WebKit::WebPageProxyIdentifier pageID, WebKit::FrameInfoData frameInfoData, WebKit::ScriptMessageHandlerIdentifier messageHandlerID, std::span<const uint8_t> message) -> (std::span<const uint8_t> resultValue, String errorMessage)`

## `GPUConnectionToWebProcess` - WebContent -> GPU

`GPUProcess/GPUConnectionToWebProcess.messages.in`

- `CreateRenderingBackend(WebKit::RenderingBackendIdentifier renderingBackendIdentifier, IPC::StreamServerConnectionHandle connectionHandle)` (AllowedWhenWaitingForSyncReply)
- `ReleaseRenderingBackend(WebKit::RenderingBackendIdentifier renderingBackendIdentifier)` (AllowedWhenWaitingForSyncReply)
- `CreateGraphicsContextGL(WebKit::GraphicsContextGLIdentifier identifier, WebCore::GraphicsContextGLAttributes attributes, WebKit::RenderingBackendIdentifier renderingBackendIdentifier, IPC::StreamServerConnectionHandle serverConnection)` (AllowedWhenWaitingForSyncReply, if ENABLE(WEBGL))
- `ReleaseGraphicsContextGL(WebKit::GraphicsContextGLIdentifier identifier)` (AllowedWhenWaitingForSyncReply, if ENABLE(WEBGL))
- `CreateGPU(WebKit::WebGPUIdentifier identifier, WebKit::RenderingBackendIdentifier renderingBackendIdentifier, IPC::StreamServerConnectionHandle serverConnection)` (AllowedWhenWaitingForSyncReply)
- `ReleaseGPU(WebKit::WebGPUIdentifier identifier)` (AllowedWhenWaitingForSyncReply)
- `ClearNowPlayingInfo()`
- `SetNowPlayingInfo(WebCore::NowPlayingInfo nowPlayingInfo)`
- `EnsureAudioSession() -> (WebKit::RemoteAudioSessionConfiguration configuration)` (sync, if USE(AUDIO_SESSION))
- `EnsureMediaSessionHelper()` (if PLATFORM(IOS_FAMILY))
- `CreateVisibilityPropagationContextForPage(WebKit::WebPageProxyIdentifier pageProxyID, WebCore::PageIdentifier pageID, bool canShowWhileLocked)` (if HAVE(VISIBILITY_PROPAGATION_VIEW))
- `DestroyVisibilityPropagationContextForPage(WebKit::WebPageProxyIdentifier pageProxyID, WebCore::PageIdentifier pageID)` (if HAVE(VISIBILITY_PROPAGATION_VIEW))
- `SetMediaOverridesForTesting(WebKit::MediaOverridesForTesting configuration)`
- `CreateAudioHardwareListener(WebKit::RemoteAudioHardwareListenerIdentifier identifier)`
- `ReleaseAudioHardwareListener(WebKit::RemoteAudioHardwareListenerIdentifier identifier)`
- `CreateRemoteCommandListener(WebKit::RemoteRemoteCommandListenerIdentifier identifier)`
- `ReleaseRemoteCommandListener(WebKit::RemoteRemoteCommandListenerIdentifier identifier)`
- `ConfigureLoggingChannel(String channelName, WTFLogChannelState state, WTFLogLevel level)`
- `CreateWCLayerTreeHost(WebKit::WCLayerTreeHostIdentifier identifier, uint64_t nativeWindow, bool usesOffscreenRendering)` (AllowedWhenWaitingForSyncReply, if USE(GRAPHICS_LAYER_WC))
- `ReleaseWCLayerTreeHost(WebKit::WCLayerTreeHostIdentifier identifier)` (AllowedWhenWaitingForSyncReply, if USE(GRAPHICS_LAYER_WC))
- `EnableMockMediaSource()` (if ENABLE(MEDIA_SOURCE))
- `UpdateSampleBufferDisplayLayerBoundsAndPosition(WebKit::SampleBufferDisplayLayerIdentifier identifier, WebCore::FloatRect bounds, std::optional<MachSendRight> fence)` (if PLATFORM(COCOA) && ENABLE(MEDIA_STREAM))
- `SetMediaEnvironment(WebCore::PageIdentifier pageIdentifier, String mediaEnvironment)` (if ENABLE(EXTENSION_CAPABILITIES))

## `LibWebRTCCodecsProxy` - WebContent -> GPU

`GPUProcess/webrtc/LibWebRTCCodecsProxy.messages.in`

- `CreateDecoder(WebKit::VideoDecoderIdentifier id, WebCore::VideoCodecType codecType, String codecString, bool useRemoteFrames, bool enableAdditionalLogging) -> (bool success)`
- `ReleaseDecoder(WebKit::VideoDecoderIdentifier id)`
- `FlushDecoder(WebKit::VideoDecoderIdentifier id) -> ()`
- `SetDecoderFormatDescription(WebKit::VideoDecoderIdentifier id, std::span<const uint8_t> description, uint16_t width, uint16_t height)`
- `DecodeFrame(WebKit::VideoDecoderIdentifier id, int64_t timeStamp, std::span<const uint8_t> data) -> (bool success)`
- `SetFrameSize(WebKit::VideoDecoderIdentifier id, uint16_t width, uint16_t height)`
- `CreateEncoder(WebKit::VideoEncoderIdentifier id, WebCore::VideoCodecType codecType, String codecString, Vector<std::pair<String, String>> parameters, bool useLowLatency, bool useAnnexB, WebCore::VideoEncoderScalabilityMode scalabilityMode) -> (bool success)`
- `ReleaseEncoder(WebKit::VideoEncoderIdentifier id)`
- `InitializeEncoder(WebKit::VideoEncoderIdentifier id, uint16_t width, uint16_t height, unsigned startBitrate, unsigned maxBitrate, unsigned minBitrate, uint32_t maxFramerate)`
- `EncodeFrame(WebKit::VideoEncoderIdentifier id, WebKit::SharedVideoFrame buffer, int64_t timeStamp, std::optional<uint64_t> duration, bool shouldEncodeAsKeyFrame) -> (bool success)`
- `FlushEncoder(WebKit::VideoEncoderIdentifier id) -> ()`
- `SetEncodeRates(WebKit::VideoEncoderIdentifier id, uint32_t bitRate, uint32_t frameRate) -> ()`
- `SetSharedVideoFrameSemaphore(WebKit::VideoEncoderIdentifier id, IPC::Semaphore semaphore)`
- `SetSharedVideoFrameMemory(WebKit::VideoEncoderIdentifier id, WebCore::SharedMemory::Handle storageHandle)`
- `SetRTCLoggingLevel(WTFLogLevel level)`

## `RemoteAdapter` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteAdapter.messages.in`

- `Destruct()`
- `RequestDevice(WebKit::WebGPU::DeviceDescriptor deviceDescriptor, WebKit::WebGPUIdentifier identifier, WebKit::WebGPUIdentifier queueIdentifier) -> (WebKit::WebGPU::SupportedFeatures supportedFeatures, WebKit::WebGPU::SupportedLimits supportedLimits)` (sync)

## `RemoteAudioDestinationManager` - WebContent -> GPU

`GPUProcess/media/RemoteAudioDestinationManager.messages.in`

- `CreateAudioDestination(WebKit::RemoteAudioDestinationIdentifier identifier, String inputDeviceId, uint32_t numberOfInputChannels, uint32_t numberOfOutputChannels, float sampleRate, float hardwareSampleRate, IPC::Semaphore renderSemaphore, WebCore::SharedMemory::Handle frameCount) -> (size_t audioUnitLatency)`
- `DeleteAudioDestination(WebKit::RemoteAudioDestinationIdentifier identifier)`
- `StartAudioDestination(WebKit::RemoteAudioDestinationIdentifier identifier) -> (bool isPlaying, size_t audioUnitLatency)`
- `StopAudioDestination(WebKit::RemoteAudioDestinationIdentifier identifier) -> (bool isPlaying)`
- `AudioSamplesStorageChanged(WebKit::RemoteAudioDestinationIdentifier identifier, WebKit::ConsumerSharedCARingBufferHandle storageHandle)` (if PLATFORM(COCOA))

## `RemoteAudioMediaStreamTrackRendererInternalUnitManager` - WebContent -> GPU

`GPUProcess/webrtc/RemoteAudioMediaStreamTrackRendererInternalUnitManager.messages.in`

- `CreateUnit(WebKit::AudioMediaStreamTrackRendererInternalUnitIdentifier identifier, String deviceID) -> (std::optional<WebCore::CAAudioStreamDescription> description, size_t frameChunkSize)`
- `DeleteUnit(WebKit::AudioMediaStreamTrackRendererInternalUnitIdentifier identifier)`
- `StartUnit(WebKit::AudioMediaStreamTrackRendererInternalUnitIdentifier identifier, WebKit::ConsumerSharedCARingBufferHandle storageHandle, IPC::Semaphore renderSemaphore)`
- `StopUnit(WebKit::AudioMediaStreamTrackRendererInternalUnitIdentifier identifier)`
- `SetLastDeviceUsed(String deviceID)`

## `RemoteAudioSessionProxy` - WebContent -> GPU

`GPUProcess/media/RemoteAudioSessionProxy.messages.in`

- `SetCategory(WebCore::AudioSessionCategory type, WebCore::AudioSessionMode mode, WebCore::RouteSharingPolicy policy)`
- `SetPreferredBufferSize(uint64_t preferredBufferSize)`
- `TryToSetActive(bool active) -> (bool suceeded)` (sync)
- `SetIsPlayingToBluetoothOverride(std::optional<bool> value)`
- `TriggerBeginInterruptionForTesting()`
- `TriggerEndInterruptionForTesting()`
- `BeginInterruptionRemote()`
- `EndInterruptionRemote(WebCore::AudioSession::MayResume flags)`
- `SetSceneIdentifier(String sceneIdentifier)`
- `SetSoundStageSize(WebCore::AudioSessionSoundStageSize size)`

## `RemoteBarcodeDetector` - WebContent -> GPU

`GPUProcess/ShapeDetection/RemoteBarcodeDetector.messages.in`

- `Detect(WebCore::RenderingResourceIdentifier renderingResourceIdentifier) -> (Vector<WebCore::ShapeDetection::DetectedBarcode> detectedBarcodes)`

## `RemoteBindGroup` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteBindGroup.messages.in`

- `Destruct()`
- `SetLabel(String label)`
- `UpdateExternalTextures(WebKit::WebGPUIdentifier externalTextureIdentifier) -> (bool success)` (sync)

## `RemoteBindGroupLayout` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteBindGroupLayout.messages.in`

- `Destruct()`
- `SetLabel(String label)`

## `RemoteBuffer` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteBuffer.messages.in`

- `GetMappedRange(WebCore::WebGPU::Size64 offset, std::optional<WebCore::WebGPU::Size64> size) -> (std::optional<Vector<uint8_t>> data)` (sync)
- `MapAsync(WebCore::WebGPU::MapModeFlags mapModeFlags, WebCore::WebGPU::Size64 offset, std::optional<WebCore::WebGPU::Size64> size) -> (bool success)`
- `Copy(std::optional<WebCore::SharedMemory::Handle> data, size_t offset) -> (bool success)` (NotStreamEncodable)
- `Unmap()`
- `Destroy()`
- `Destruct()`
- `SetLabel(String label)`

## `RemoteCDMFactoryProxy` - WebContent -> GPU

`GPUProcess/media/RemoteCDMFactoryProxy.messages.in`

- `CreateCDM(String keySystem) -> (std::optional<WebKit::RemoteCDMIdentifier> identifier, WebKit::RemoteCDMConfiguration configuration)` (sync)
- `SupportsKeySystem(String keySystem) -> (bool result)` (sync)
- `RemoveInstance(WebKit::RemoteCDMInstanceIdentifier identifier)`
- `RemoveSession(WebKit::RemoteCDMInstanceSessionIdentifier identifier)`

## `RemoteCDMInstanceProxy` - WebContent -> GPU

`GPUProcess/media/RemoteCDMInstanceProxy.messages.in`

- `CreateSession(uint64_t logIdentifier) -> (std::optional<WebKit::RemoteCDMInstanceSessionIdentifier> identifier)` (sync)
- `InitializeWithConfiguration(WebCore::CDMKeySystemConfiguration configuration, WebCore::CDMInstance::AllowDistinctiveIdentifiers distinctiveIdentifiersAllowed, WebCore::CDMInstance::AllowPersistentState persistentStateAllowed) -> (WebCore::CDMInstance::SuccessValue success)`
- `SetServerCertificate(Ref<WebCore::SharedBuffer> certificate) -> (WebCore::CDMInstance::SuccessValue success)`
- `SetStorageDirectory(String directory)`

## `RemoteCDMInstanceSessionProxy` - WebContent -> GPU

`GPUProcess/media/RemoteCDMInstanceSessionProxy.messages.in`

- `SetLogIdentifier(uint64_t logIdentifier)`
- `RequestLicense(WebCore::CDMInstanceSession::LicenseType type, WebCore::CDMKeyGroupingStrategy keyGroupingStrategy, AtomString initDataType, RefPtr<WebCore::SharedBuffer> initData) -> (RefPtr<WebCore::SharedBuffer> message, String sessionId, bool needsIndividualization, bool succeeded)`
- `UpdateLicense(String sessionId, WebCore::CDMInstanceSession::LicenseType type, RefPtr<WebCore::SharedBuffer> response) -> (bool sessionWasClosed, std::optional<WebCore::CDMInstanceSession::KeyStatusVector> changedKeys, std::optional<double> changedExpiration, std::optional<WebCore::CDMInstanceSession::Message> message, bool succeeded)`
- `LoadSession(WebCore::CDMInstanceSession::LicenseType type, String sessionId, String origin) -> (std::optional<WebCore::CDMInstanceSession::KeyStatusVector> changedKeys, std::optional<double> changedExpiration, std::optional<WebCore::CDMInstanceSession::Message> message, bool succeeded, WebCore::CDMInstanceSessionLoadFailure loadFailure)`
- `CloseSession(String sessionId) -> ()`
- `RemoveSessionData(String sessionId, WebCore::CDMInstanceSession::LicenseType type) -> (WebCore::CDMInstanceSession::KeyStatusVector changedKeys, RefPtr<WebCore::SharedBuffer> message, bool succeeded)`
- `StoreRecordOfKeyUsage(String sessionId)`

## `RemoteCDMProxy` - WebContent -> GPU

`GPUProcess/media/RemoteCDMProxy.messages.in`

- `GetSupportedConfiguration(WebCore::CDMKeySystemConfiguration candidateConfiguration, WebCore::CDMPrivate::LocalStorageAccess access) -> (std::optional<WebCore::CDMKeySystemConfiguration> accumulatedConfiguration)`
- `CreateInstance() -> (std::optional<WebKit::RemoteCDMInstanceIdentifier> identifier, WebKit::RemoteCDMInstanceConfiguration configuration)` (sync)
- `LoadAndInitialize()`
- `SetLogIdentifier(uint64_t logIdentifier)`

## `RemoteCommandBuffer` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteCommandBuffer.messages.in`

- `Destruct()`
- `SetLabel(String label)`

## `RemoteCommandEncoder` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteCommandEncoder.messages.in`

- `BeginRenderPass(WebKit::WebGPU::RenderPassDescriptor descriptor, WebKit::WebGPUIdentifier identifier)`
- `BeginComputePass(std::optional<WebKit::WebGPU::ComputePassDescriptor> descriptor, WebKit::WebGPUIdentifier identifier)`
- `CopyBufferToBuffer(WebKit::WebGPUIdentifier source, WebCore::WebGPU::Size64 sourceOffset, WebKit::WebGPUIdentifier destination, WebCore::WebGPU::Size64 destinationOffset, WebCore::WebGPU::Size64 size)`
- `CopyBufferToTexture(WebKit::WebGPU::ImageCopyBuffer source, WebKit::WebGPU::ImageCopyTexture destination, WebKit::WebGPU::Extent3D copySize)`
- `CopyTextureToBuffer(WebKit::WebGPU::ImageCopyTexture source, WebKit::WebGPU::ImageCopyBuffer destination, WebKit::WebGPU::Extent3D copySize)`
- `CopyTextureToTexture(WebKit::WebGPU::ImageCopyTexture source, WebKit::WebGPU::ImageCopyTexture destination, WebKit::WebGPU::Extent3D copySize)`
- `ClearBuffer(WebKit::WebGPUIdentifier buffer, WebCore::WebGPU::Size64 offset, std::optional<WebCore::WebGPU::Size64> size)`
- `Destruct()`
- `PushDebugGroup(String groupLabel)`
- `PopDebugGroup()`
- `InsertDebugMarker(String markerLabel)`
- `WriteTimestamp(WebKit::WebGPUIdentifier identifier, WebCore::WebGPU::Size32 queryIndex)`
- `ResolveQuerySet(WebKit::WebGPUIdentifier identifier, WebCore::WebGPU::Size32 firstQuery, WebCore::WebGPU::Size32 queryCount, WebKit::WebGPUIdentifier destination, WebCore::WebGPU::Size64 destinationOffset)`
- `Finish(WebKit::WebGPU::CommandBufferDescriptor descriptor, WebKit::WebGPUIdentifier identifier)`
- `SetLabel(String label)`

## `RemoteCompositorIntegration` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteCompositorIntegration.messages.in`

- `RecreateRenderBuffers(int width, int height, WebCore::DestinationColorSpace destinationColorSpace, WebCore::AlphaPremultiplication alphaMode, WebCore::WebGPU::TextureFormat textureFormat, WebKit::WebGPUIdentifier deviceIdentifier) -> (Vector<MachSendRight> renderBuffers)` (NotStreamEncodableReply, sync, if PLATFORM(COCOA))
- `PrepareForDisplay(uint32_t frameIndex) -> (bool dummy)` (//, Because, CanvasRenderingContext::prepareForDisplay(), NotStreamEncodableReply, Synchronous., be, contents, layer, needs, requires, synchronously,, the, this, to, sync)
- `PaintCompositedResultsToCanvas(WebCore::RenderingResourceIdentifier imageBuffer, uint32_t bufferIndex) -> ()` (sync)
- `Destruct()`

## `RemoteComputePassEncoder` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteComputePassEncoder.messages.in`

- `Destruct()`
- `SetPipeline(WebKit::WebGPUIdentifier identifier)`
- `Dispatch(WebCore::WebGPU::Size32 workgroupCountX, WebCore::WebGPU::Size32 workgroupCountY, WebCore::WebGPU::Size32 workgroupCountZ)`
- `DispatchIndirect(WebKit::WebGPUIdentifier indirectBuffer, WebCore::WebGPU::Size64 indirectOffset)`
- `End()`
- `SetBindGroup(WebCore::WebGPU::Index32 index, WebKit::WebGPUIdentifier identifier, std::optional<Vector<WebCore::WebGPU::BufferDynamicOffset>> dynamicOffsets)`
- `PushDebugGroup(String groupLabel)`
- `PopDebugGroup()`
- `InsertDebugMarker(String markerLabel)`
- `SetLabel(String label)`

## `RemoteComputePipeline` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteComputePipeline.messages.in`

- `Destruct()`
- `GetBindGroupLayout(uint32_t index, WebKit::WebGPUIdentifier identifier)`
- `SetLabel(String label)`

## `RemoteDevice` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteDevice.messages.in`

- `Destroy()`
- `Destruct()`
- `CreateXRBinding(WebKit::WebGPUIdentifier identifier)`
- `CreateBuffer(WebKit::WebGPU::BufferDescriptor descriptor, WebKit::WebGPUIdentifier identifier)`
- `CreateTexture(WebKit::WebGPU::TextureDescriptor descriptor, WebKit::WebGPUIdentifier identifier)`
- `CreateSampler(WebKit::WebGPU::SamplerDescriptor descriptor, WebKit::WebGPUIdentifier identifier)`
- `CreateBindGroupLayout(WebKit::WebGPU::BindGroupLayoutDescriptor descriptor, WebKit::WebGPUIdentifier identifier)`
- `CreatePipelineLayout(WebKit::WebGPU::PipelineLayoutDescriptor descriptor, WebKit::WebGPUIdentifier identifier)`
- `CreateBindGroup(WebKit::WebGPU::BindGroupDescriptor descriptor, WebKit::WebGPUIdentifier identifier)`
- `CreateShaderModule(WebKit::WebGPU::ShaderModuleDescriptor descriptor, WebKit::WebGPUIdentifier identifier)`
- `CreateComputePipeline(WebKit::WebGPU::ComputePipelineDescriptor descriptor, WebKit::WebGPUIdentifier identifier)`
- `CreateRenderPipeline(WebKit::WebGPU::RenderPipelineDescriptor descriptor, WebKit::WebGPUIdentifier identifier)`
- `CreateComputePipelineAsync(WebKit::WebGPU::ComputePipelineDescriptor descriptor, WebKit::WebGPUIdentifier identifier) -> (bool success, String error)`
- `CreateRenderPipelineAsync(WebKit::WebGPU::RenderPipelineDescriptor descriptor, WebKit::WebGPUIdentifier identifier) -> (bool success, String error)`
- `CreateCommandEncoder(std::optional<WebKit::WebGPU::CommandEncoderDescriptor> descriptor, WebKit::WebGPUIdentifier identifier)`
- `CreateRenderBundleEncoder(WebKit::WebGPU::RenderBundleEncoderDescriptor descriptor, WebKit::WebGPUIdentifier identifier)`
- `CreateQuerySet(WebKit::WebGPU::QuerySetDescriptor descriptor, WebKit::WebGPUIdentifier identifier)`
- `PushErrorScope(WebCore::WebGPU::ErrorFilter errorFilter)`
- `PopErrorScope() -> (bool success, std::optional<WebKit::WebGPU::Error> error)`
- `ResolveUncapturedErrorEvent() -> (bool hasUncapturedError, std::optional<WebKit::WebGPU::Error> error)`
- `ResolveDeviceLostPromise() -> (WebCore::WebGPU::DeviceLostReason reason)`
- `SetLabel(String label)`
- `PauseAllErrorReporting(bool pauseErrorReporting)`
- `SetSharedVideoFrameSemaphore(IPC::Semaphore semaphore)` (NotStreamEncodable, if PLATFORM(COCOA) && ENABLE(VIDEO))
- `SetSharedVideoFrameMemory(WebCore::SharedMemory::Handle storageHandle)` (NotStreamEncodable, if PLATFORM(COCOA) && ENABLE(VIDEO))
- `ImportExternalTextureFromVideoFrame(WebKit::WebGPU::ExternalTextureDescriptor descriptor, WebKit::WebGPUIdentifier identifier)` (NotStreamEncodable, if PLATFORM(COCOA) && ENABLE(VIDEO))
- `UpdateExternalTexture(WebKit::WebGPUIdentifier externalTextureIdentifier, WebCore::MediaPlayerIdentifier mediaIdentifier)` (if PLATFORM(COCOA) && ENABLE(VIDEO))

## `RemoteDisplayListRecorder` - WebContent -> GPU

`GPUProcess/graphics/RemoteDisplayListRecorder.messages.in`

- `Save()` (StreamBatched)
- `Restore()` (StreamBatched)
- `Translate(float x, float y)` (StreamBatched)
- `Rotate(float angle)` (StreamBatched)
- `Scale(WebCore::FloatSize scale)` (StreamBatched)
- `SetCTM(WebCore::AffineTransform ctm)` (StreamBatched)
- `ConcatenateCTM(WebCore::AffineTransform ctm)` (StreamBatched)
- `SetInlineFillColor(WebCore::DisplayList::SetInlineFillColor fillColorItem)` (StreamBatched)
- `SetInlineStroke(WebCore::DisplayList::SetInlineStroke strokeItem)` (StreamBatched)
- `SetState(WebCore::DisplayList::SetState item)` (StreamBatched)
- `SetLineCap(WebCore::LineCap lineCap)` (StreamBatched)
- `SetLineDash(WebCore::DisplayList::SetLineDash item)` (StreamBatched)
- `SetLineJoin(WebCore::LineJoin lineJoin)` (StreamBatched)
- `SetMiterLimit(float limit)` (StreamBatched)
- `ClearDropShadow()`
- `Clip(WebCore::FloatRect rect)`
- `ClipRoundedRect(WebCore::FloatRoundedRect rect)`
- `ClipOut(WebCore::FloatRect rect)`
- `ClipOutRoundedRect(WebCore::FloatRoundedRect rect)`
- `ClipToImageBuffer(WebCore::RenderingResourceIdentifier renderingResourceIdentifier, WebCore::FloatRect destinationRect)`
- `ClipOutToPath(WebCore::Path path)`
- `ClipPath(WebCore::Path path, WebCore::WindRule windRule)`
- `ResetClip()`
- `DrawGlyphs(WebCore::DisplayList::DrawGlyphs item)`
- `DrawDecomposedGlyphs(WebCore::RenderingResourceIdentifier fontIdentifier, WebCore::RenderingResourceIdentifier decomposedGlyphsIdentifier)`
- `DrawFilteredImageBuffer(std::optional<WebCore::RenderingResourceIdentifier> sourceImageIdentifier, WebCore::FloatRect sourceImageRect, Ref<WebCore::Filter> filter)`
- `DrawImageBuffer(WebCore::RenderingResourceIdentifier imageBufferIdentifier, WebCore::FloatRect destinationRect, WebCore::FloatRect srcRect, WebCore::ImagePaintingOptions options)`
- `DrawNativeImage(WebCore::RenderingResourceIdentifier imageIdentifier, WebCore::FloatRect destRect, WebCore::FloatRect srcRect, WebCore::ImagePaintingOptions options)`
- `DrawSystemImage(Ref<WebCore::SystemImage> systemImage, WebCore::FloatRect destinationRect)`
- `DrawPattern(WebCore::RenderingResourceIdentifier imageIdentifier, WebCore::FloatRect destRect, WebCore::FloatRect tileRect, WebCore::AffineTransform transform, WebCore::FloatPoint phase, WebCore::FloatSize spacing, WebCore::ImagePaintingOptions options)`
- `BeginTransparencyLayer(float opacity)`
- `BeginTransparencyLayerWithCompositeMode(WebCore::CompositeMode compositeMode)`
- `EndTransparencyLayer()`
- `DrawRect(WebCore::FloatRect rect, float borderThickness)`
- `DrawLine(WebCore::FloatPoint point1, WebCore::FloatPoint point2)`
- `DrawLinesForText(WebCore::DisplayList::DrawLinesForText item)`
- `DrawDotsForDocumentMarker(WebCore::FloatRect rect, WebCore::DocumentMarkerLineStyle style)`
- `DrawEllipse(WebCore::FloatRect rect)`
- `DrawPath(WebCore::Path path)`
- `DrawFocusRingPath(WebCore::Path path, float outlineWidth, WebCore::Color color)`
- `DrawFocusRingRects(Vector<WebCore::FloatRect> rects, float outlineOffset, float outlineWidth, WebCore::Color color)`
- `FillRect(WebCore::FloatRect rect, WebCore::GraphicsContext::RequiresClipToRect requiresClipToRect)`
- `FillRectWithColor(WebCore::FloatRect rect, WebCore::Color color)`
- `FillRectWithGradient(WebCore::DisplayList::FillRectWithGradient item)`
- `FillRectWithGradientAndSpaceTransform(WebCore::DisplayList::FillRectWithGradientAndSpaceTransform item)`
- `FillCompositedRect(WebCore::FloatRect rect, WebCore::Color color, WebCore::CompositeOperator op, WebCore::BlendMode blendMode)`
- `FillRoundedRect(WebCore::FloatRoundedRect rect, WebCore::Color color, WebCore::BlendMode blendMode)`
- `FillRectWithRoundedHole(WebCore::FloatRect rect, WebCore::FloatRoundedRect roundedHoleRect, WebCore::Color color)`
- `FillLine(WebCore::PathDataLine line)` (if ENABLE(INLINE_PATH_DATA))
- `FillArc(WebCore::PathArc arc)` (if ENABLE(INLINE_PATH_DATA))
- `FillClosedArc(WebCore::PathClosedArc closedArc)` (if ENABLE(INLINE_PATH_DATA))
- `FillQuadCurve(WebCore::PathDataQuadCurve curve)` (if ENABLE(INLINE_PATH_DATA))
- `FillBezierCurve(WebCore::PathDataBezierCurve curve)` (if ENABLE(INLINE_PATH_DATA))
- `FillPathSegment(WebCore::PathSegment segment)` (StreamBatched)
- `FillPath(WebCore::Path path)`
- `FillEllipse(WebCore::FloatRect rect)`
- `StrokeRect(WebCore::FloatRect rect, float lineWidth)`
- `StrokeLine(WebCore::PathDataLine line)` (StreamBatched, if ENABLE(INLINE_PATH_DATA))
- `StrokeLineWithColorAndThickness(WebCore::PathDataLine line, WebCore::DisplayList::SetInlineStroke strokeItem)` (StreamBatched, if ENABLE(INLINE_PATH_DATA))
- `StrokeArc(WebCore::PathArc arc)` (StreamBatched, if ENABLE(INLINE_PATH_DATA))
- `StrokeClosedArc(WebCore::PathClosedArc closedArc)` (StreamBatched, if ENABLE(INLINE_PATH_DATA))
- `StrokeQuadCurve(WebCore::PathDataQuadCurve curve)` (StreamBatched, if ENABLE(INLINE_PATH_DATA))
- `StrokeBezierCurve(WebCore::PathDataBezierCurve curve)` (StreamBatched, if ENABLE(INLINE_PATH_DATA))
- `StrokePathSegment(WebCore::PathSegment segment)` (StreamBatched)
- `StrokePath(WebCore::Path path)` (StreamBatched)
- `StrokeEllipse(WebCore::FloatRect rect)` (StreamBatched)
- `ClearRect(WebCore::FloatRect rect)`
- `DrawControlPart(Ref<WebCore::ControlPart> part, WebCore::FloatRoundedRect borderRect, float deviceScaleFactor, WebCore::ControlStyle style)`
- `ApplyStrokePattern()` (if USE(CG))
- `ApplyFillPattern()` (if USE(CG))
- `ApplyDeviceScaleFactor(float scaleFactor)`
- `BeginPage(WebCore::IntSize pageSize)`
- `EndPage()`
- `SetURLForRect(URL link, WebCore::FloatRect destRect)`
- `DrawVideoFrame(WebKit::SharedVideoFrame frame, WebCore::FloatRect rect, WebCore::ImageOrientation orientation, bool shouldDiscardAlpha)` (NotStreamEncodable, if PLATFORM(COCOA) && ENABLE(VIDEO))
- `SetSharedVideoFrameSemaphore(IPC::Semaphore semaphore)` (NotStreamEncodable, if PLATFORM(COCOA) && ENABLE(VIDEO))
- `SetSharedVideoFrameMemory(WebCore::SharedMemory::Handle storageHandle)` (NotStreamEncodable, if PLATFORM(COCOA) && ENABLE(VIDEO))

## `RemoteExternalTexture` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteExternalTexture.messages.in`

- `Destruct()`
- `SetLabel(String label)`
- `Destroy()`
- `Undestroy()`

## `RemoteFaceDetector` - WebContent -> GPU

`GPUProcess/ShapeDetection/RemoteFaceDetector.messages.in`

- `Detect(WebCore::RenderingResourceIdentifier renderingResourceIdentifier) -> (Vector<WebCore::ShapeDetection::DetectedFace> detectedFaces)`

## `RemoteGPU` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteGPU.messages.in`

- `RequestAdapter(WebKit::WebGPU::RequestAdapterOptions options, WebKit::WebGPUIdentifier identifier) -> (std::optional<WebKit::RemoteGPURequestAdapterResponse> response)` (sync)
- `CreatePresentationContext(WebKit::WebGPU::PresentationContextDescriptor descriptor, WebKit::WebGPUIdentifier identifier)`
- `CreateCompositorIntegration(WebKit::WebGPUIdentifier identifier)`
- `IsValid(WebKit::WebGPUIdentifier identifier) -> (bool isValid, bool exists)` (sync)

## `RemoteGraphicsContextGL` - WebContent -> GPU

`GPUProcess/graphics/RemoteGraphicsContextGL.messages.in`

- `Reshape(int32_t width, int32_t height)`
- `PrepareForDisplay(IPC::Semaphore finishedFence) -> (MachSendRight displayBuffer)` (NotStreamEncodable, NotStreamEncodableReply, sync, if PLATFORM(COCOA))
- `PrepareForDisplay() -> (std::optional<WebKit::WCContentBufferIdentifier> contentBuffer)` (sync, if USE(GRAPHICS_LAYER_WC))
- `PrepareForDisplay() -> (uint64_t bufferID, std::optional<WebCore::DMABufBufferAttributes> dmabufAttributes, UnixFileDescriptor fenceFD)` (NotStreamEncodableReply, sync, if USE(GBM))
- `PrepareForDisplay() -> ()` (sync, if !PLATFORM(COCOA) && !USE(GRAPHICS_LAYER_WC) && !USE(GBM))
- `EnsureExtensionEnabled(String extension)`
- `GetErrors() -> (GCGLErrorCodeSet returnValue)` (sync)
- `DrawSurfaceBufferToImageBuffer(WebCore::GraphicsContextGLSurfaceBuffer buffer, WebCore::RenderingResourceIdentifier imageBuffer) -> ()` (sync)
- `SurfaceBufferToVideoFrame(WebCore::GraphicsContextGLSurfaceBuffer buffer) -> (std::optional<WebKit::RemoteVideoFrameProxyProperties> properties)` (sync, if ENABLE(MEDIA_STREAM) || ENABLE(WEB_CODECS))
- `CopyTextureFromVideoFrame(WebKit::SharedVideoFrame frame, PlatformGLObject texture, uint32_t target, int32_t level, uint32_t internalFormat, uint32_t format, uint32_t type, bool premultiplyAlpha, bool flipY) -> (bool success)` (NotStreamEncodable, sync, if ENABLE(VIDEO) && PLATFORM(COCOA))
- `SetSharedVideoFrameSemaphore(IPC::Semaphore semaphore)` (NotStreamEncodable, if ENABLE(VIDEO) && PLATFORM(COCOA))
- `SetSharedVideoFrameMemory(WebCore::SharedMemory::Handle storageHandle)` (NotStreamEncodable, if ENABLE(VIDEO) && PLATFORM(COCOA))
- `SimulateEventForTesting(WebCore::GraphicsContextGLSimulatedEventForTesting event)`
- `GetBufferSubDataInline(uint32_t target, uint64_t offset, size_t dataSize) -> (std::span<const uint8_t> data)` (sync)
- `GetBufferSubDataSharedMemory(uint32_t target, uint64_t offset, size_t dataSize, WebCore::SharedMemory::Handle handle) -> (bool valid)` (NotStreamEncodable, sync)
- `ReadPixelsInline(WebCore::IntRect rect, uint32_t format, uint32_t type, bool packReverseRowOrder) -> (std::optional<WebCore::IntSize> readArea, std::span<const uint8_t> data)` (sync)
- `ReadPixelsSharedMemory(WebCore::IntRect rect, uint32_t format, uint32_t type, bool packReverseRowOrder, WebCore::SharedMemory::Handle handle) -> (std::optional<WebCore::IntSize> readArea)` (NotStreamEncodable, sync)
- `MultiDrawArraysANGLE(uint32_t mode, IPC::ArrayReferenceTuple<int32_t, int32_t> firstsAndCounts)`
- `MultiDrawArraysInstancedANGLE(uint32_t mode, IPC::ArrayReferenceTuple<int32_t, int32_t, int32_t> firstsCountsAandInstanceCounts)`
- `MultiDrawElementsANGLE(uint32_t mode, IPC::ArrayReferenceTuple<int32_t, int32_t> countsAndOffsets, uint32_t type)`
- `MultiDrawElementsInstancedANGLE(uint32_t mode, IPC::ArrayReferenceTuple<int32_t, int32_t, int32_t> countsOffsetsAndInstanceCounts, uint32_t type)`
- `MultiDrawArraysInstancedBaseInstanceANGLE(uint32_t mode, IPC::ArrayReferenceTuple<int32_t, int32_t, int32_t, uint32_t> firstsCountsInstanceCountsAndBaseInstances)`
- `MultiDrawElementsInstancedBaseVertexBaseInstanceANGLE(uint32_t mode, IPC::ArrayReferenceTuple<int32_t, int32_t, int32_t, int32_t, uint32_t> countsOffsetsInstanceCountsBaseVerticesAndBaseInstances, uint32_t type)`
- `ActiveTexture(uint32_t texture)`
- `AttachShader(uint32_t program, uint32_t shader)`
- `BindAttribLocation(uint32_t arg0, uint32_t index, String name)`
- `BindBuffer(uint32_t target, uint32_t arg1)`
- `BindFramebuffer(uint32_t target, uint32_t arg1)`
- `BindRenderbuffer(uint32_t target, uint32_t arg1)`
- `BindTexture(uint32_t target, uint32_t arg1)`
- `BlendColor(float red, float green, float blue, float alpha)`
- `BlendEquation(uint32_t mode)`
- `BlendEquationSeparate(uint32_t modeRGB, uint32_t modeAlpha)`
- `BlendFunc(uint32_t sfactor, uint32_t dfactor)`
- `BlendFuncSeparate(uint32_t srcRGB, uint32_t dstRGB, uint32_t srcAlpha, uint32_t dstAlpha)`
- `CheckFramebufferStatus(uint32_t target) -> (uint32_t returnValue)` (sync)
- `Clear(uint32_t mask)`
- `ClearColor(float red, float green, float blue, float alpha)`
- `ClearDepth(float depth)`
- `ClearStencil(int32_t s)`
- `ColorMask(bool red, bool green, bool blue, bool alpha)`
- `CompileShader(uint32_t arg0)`
- `CopyTexImage2D(uint32_t target, int32_t level, uint32_t internalformat, int32_t x, int32_t y, int32_t width, int32_t height, int32_t border)`
- `CopyTexSubImage2D(uint32_t target, int32_t level, int32_t xoffset, int32_t yoffset, int32_t x, int32_t y, int32_t width, int32_t height)`
- `CreateBuffer(uint32_t buffer)`
- `CreateFramebuffer(uint32_t framebuffer)`
- `CreateProgram(uint32_t program)`
- `CreateRenderbuffer(uint32_t renderbuffer)`
- `CreateShader(uint32_t shader, uint32_t arg0)`
- `CreateTexture(uint32_t texture)`
- `CullFace(uint32_t mode)`
- `DeleteBuffer(uint32_t arg0)`
- `DeleteFramebuffer(uint32_t arg0)`
- `DeleteProgram(uint32_t arg0)`
- `DeleteRenderbuffer(uint32_t arg0)`
- `DeleteShader(uint32_t arg0)`
- `DeleteTexture(uint32_t arg0)`
- `DepthFunc(uint32_t func)`
- `DepthMask(bool flag)`
- `DepthRange(float zNear, float zFar)`
- `DetachShader(uint32_t arg0, uint32_t arg1)`
- `Disable(uint32_t cap)`
- `DisableVertexAttribArray(uint32_t index)`
- `DrawArrays(uint32_t mode, int32_t first, int32_t count)`
- `DrawElements(uint32_t mode, int32_t count, uint32_t type, uint64_t offset)`
- `Enable(uint32_t cap)`
- `EnableVertexAttribArray(uint32_t index)`
- `Finish()`
- `Flush()`
- `FramebufferRenderbuffer(uint32_t target, uint32_t attachment, uint32_t renderbuffertarget, uint32_t arg3)`
- `FramebufferTexture2D(uint32_t target, uint32_t attachment, uint32_t textarget, uint32_t arg3, int32_t level)`
- `FrontFace(uint32_t mode)`
- `GenerateMipmap(uint32_t target)`
- `GetActiveAttrib(uint32_t program, uint32_t index) -> (bool returnValue, WebCore::GraphicsContextGLActiveInfo arg2)` (sync)
- `GetActiveUniform(uint32_t program, uint32_t index) -> (bool returnValue, WebCore::GraphicsContextGLActiveInfo arg2)` (sync)
- `GetAttribLocation(uint32_t arg0, String name) -> (int32_t returnValue)` (sync)
- `GetBufferParameteri(uint32_t target, uint32_t pname) -> (int32_t returnValue)` (sync)
- `GetString(uint32_t name) -> (String returnValue)` (sync)
- `GetFloatv(uint32_t pname, size_t valueSize) -> (std::span<const float> value)` (sync)
- `GetIntegerv(uint32_t pname, size_t valueSize) -> (std::span<const int32_t> value)` (sync)
- `GetIntegeri_v(uint32_t pname, uint32_t index) -> (std::span<const int32_t, 4> value)` (sync)
- `GetInteger64(uint32_t pname) -> (int64_t returnValue)` (sync)
- `GetInteger64i(uint32_t pname, uint32_t index) -> (int64_t returnValue)` (sync)
- `GetProgrami(uint32_t program, uint32_t pname) -> (int32_t returnValue)` (sync)
- `GetBooleanv(uint32_t pname, size_t valueSize) -> (std::span<const bool> value)` (sync)
- `GetFramebufferAttachmentParameteri(uint32_t target, uint32_t attachment, uint32_t pname) -> (int32_t returnValue)` (sync)
- `GetProgramInfoLog(uint32_t arg0) -> (String returnValue)` (sync)
- `GetRenderbufferParameteri(uint32_t target, uint32_t pname) -> (int32_t returnValue)` (sync)
- `GetShaderi(uint32_t arg0, uint32_t pname) -> (int32_t returnValue)` (sync)
- `GetShaderInfoLog(uint32_t arg0) -> (String returnValue)` (sync)
- `GetShaderPrecisionFormat(uint32_t shaderType, uint32_t precisionType) -> (std::span<const int32_t, 2> range, GCGLint precision)` (sync)
- `GetShaderSource(uint32_t arg0) -> (String returnValue)` (sync)
- `GetTexParameterf(uint32_t target, uint32_t pname) -> (float returnValue)` (sync)
- `GetTexParameteri(uint32_t target, uint32_t pname) -> (int32_t returnValue)` (sync)
- `GetUniformfv(uint32_t program, int32_t location, size_t valueSize) -> (std::span<const float> value)` (sync)
- `GetUniformiv(uint32_t program, int32_t location, size_t valueSize) -> (std::span<const int32_t> value)` (sync)
- `GetUniformuiv(uint32_t program, int32_t location, size_t valueSize) -> (std::span<const uint32_t> value)` (sync)
- `GetUniformLocation(uint32_t arg0, String name) -> (int32_t returnValue)` (sync)
- `GetVertexAttribOffset(uint32_t index, uint32_t pname) -> (uint64_t returnValue)` (sync)
- `Hint(uint32_t target, uint32_t mode)`
- `IsBuffer(uint32_t arg0) -> (bool returnValue)` (sync)
- `IsEnabled(uint32_t cap) -> (bool returnValue)` (sync)
- `IsFramebuffer(uint32_t arg0) -> (bool returnValue)` (sync)
- `IsProgram(uint32_t arg0) -> (bool returnValue)` (sync)
- `IsRenderbuffer(uint32_t arg0) -> (bool returnValue)` (sync)
- `IsShader(uint32_t arg0) -> (bool returnValue)` (sync)
- `IsTexture(uint32_t arg0) -> (bool returnValue)` (sync)
- `LineWidth(float arg0)`
- `LinkProgram(uint32_t arg0)`
- `PixelStorei(uint32_t pname, int32_t param)`
- `PolygonOffset(float factor, float units)`
- `RenderbufferStorage(uint32_t target, uint32_t internalformat, int32_t width, int32_t height)`
- `SampleCoverage(float value, bool invert)`
- `Scissor(int32_t x, int32_t y, int32_t width, int32_t height)`
- `ShaderSource(uint32_t arg0, String arg1)`
- `StencilFunc(uint32_t func, int32_t ref, uint32_t mask)`
- `StencilFuncSeparate(uint32_t face, uint32_t func, int32_t ref, uint32_t mask)`
- `StencilMask(uint32_t mask)`
- `StencilMaskSeparate(uint32_t face, uint32_t mask)`
- `StencilOp(uint32_t fail, uint32_t zfail, uint32_t zpass)`
- `StencilOpSeparate(uint32_t face, uint32_t fail, uint32_t zfail, uint32_t zpass)`
- `TexParameterf(uint32_t target, uint32_t pname, float param)`
- `TexParameteri(uint32_t target, uint32_t pname, int32_t param)`
- `Uniform1f(int32_t location, float x)`
- `Uniform1fv(int32_t location, std::span<const float> v)`
- `Uniform1i(int32_t location, int32_t x)`
- `Uniform1iv(int32_t location, std::span<const int32_t> v)`
- `Uniform2f(int32_t location, float x, float y)`
- `Uniform2fv(int32_t location, std::span<const float> v)`
- `Uniform2i(int32_t location, int32_t x, int32_t y)`
- `Uniform2iv(int32_t location, std::span<const int32_t> v)`
- `Uniform3f(int32_t location, float x, float y, float z)`
- `Uniform3fv(int32_t location, std::span<const float> v)`
- `Uniform3i(int32_t location, int32_t x, int32_t y, int32_t z)`
- `Uniform3iv(int32_t location, std::span<const int32_t> v)`
- `Uniform4f(int32_t location, float x, float y, float z, float w)`
- `Uniform4fv(int32_t location, std::span<const float> v)`
- `Uniform4i(int32_t location, int32_t x, int32_t y, int32_t z, int32_t w)`
- `Uniform4iv(int32_t location, std::span<const int32_t> v)`
- `UniformMatrix2fv(int32_t location, bool transpose, std::span<const float> value)`
- `UniformMatrix3fv(int32_t location, bool transpose, std::span<const float> value)`
- `UniformMatrix4fv(int32_t location, bool transpose, std::span<const float> value)`
- `UseProgram(uint32_t arg0)`
- `ValidateProgram(uint32_t arg0)`
- `VertexAttrib1f(uint32_t index, float x)`
- `VertexAttrib1fv(uint32_t index, std::span<const float, 1> values)`
- `VertexAttrib2f(uint32_t index, float x, float y)`
- `VertexAttrib2fv(uint32_t index, std::span<const float, 2> values)`
- `VertexAttrib3f(uint32_t index, float x, float y, float z)`
- `VertexAttrib3fv(uint32_t index, std::span<const float, 3> values)`
- `VertexAttrib4f(uint32_t index, float x, float y, float z, float w)`
- `VertexAttrib4fv(uint32_t index, std::span<const float, 4> values)`
- `VertexAttribPointer(uint32_t index, int32_t size, uint32_t type, bool normalized, int32_t stride, uint64_t offset)`
- `Viewport(int32_t x, int32_t y, int32_t width, int32_t height)`
- `BufferData0(uint32_t target, uint64_t arg1, uint32_t usage)`
- `BufferData1(uint32_t target, std::span<const uint8_t> data, uint32_t usage)`
- `BufferSubData(uint32_t target, uint64_t offset, std::span<const uint8_t> data)`
- `ReadPixelsBufferObject(WebCore::IntRect arg0, uint32_t format, uint32_t type, uint64_t offset, int32_t alignment, int32_t rowLength)`
- `TexImage2D0(uint32_t target, int32_t level, uint32_t internalformat, int32_t width, int32_t height, int32_t border, uint32_t format, uint32_t type, std::span<const uint8_t> pixels)`
- `TexImage2D1(uint32_t target, int32_t level, uint32_t internalformat, int32_t width, int32_t height, int32_t border, uint32_t format, uint32_t type, uint64_t offset)`
- `TexSubImage2D0(uint32_t target, int32_t level, int32_t xoffset, int32_t yoffset, int32_t width, int32_t height, uint32_t format, uint32_t type, std::span<const uint8_t> pixels)`
- `TexSubImage2D1(uint32_t target, int32_t level, int32_t xoffset, int32_t yoffset, int32_t width, int32_t height, uint32_t format, uint32_t type, uint64_t offset)`
- `CompressedTexImage2D0(uint32_t target, int32_t level, uint32_t internalformat, int32_t width, int32_t height, int32_t border, int32_t imageSize, std::span<const uint8_t> data)`
- `CompressedTexImage2D1(uint32_t target, int32_t level, uint32_t internalformat, int32_t width, int32_t height, int32_t border, int32_t imageSize, uint64_t offset)`
- `CompressedTexSubImage2D0(uint32_t target, int32_t level, int32_t xoffset, int32_t yoffset, int32_t width, int32_t height, uint32_t format, int32_t imageSize, std::span<const uint8_t> data)`
- `CompressedTexSubImage2D1(uint32_t target, int32_t level, int32_t xoffset, int32_t yoffset, int32_t width, int32_t height, uint32_t format, int32_t imageSize, uint64_t offset)`
- `DrawArraysInstanced(uint32_t mode, int32_t first, int32_t count, int32_t primcount)`
- `DrawElementsInstanced(uint32_t mode, int32_t count, uint32_t type, uint64_t offset, int32_t primcount)`
- `VertexAttribDivisor(uint32_t index, uint32_t divisor)`
- `CreateVertexArray(uint32_t vertexArray)`
- `DeleteVertexArray(uint32_t arg0)`
- `IsVertexArray(uint32_t arg0) -> (bool returnValue)` (sync)
- `BindVertexArray(uint32_t arg0)`
- `CopyBufferSubData(uint32_t readTarget, uint32_t writeTarget, uint64_t readOffset, uint64_t writeOffset, uint64_t arg4)`
- `BlitFramebuffer(int32_t srcX0, int32_t srcY0, int32_t srcX1, int32_t srcY1, int32_t dstX0, int32_t dstY0, int32_t dstX1, int32_t dstY1, uint32_t mask, uint32_t filter)`
- `FramebufferTextureLayer(uint32_t target, uint32_t attachment, uint32_t texture, int32_t level, int32_t layer)`
- `InvalidateFramebuffer(uint32_t target, std::span<const uint32_t> attachments)`
- `InvalidateSubFramebuffer(uint32_t target, std::span<const uint32_t> attachments, int32_t x, int32_t y, int32_t width, int32_t height)`
- `ReadBuffer(uint32_t src)`
- `RenderbufferStorageMultisample(uint32_t target, int32_t samples, uint32_t internalformat, int32_t width, int32_t height)`
- `TexStorage2D(uint32_t target, int32_t levels, uint32_t internalformat, int32_t width, int32_t height)`
- `TexStorage3D(uint32_t target, int32_t levels, uint32_t internalformat, int32_t width, int32_t height, int32_t depth)`
- `TexImage3D0(uint32_t target, int32_t level, int32_t internalformat, int32_t width, int32_t height, int32_t depth, int32_t border, uint32_t format, uint32_t type, std::span<const uint8_t> pixels)`
- `TexImage3D1(uint32_t target, int32_t level, int32_t internalformat, int32_t width, int32_t height, int32_t depth, int32_t border, uint32_t format, uint32_t type, uint64_t offset)`
- `TexSubImage3D0(uint32_t target, int32_t level, int32_t xoffset, int32_t yoffset, int32_t zoffset, int32_t width, int32_t height, int32_t depth, uint32_t format, uint32_t type, std::span<const uint8_t> pixels)`
- `TexSubImage3D1(uint32_t target, int32_t level, int32_t xoffset, int32_t yoffset, int32_t zoffset, int32_t width, int32_t height, int32_t depth, uint32_t format, uint32_t type, uint64_t offset)`
- `CopyTexSubImage3D(uint32_t target, int32_t level, int32_t xoffset, int32_t yoffset, int32_t zoffset, int32_t x, int32_t y, int32_t width, int32_t height)`
- `CompressedTexImage3D0(uint32_t target, int32_t level, uint32_t internalformat, int32_t width, int32_t height, int32_t depth, int32_t border, int32_t imageSize, std::span<const uint8_t> data)`
- `CompressedTexImage3D1(uint32_t target, int32_t level, uint32_t internalformat, int32_t width, int32_t height, int32_t depth, int32_t border, int32_t imageSize, uint64_t offset)`
- `CompressedTexSubImage3D0(uint32_t target, int32_t level, int32_t xoffset, int32_t yoffset, int32_t zoffset, int32_t width, int32_t height, int32_t depth, uint32_t format, int32_t imageSize, std::span<const uint8_t> data)`
- `CompressedTexSubImage3D1(uint32_t target, int32_t level, int32_t xoffset, int32_t yoffset, int32_t zoffset, int32_t width, int32_t height, int32_t depth, uint32_t format, int32_t imageSize, uint64_t offset)`
- `GetFragDataLocation(uint32_t program, String name) -> (int32_t returnValue)` (sync)
- `Uniform1ui(int32_t location, uint32_t v0)`
- `Uniform2ui(int32_t location, uint32_t v0, uint32_t v1)`
- `Uniform3ui(int32_t location, uint32_t v0, uint32_t v1, uint32_t v2)`
- `Uniform4ui(int32_t location, uint32_t v0, uint32_t v1, uint32_t v2, uint32_t v3)`
- `Uniform1uiv(int32_t location, std::span<const uint32_t> data)`
- `Uniform2uiv(int32_t location, std::span<const uint32_t> data)`
- `Uniform3uiv(int32_t location, std::span<const uint32_t> data)`
- `Uniform4uiv(int32_t location, std::span<const uint32_t> data)`
- `UniformMatrix2x3fv(int32_t location, bool transpose, std::span<const float> data)`
- `UniformMatrix3x2fv(int32_t location, bool transpose, std::span<const float> data)`
- `UniformMatrix2x4fv(int32_t location, bool transpose, std::span<const float> data)`
- `UniformMatrix4x2fv(int32_t location, bool transpose, std::span<const float> data)`
- `UniformMatrix3x4fv(int32_t location, bool transpose, std::span<const float> data)`
- `UniformMatrix4x3fv(int32_t location, bool transpose, std::span<const float> data)`
- `VertexAttribI4i(uint32_t index, int32_t x, int32_t y, int32_t z, int32_t w)`
- `VertexAttribI4iv(uint32_t index, std::span<const int32_t, 4> values)`
- `VertexAttribI4ui(uint32_t index, uint32_t x, uint32_t y, uint32_t z, uint32_t w)`
- `VertexAttribI4uiv(uint32_t index, std::span<const uint32_t, 4> values)`
- `VertexAttribIPointer(uint32_t index, int32_t size, uint32_t type, int32_t stride, uint64_t offset)`
- `DrawRangeElements(uint32_t mode, uint32_t start, uint32_t end, int32_t count, uint32_t type, uint64_t offset)`
- `DrawBuffers(std::span<const uint32_t> bufs)`
- `ClearBufferiv(uint32_t buffer, int32_t drawbuffer, std::span<const int32_t> values)`
- `ClearBufferuiv(uint32_t buffer, int32_t drawbuffer, std::span<const uint32_t> values)`
- `ClearBufferfv(uint32_t buffer, int32_t drawbuffer, std::span<const float> values)`
- `ClearBufferfi(uint32_t buffer, int32_t drawbuffer, float depth, int32_t stencil)`
- `CreateQuery(uint32_t query)`
- `DeleteQuery(uint32_t query)`
- `IsQuery(uint32_t query) -> (bool returnValue)` (sync)
- `BeginQuery(uint32_t target, uint32_t query)`
- `EndQuery(uint32_t target)`
- `GetQuery(uint32_t target, uint32_t pname) -> (int32_t returnValue)` (sync)
- `GetQueryObjectui(uint32_t query, uint32_t pname) -> (uint32_t returnValue)` (sync)
- `CreateSampler(uint32_t sampler)`
- `DeleteSampler(uint32_t sampler)`
- `IsSampler(uint32_t sampler) -> (bool returnValue)` (sync)
- `BindSampler(uint32_t unit, uint32_t sampler)`
- `SamplerParameteri(uint32_t sampler, uint32_t pname, int32_t param)`
- `SamplerParameterf(uint32_t sampler, uint32_t pname, float param)`
- `GetSamplerParameterf(uint32_t sampler, uint32_t pname) -> (float returnValue)` (sync)
- `GetSamplerParameteri(uint32_t sampler, uint32_t pname) -> (int32_t returnValue)` (sync)
- `FenceSync(uint32_t condition, uint32_t flags) -> (uint64_t returnValue)` (sync)
- `IsSync(uint64_t arg0) -> (bool returnValue)` (sync)
- `DeleteSync(uint64_t arg0)`
- `ClientWaitSync(uint64_t arg0, uint32_t flags, uint64_t timeout) -> (uint32_t returnValue)` (sync)
- `WaitSync(uint64_t arg0, uint32_t flags, int64_t timeout)`
- `GetSynci(uint64_t arg0, uint32_t pname) -> (int32_t returnValue)` (sync)
- `CreateTransformFeedback(uint32_t transformFeedback)`
- `DeleteTransformFeedback(uint32_t id)`
- `IsTransformFeedback(uint32_t id) -> (bool returnValue)` (sync)
- `BindTransformFeedback(uint32_t target, uint32_t id)`
- `BeginTransformFeedback(uint32_t primitiveMode)`
- `EndTransformFeedback()`
- `TransformFeedbackVaryings(uint32_t program, Vector<String> varyings, uint32_t bufferMode)`
- `GetTransformFeedbackVarying(uint32_t program, uint32_t index) -> (WebCore::GraphicsContextGLActiveInfo arg2)` (sync)
- `PauseTransformFeedback()`
- `ResumeTransformFeedback()`
- `BindBufferBase(uint32_t target, uint32_t index, uint32_t buffer)`
- `BindBufferRange(uint32_t target, uint32_t index, uint32_t buffer, uint64_t offset, uint64_t arg4)`
- `GetUniformIndices(uint32_t program, Vector<String> uniformNames) -> (Vector<uint32_t> returnValue)` (sync)
- `GetActiveUniforms(uint32_t program, Vector<uint32_t> uniformIndices, uint32_t pname) -> (Vector<int32_t> returnValue)` (sync)
- `GetUniformBlockIndex(uint32_t program, String uniformBlockName) -> (uint32_t returnValue)` (sync)
- `GetActiveUniformBlockName(uint32_t program, uint32_t uniformBlockIndex) -> (String returnValue)` (sync)
- `UniformBlockBinding(uint32_t program, uint32_t uniformBlockIndex, uint32_t uniformBlockBinding)`
- `GetActiveUniformBlockiv(uint32_t program, uint32_t uniformBlockIndex, uint32_t pname, size_t paramsSize) -> (std::span<const int32_t> params)` (sync)
- `GetTranslatedShaderSourceANGLE(uint32_t arg0) -> (String returnValue)` (sync)
- `DrawBuffersEXT(std::span<const uint32_t> bufs)`
- `CreateQueryEXT(uint32_t queryEXT)`
- `DeleteQueryEXT(uint32_t query)`
- `IsQueryEXT(uint32_t query) -> (bool returnValue)` (sync)
- `BeginQueryEXT(uint32_t target, uint32_t query)`
- `EndQueryEXT(uint32_t target)`
- `QueryCounterEXT(uint32_t query, uint32_t target)`
- `GetQueryiEXT(uint32_t target, uint32_t pname) -> (int32_t returnValue)` (sync)
- `GetQueryObjectiEXT(uint32_t query, uint32_t pname) -> (int32_t returnValue)` (sync)
- `GetQueryObjectui64EXT(uint32_t query, uint32_t pname) -> (uint64_t returnValue)` (sync)
- `GetInteger64EXT(uint32_t pname) -> (int64_t returnValue)` (sync)
- `EnableiOES(uint32_t target, uint32_t index)`
- `DisableiOES(uint32_t target, uint32_t index)`
- `BlendEquationiOES(uint32_t buf, uint32_t mode)`
- `BlendEquationSeparateiOES(uint32_t buf, uint32_t modeRGB, uint32_t modeAlpha)`
- `BlendFunciOES(uint32_t buf, uint32_t src, uint32_t dst)`
- `BlendFuncSeparateiOES(uint32_t buf, uint32_t srcRGB, uint32_t dstRGB, uint32_t srcAlpha, uint32_t dstAlpha)`
- `ColorMaskiOES(uint32_t buf, bool red, bool green, bool blue, bool alpha)`
- `DrawArraysInstancedBaseInstanceANGLE(uint32_t mode, int32_t first, int32_t count, int32_t instanceCount, uint32_t baseInstance)`
- `DrawElementsInstancedBaseVertexBaseInstanceANGLE(uint32_t mode, int32_t count, uint32_t type, uint64_t offset, int32_t instanceCount, int32_t baseVertex, uint32_t baseInstance)`
- `ClipControlEXT(uint32_t origin, uint32_t depth)`
- `ProvokingVertexANGLE(uint32_t provokeMode)`
- `PolygonModeANGLE(uint32_t face, uint32_t mode)`
- `PolygonOffsetClampEXT(float factor, float units, float clamp)`
- `RenderbufferStorageMultisampleANGLE(uint32_t target, int32_t samples, uint32_t internalformat, int32_t width, int32_t height)`
- `GetInternalformativ(uint32_t target, uint32_t internalformat, uint32_t pname, size_t paramsSize) -> (std::span<const int32_t> params)` (sync)
- `SetDrawingBufferColorSpace(WebCore::DestinationColorSpace arg0)`
- `CreateExternalImage(uint32_t externalImage, WebCore::GraphicsContextGL::ExternalImageSource arg0, uint32_t internalFormat, int32_t layer)` (NotStreamEncodable, if ENABLE(WEBXR))
- `DeleteExternalImage(uint32_t handle)` (if ENABLE(WEBXR))
- `BindExternalImage(uint32_t target, uint32_t arg1)` (if ENABLE(WEBXR))
- `CreateExternalSync(uint32_t externalSync, WebCore::GraphicsContextGL::ExternalSyncSource arg0)` (NotStreamEncodable, if ENABLE(WEBXR))
- `DeleteExternalSync(uint32_t arg0)`
- `EnableRequiredWebXRExtensions() -> (bool returnValue)` (sync, if ENABLE(WEBXR))
- `AddFoveation(WebCore::IntSize physicalSizeLeft, WebCore::IntSize physicalSizeRight, WebCore::IntSize screenSize, std::span<const float> horizontalSamplesLeft, std::span<const float> verticalSamples, std::span<const float> horizontalSamplesRight) -> (bool returnValue)` (sync, if ENABLE(WEBXR))
- `EnableFoveation(uint32_t arg0)` (if ENABLE(WEBXR))
- `DisableFoveation()` (if ENABLE(WEBXR))
- `FramebufferDiscard(uint32_t target, std::span<const uint32_t> attachments)` (if ENABLE(WEBXR))
- `FramebufferResolveRenderbuffer(uint32_t target, uint32_t attachment, uint32_t renderbuffertarget, uint32_t arg3)` (if ENABLE(WEBXR))

## `RemoteImageBuffer` - WebContent -> GPU

`GPUProcess/graphics/RemoteImageBuffer.messages.in`

- `GetPixelBuffer(WebCore::PixelBufferFormat outputFormat, WebCore::IntPoint srcPoint, WebCore::IntSize srcSize) -> ()` (sync)
- `GetPixelBufferWithNewMemory(WebCore::SharedMemory::Handle handle, WebCore::PixelBufferFormat outputFormat, WebCore::IntPoint srcPoint, WebCore::IntSize srcSize) -> ()` (NotStreamEncodable, sync)
- `PutPixelBuffer(Ref<WebCore::PixelBuffer> pixelBuffer, WebCore::IntPoint srcPoint, WebCore::IntSize srcSize, WebCore::IntPoint destPoint, WebCore::AlphaPremultiplication destFormat)`
- `GetShareableBitmap(WebCore::PreserveResolution preserveResolution) -> (std::optional<WebCore::ShareableBitmapHandle> handle)` (NotStreamEncodableReply, sync)
- `FilteredNativeImage(Ref<WebCore::Filter> filter) -> (std::optional<WebCore::ShareableBitmapHandle> handle)` (NotStreamEncodableReply, sync)
- `ConvertToLuminanceMask()`
- `TransformToColorSpace(WebCore::DestinationColorSpace colorSpace)`
- `FlushContext()`
- `FlushContextSync() -> ()` (sync)
- `DynamicContentScalingDisplayList() -> (std::optional<WebCore::DynamicContentScalingDisplayList> displayList)` (NotStreamEncodableReply, sync, if ENABLE(RE_DYNAMIC_CONTENT_SCALING))

## `RemoteImageBufferSet` - WebContent -> GPU

`GPUProcess/graphics/RemoteImageBufferSet.messages.in`

- `UpdateConfiguration(WebCore::FloatSize logicalSize, WebCore::RenderingMode renderingMode, WebCore::RenderingPurpose renderingPurpose, float resolutionScale, WebCore::DestinationColorSpace colorSpace, WebCore::ImageBufferPixelFormat pixelFormat)`
- `EndPrepareForDisplay(WebKit::RenderingUpdateID renderingUpdateID)`
- `DynamicContentScalingDisplayList() -> (std::optional<WebCore::DynamicContentScalingDisplayList> displayList)` (NotStreamEncodableReply, sync, if ENABLE(RE_DYNAMIC_CONTENT_SCALING))

## `RemoteImageDecoderAVFProxy` - WebContent -> GPU

`GPUProcess/media/RemoteImageDecoderAVFProxy.messages.in`

- `CreateDecoder(IPC::SharedBufferReference data, String mimeType) -> (std::optional<WebCore::ImageDecoderIdentifier> identifier)` (sync)
- `DeleteDecoder(WebCore::ImageDecoderIdentifier identifier)`
- `SetExpectedContentSize(WebCore::ImageDecoderIdentifier identifier, long long expectedContentSize)`
- `SetData(WebCore::ImageDecoderIdentifier identifier, IPC::SharedBufferReference data, bool allDataReceived) -> (size_t frameCount, WebCore::IntSize size, bool hasTrack, std::optional<Vector<WebCore::ImageDecoderFrameInfo>> frameInfos)` (sync)
- `CreateFrameImageAtIndex(WebCore::ImageDecoderIdentifier identifier, size_t index) -> (std::optional<WebCore::ShareableBitmapHandle> imageHandle)` (sync)
- `ClearFrameBufferCache(WebCore::ImageDecoderIdentifier identifier, size_t index)`

## `RemoteLegacyCDMFactoryProxy` - WebContent -> GPU

`GPUProcess/media/RemoteLegacyCDMFactoryProxy.messages.in`

- `CreateCDM(String keySystem, std::optional<WebCore::MediaPlayerIdentifier> playerId) -> (std::optional<WebKit::RemoteLegacyCDMIdentifier> identifier)` (sync)
- `SupportsKeySystem(String keySystem, std::optional<String> mimeType) -> (bool result)` (sync)
- `RemoveSession(WebKit::RemoteLegacyCDMSessionIdentifier identifier) -> ()`

## `RemoteLegacyCDMProxy` - WebContent -> GPU

`GPUProcess/media/RemoteLegacyCDMProxy.messages.in`

- `SupportsMIMEType(String mimeType) -> (bool supports)` (sync)
- `CreateSession(String mediaKeysStorageDirectory, uint64_t logIdentifier) -> (std::optional<WebKit::RemoteLegacyCDMSessionIdentifier> identifier)` (sync)
- `SetPlayerId(std::optional<WebCore::MediaPlayerIdentifier> playerId)`

## `RemoteLegacyCDMSessionProxy` - WebContent -> GPU

`GPUProcess/media/RemoteLegacyCDMSessionProxy.messages.in`

- `GenerateKeyRequest(String mimeType, RefPtr<WebCore::SharedBuffer> initData) -> (RefPtr<WebCore::SharedBuffer> nextMessage, String destinationURL, unsigned short errorCode, uint32_t systemCode)` (sync)
- `ReleaseKeys()`
- `Update(RefPtr<WebCore::SharedBuffer> update) -> (bool succeeded, RefPtr<WebCore::SharedBuffer> nextMessage, unsigned short errorCode, uint32_t systemCode)` (sync)
- `CachedKeyForKeyID(String keyId) -> (RefPtr<WebCore::SharedBuffer> key)` (sync)

## `RemoteMediaEngineConfigurationFactoryProxy` - WebContent -> GPU

`GPUProcess/media/RemoteMediaEngineConfigurationFactoryProxy.messages.in`

- `CreateDecodingConfiguration(WebCore::MediaDecodingConfiguration configuration) -> (WebCore::MediaCapabilitiesDecodingInfo decodingInfo)`
- `CreateEncodingConfiguration(WebCore::MediaEncodingConfiguration configuration) -> (WebCore::MediaCapabilitiesEncodingInfo decodingInfo)`

## `RemoteMediaPlayerManagerProxy` - WebContent -> GPU

`GPUProcess/media/RemoteMediaPlayerManagerProxy.messages.in`

- `CreateMediaPlayer(WebCore::MediaPlayerIdentifier identifier, WebCore::MediaPlayerClientIdentifier clientIdentifier, WebCore::MediaPlayerMediaEngineIdentifier remoteEngineIdentifier, WebKit::RemoteMediaPlayerProxyConfiguration proxyConfiguration)`
- `DeleteMediaPlayer(WebCore::MediaPlayerIdentifier identifier)`
- `GetSupportedTypes(WebCore::MediaPlayerMediaEngineIdentifier remoteEngineIdentifier) -> (Vector<String> types)` (sync)
- `SupportsTypeAndCodecs(WebCore::MediaPlayerMediaEngineIdentifier remoteEngineIdentifier, WebCore::MediaEngineSupportParameters type) -> (WebCore::MediaPlayerSupportsType support)` (sync)
- `SupportsKeySystem(WebCore::MediaPlayerMediaEngineIdentifier remoteEngineIdentifier, String keySystem, String mimeType) -> (bool supports)` (sync)

## `RemoteMediaPlayerProxy` - WebContent -> GPU

`GPUProcess/media/RemoteMediaPlayerProxy.messages.in`

- `PrepareForPlayback(bool privateMode, WebCore::MediaPlayerPreload preload, bool preservesPitch, WebCore::MediaPlayerPitchCorrectionAlgorithm pitchCorrectionAlgorithm, bool prepareToPlay, bool prepareForRendering, WebCore::IntSize presentationSize, float videoContentScale, bool isFullscreen, WebCore::DynamicRangeMode mode)`
- `Load(URL url, std::optional<WebKit::SandboxExtensionHandle> sandboxExtension, WebCore::ContentType contentType, String keySystem, bool requiresRemotePlayback) -> (WebKit::RemoteMediaPlayerConfiguration playerConfiguration)`
- `LoadMediaSource(URL url, WebCore::ContentType contentType, WebKit::RemoteMediaSourceIdentifier mediaSourceIdentifier) -> (WebKit::RemoteMediaPlayerConfiguration playerConfiguration)` (if ENABLE(MEDIA_SOURCE))
- `CancelLoad()`
- `PrepareToPlay()`
- `Play()`
- `Pause()`
- `SetVolume(double volume)`
- `SetMuted(bool muted)`
- `SeekToTarget(WebCore::SeekTarget target)`
- `SetPreload(WebCore::MediaPlayerPreload preload)`
- `SetPrivateBrowsingMode(bool privateMode)`
- `SetPreservesPitch(bool preservesPitch)`
- `SetPitchCorrectionAlgorithm(WebCore::MediaPlayerPitchCorrectionAlgorithm algorithm)`
- `PrepareForRendering()`
- `SetPageIsVisible(bool visible)`
- `SetShouldMaintainAspectRatio(bool maintainAspectRatio)`
- `AcceleratedRenderingStateChanged(bool canBeAccelerated)`
- `SetShouldDisableSleep(bool disable)`
- `SetRate(double rate)`
- `DidLoadingProgress() -> (bool flag)`
- `UpdateVideoFullscreenInlineImage()` (if ENABLE(VIDEO_PRESENTATION_MODE))
- `SetVideoFullscreenMode(WebCore::MediaPlayer::VideoFullscreenMode mode)` (if ENABLE(VIDEO_PRESENTATION_MODE))
- `SetVideoFullscreenGravity(WebCore::MediaPlayerVideoGravity gravity)` (if ENABLE(VIDEO_PRESENTATION_MODE))
- `VideoFullscreenStandbyChanged(bool standby)` (if ENABLE(VIDEO_PRESENTATION_MODE))
- `SetBufferingPolicy(WebCore::MediaPlayerBufferingPolicy policy)`
- `SetPresentationSize(WebCore::IntSize size)`
- `SetVideoLayerSizeFenced(WebCore::FloatSize size, MachSendRight machSendRight)` (if PLATFORM(COCOA))
- `SetWirelessVideoPlaybackDisabled(bool disabled)` (if ENABLE(WIRELESS_PLAYBACK_TARGET))
- `SetWirelessPlaybackTarget(WebKit::MediaPlaybackTargetContextSerialized target)` (if ENABLE(WIRELESS_PLAYBACK_TARGET))
- `SetShouldPlayToPlaybackTarget(bool shouldPlay)` (if ENABLE(WIRELESS_PLAYBACK_TARGET))
- `SetLegacyCDMSession(std::optional<WebKit::RemoteLegacyCDMSessionIdentifier> instanceId)` (if ENABLE(LEGACY_ENCRYPTED_MEDIA))
- `KeyAdded()` (if ENABLE(LEGACY_ENCRYPTED_MEDIA))
- `CdmInstanceAttached(WebKit::RemoteCDMInstanceIdentifier instanceId)` (if ENABLE(ENCRYPTED_MEDIA))
- `CdmInstanceDetached(WebKit::RemoteCDMInstanceIdentifier instanceId)` (if ENABLE(ENCRYPTED_MEDIA))
- `AttemptToDecryptWithInstance(WebKit::RemoteCDMInstanceIdentifier instanceId)` (if ENABLE(ENCRYPTED_MEDIA))
- `SetShouldContinueAfterKeyNeeded(bool should)` (if ENABLE(LEGACY_ENCRYPTED_MEDIA) && ENABLE(ENCRYPTED_MEDIA))
- `BeginSimulatedHDCPError()`
- `EndSimulatedHDCPError()`
- `NotifyActiveSourceBuffersChanged()`
- `ApplicationWillResignActive()`
- `ApplicationDidBecomeActive()`
- `NotifyTrackModeChanged()`
- `TracksChanged()`
- `AudioTrackSetEnabled(WebCore::TrackID trackId, bool enabled)`
- `VideoTrackSetSelected(WebCore::TrackID trackId, bool selected)`
- `TextTrackSetMode(WebCore::TrackID trackId, WebCore::InbandTextTrackPrivateMode mode)`
- `PerformTaskAtTime(MediaTime mediaTime) -> (std::optional<MediaTime> mediaTime)`
- `IsCrossOrigin(WebCore::SecurityOriginData origin) -> (std::optional<bool> crossOrigin)` (sync)
- `SetVideoPlaybackMetricsUpdateInterval(double interval)`
- `SetPreferredDynamicRangeMode(WebCore::DynamicRangeMode mode)`
- `ErrorLog() -> (String errorLog)` (sync, if PLATFORM(IOS_FAMILY))
- `AccessLog() -> (String accessLog)` (sync, if PLATFORM(IOS_FAMILY))
- `CreateAudioSourceProvider()` (if ENABLE(WEB_AUDIO))
- `SetShouldEnableAudioSourceProvider(bool shouldEnable)` (if ENABLE(WEB_AUDIO))
- `NativeImageForCurrentTime() -> (std::optional<MachSendRight> sendRight, WebCore::DestinationColorSpace colorSpace)` (sync, if PLATFORM(COCOA))
- `ColorSpace() -> (WebCore::DestinationColorSpace colorSpace)` (sync, if PLATFORM(COCOA))
- `VideoFrameForCurrentTimeIfChanged() -> (std::optional<WebKit::RemoteVideoFrameProxyProperties> videoFrame, bool changed)` (sync)
- `PlayAtHostTime(MonotonicTime time)`
- `PauseAtHostTime(MonotonicTime time)`
- `StartVideoFrameMetadataGathering()`
- `StopVideoFrameMetadataGathering()`
- `PlayerContentBoxRectChanged(WebCore::LayoutRect contentRect)`
- `SetShouldDisableHDR(bool shouldDisable)`
- `RequestHostingContextID() -> (uint32_t contextID)`
- `SetShouldCheckHardwareSupport(bool value)`
- `SetDefaultSpatialTrackingLabel(String defaultSpatialTrackingLabel)` (if HAVE(SPATIAL_TRACKING_LABEL))
- `SetSpatialTrackingLabel(String spatialTrackingLabel)` (if HAVE(SPATIAL_TRACKING_LABEL))
- `AudioOutputDeviceChanged(String deviceId)`
- `IsInFullscreenOrPictureInPictureChanged(bool value)`

## `RemoteMediaRecorderPrivateWriterManager` - WebContent -> GPU

`GPUProcess/media/RemoteMediaRecorderPrivateWriterManager.messages.in`

- `Create(WebKit::RemoteMediaRecorderPrivateWriterIdentifier identifier)`
- `AddAudioTrack(WebKit::RemoteMediaRecorderPrivateWriterIdentifier identifier, WebKit::RemoteAudioInfo trackInfo) -> (std::optional<uint8_t> trackNumber)` (sync)
- `AddVideoTrack(WebKit::RemoteMediaRecorderPrivateWriterIdentifier identifier, WebKit::RemoteVideoInfo trackInfo, std::optional<CGAffineTransform> transform) -> (std::optional<uint8_t> trackNumber)` (sync)
- `AllTracksAdded(WebKit::RemoteMediaRecorderPrivateWriterIdentifier identifier) -> (bool success)` (sync)
- `WriteFrames(WebKit::RemoteMediaRecorderPrivateWriterIdentifier identifier, Vector<std::pair<WebCore::TrackInfo::TrackType, Vector<WebCore::MediaSamplesBlock::MediaSampleItem>>> frames, MediaTime endTime) -> (Expected<Ref<WebCore::SharedBuffer>, WebCore::MediaRecorderPrivateWriter::Result> data)`
- `Close(WebKit::RemoteMediaRecorderPrivateWriterIdentifier identifier) -> (RefPtr<WebCore::SharedBuffer> data)`

## `RemoteMediaResourceManager` - WebContent -> GPU

`GPUProcess/media/RemoteMediaResourceManager.messages.in`

- `ResponseReceived(WebKit::RemoteMediaResourceIdentifier identifier, WebCore::ResourceResponse response, bool didPassAccessControlCheck) -> (WebCore::ShouldContinuePolicyCheck shouldContinue)`
- `RedirectReceived(WebKit::RemoteMediaResourceIdentifier identifier, WebCore::ResourceRequest request, WebCore::ResourceResponse response) -> (WebCore::ResourceRequest returnRequest)`
- `DataSent(WebKit::RemoteMediaResourceIdentifier identifier, uint64_t bytesSent, uint64_t totalBytesToBeSent)`
- `DataReceived(WebKit::RemoteMediaResourceIdentifier identifier, IPC::SharedBufferReference data) -> (std::optional<WebCore::SharedMemory::Handle> remoteData)`
- `AccessControlCheckFailed(WebKit::RemoteMediaResourceIdentifier identifier, WebCore::ResourceError error)`
- `LoadFailed(WebKit::RemoteMediaResourceIdentifier identifier, WebCore::ResourceError error)`
- `LoadFinished(WebKit::RemoteMediaResourceIdentifier identifier, WebCore::NetworkLoadMetrics metrics)`

## `RemoteMediaSessionHelperProxy` - WebContent -> GPU

`GPUProcess/media/ios/RemoteMediaSessionHelperProxy.messages.in`

- `StartMonitoringWirelessRoutes()`
- `StopMonitoringWirelessRoutes()`
- `ProvidePresentingApplicationPID(int pid, WebCore::MediaSessionHelper::ShouldOverride shouldOverride)`

## `RemoteMediaSourceProxy` - WebContent -> GPU

`GPUProcess/media/RemoteMediaSourceProxy.messages.in`

- `AddSourceBuffer(WebCore::ContentType contentType) -> (WebCore::MediaSourcePrivateAddStatus status, std::optional<WebKit::RemoteSourceBufferIdentifier> remoteSourceBufferIdentifier)` (sync)
- `DurationChanged(MediaTime duration)`
- `BufferedChanged(WebCore::PlatformTimeRanges buffered)`
- `SetMediaPlayerReadyState(WebCore::MediaPlayerReadyState readyState)`
- `SetTimeFudgeFactor(MediaTime fudgeFactor)`
- `MarkEndOfStream(WebCore::MediaSourcePrivateEndOfStreamStatus status)`
- `UnmarkEndOfStream()`
- `Shutdown()`

## `RemotePipelineLayout` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemotePipelineLayout.messages.in`

- `Destruct()`
- `SetLabel(String label)`

## `RemotePresentationContext` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemotePresentationContext.messages.in`

- `Configure(WebKit::WebGPU::CanvasConfiguration configuration)`
- `Unconfigure()`
- `GetCurrentTexture(WebKit::WebGPUIdentifier identifier, uint32_t frameIndex)`
- `Present(uint32_t frameIndex)`

## `RemoteQuerySet` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteQuerySet.messages.in`

- `Destroy()`
- `Destruct()`
- `SetLabel(String label)`

## `RemoteQueue` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteQueue.messages.in`

- `Destruct()`
- `Submit(Vector<WebKit::WebGPUIdentifier> commandBuffers)`
- `OnSubmittedWorkDone() -> ()`
- `WriteBuffer(WebKit::WebGPUIdentifier identifier, WebCore::WebGPU::Size64 bufferOffset, std::optional<WebCore::SharedMemory::Handle> data) -> (bool success)` (NotStreamEncodable)
- `WriteTexture(WebKit::WebGPU::ImageCopyTexture destination, std::optional<WebCore::SharedMemory::Handle> dataHandle, WebKit::WebGPU::ImageDataLayout imageDataLayout, WebKit::WebGPU::Extent3D size) -> (bool success)` (NotStreamEncodable)
- `CopyExternalImageToTexture(WebKit::WebGPU::ImageCopyExternalImage source, WebKit::WebGPU::ImageCopyTextureTagged destination, WebKit::WebGPU::Extent3D copySize)`
- `SetLabel(String label)`

## `RemoteRemoteCommandListenerProxy` - WebContent -> GPU

`GPUProcess/media/RemoteRemoteCommandListenerProxy.messages.in`

- `UpdateSupportedCommands(Vector<WebCore::PlatformMediaSessionRemoteControlCommandType> commands, bool supportsSeeking)`

## `RemoteRenderBundle` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteRenderBundle.messages.in`

- `Destruct()`
- `SetLabel(String label)`

## `RemoteRenderBundleEncoder` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteRenderBundleEncoder.messages.in`

- `Destruct()`
- `SetPipeline(WebKit::WebGPUIdentifier identifier)`
- `SetIndexBuffer(WebKit::WebGPUIdentifier identifier, WebCore::WebGPU::IndexFormat indexFormat, std::optional<WebCore::WebGPU::Size64> offset, std::optional<WebCore::WebGPU::Size64> size)`
- `SetVertexBuffer(WebCore::WebGPU::Index32 slot, WebKit::WebGPUIdentifier identifier, std::optional<WebCore::WebGPU::Size64> offset, std::optional<WebCore::WebGPU::Size64> size)`
- `UnsetVertexBuffer(WebCore::WebGPU::Index32 slot, std::optional<WebCore::WebGPU::Size64> offset, std::optional<WebCore::WebGPU::Size64> size)`
- `Draw(WebCore::WebGPU::Size32 vertexCount, std::optional<WebCore::WebGPU::Size32> instanceCount, std::optional<WebCore::WebGPU::Size32> firstVertex, std::optional<WebCore::WebGPU::Size32> firstInstance)`
- `DrawIndexed(WebCore::WebGPU::Size32 indexCount, std::optional<WebCore::WebGPU::Size32> instanceCount, std::optional<WebCore::WebGPU::Size32> firstIndex, std::optional<WebCore::WebGPU::SignedOffset32> baseVertex, std::optional<WebCore::WebGPU::Size32> firstInstance)`
- `DrawIndirect(WebKit::WebGPUIdentifier indirectBuffer, WebCore::WebGPU::Size64 indirectOffset)`
- `DrawIndexedIndirect(WebKit::WebGPUIdentifier indirectBuffer, WebCore::WebGPU::Size64 indirectOffset)`
- `SetBindGroup(WebCore::WebGPU::Index32 index, WebKit::WebGPUIdentifier identifier, std::optional<Vector<WebCore::WebGPU::BufferDynamicOffset>> dynamicOffsets)`
- `PushDebugGroup(String groupLabel)`
- `PopDebugGroup()`
- `InsertDebugMarker(String markerLabel)`
- `Finish(WebKit::WebGPU::RenderBundleDescriptor descriptor, WebKit::WebGPUIdentifier identifier)`
- `SetLabel(String label)`

## `RemoteRenderPassEncoder` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteRenderPassEncoder.messages.in`

- `Destruct()`
- `SetPipeline(WebKit::WebGPUIdentifier identifier)`
- `SetIndexBuffer(WebKit::WebGPUIdentifier identifier, WebCore::WebGPU::IndexFormat indexFormat, std::optional<WebCore::WebGPU::Size64> offset, std::optional<WebCore::WebGPU::Size64> size)`
- `SetVertexBuffer(WebCore::WebGPU::Index32 slot, WebKit::WebGPUIdentifier identifier, std::optional<WebCore::WebGPU::Size64> offset, std::optional<WebCore::WebGPU::Size64> size)`
- `UnsetVertexBuffer(WebCore::WebGPU::Index32 slot, std::optional<WebCore::WebGPU::Size64> offset, std::optional<WebCore::WebGPU::Size64> size)`
- `Draw(WebCore::WebGPU::Size32 vertexCount, std::optional<WebCore::WebGPU::Size32> instanceCount, std::optional<WebCore::WebGPU::Size32> firstVertex, std::optional<WebCore::WebGPU::Size32> firstInstance)`
- `DrawIndexed(WebCore::WebGPU::Size32 indexCount, std::optional<WebCore::WebGPU::Size32> instanceCount, std::optional<WebCore::WebGPU::Size32> firstIndex, std::optional<WebCore::WebGPU::SignedOffset32> baseVertex, std::optional<WebCore::WebGPU::Size32> firstInstance)`
- `DrawIndirect(WebKit::WebGPUIdentifier indirectBuffer, WebCore::WebGPU::Size64 indirectOffset)`
- `DrawIndexedIndirect(WebKit::WebGPUIdentifier indirectBuffer, WebCore::WebGPU::Size64 indirectOffset)`
- `SetBindGroup(WebCore::WebGPU::Index32 index, WebKit::WebGPUIdentifier identifier, std::optional<Vector<WebCore::WebGPU::BufferDynamicOffset>> dynamicOffsets)`
- `PushDebugGroup(String groupLabel)`
- `PopDebugGroup()`
- `InsertDebugMarker(String markerLabel)`
- `SetViewport(float x, float y, float width, float height, float minDepth, float maxDepth)`
- `SetScissorRect(WebCore::WebGPU::IntegerCoordinate x, WebCore::WebGPU::IntegerCoordinate y, WebCore::WebGPU::IntegerCoordinate width, WebCore::WebGPU::IntegerCoordinate height)`
- `SetBlendConstant(WebKit::WebGPU::Color color)`
- `SetStencilReference(WebCore::WebGPU::StencilValue stencilValue)`
- `BeginOcclusionQuery(WebCore::WebGPU::Size32 queryIndex)`
- `EndOcclusionQuery()`
- `ExecuteBundles(Vector<WebKit::WebGPUIdentifier> bundles)`
- `End()`
- `SetLabel(String label)`

## `RemoteRenderPipeline` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteRenderPipeline.messages.in`

- `Destruct()`
- `GetBindGroupLayout(uint32_t index, WebKit::WebGPUIdentifier identifier)`
- `SetLabel(String label)`

## `RemoteRenderingBackend` - WebContent -> GPU

`GPUProcess/graphics/RemoteRenderingBackend.messages.in`

- `CreateImageBuffer(WebCore::FloatSize logicalSize, WebCore::RenderingMode renderingMode, WebCore::RenderingPurpose renderingPurpose, float resolutionScale, WebCore::DestinationColorSpace colorSpace, WebCore::ImageBufferPixelFormat pixelFormat, WebCore::RenderingResourceIdentifier renderingResourceIdentifier)`
- `ReleaseImageBuffer(WebCore::RenderingResourceIdentifier renderingResourceIdentifier)`
- `GetImageBufferResourceLimitsForTesting() -> (WebCore::ImageBufferResourceLimits limits)` (Async)
- `DestroyGetPixelBufferSharedMemory()`
- `CacheNativeImage(WebCore::ShareableBitmapHandle handle, WebCore::RenderingResourceIdentifier renderingResourceIdentifier)` (NotStreamEncodable)
- `CacheFont(WebCore::FontInternalAttributes data, WebCore::FontPlatformDataAttributes platformData, std::optional<WebCore::RenderingResourceIdentifier> renderingResourceIdentifier)` (NotStreamEncodable)
- `CacheFontCustomPlatformData(WebCore::FontCustomPlatformSerializedData fontCustomPlatformData)` (NotStreamEncodable)
- `CacheDecomposedGlyphs(Ref<WebCore::DecomposedGlyphs> decomposedGlyphs)`
- `CacheGradient(Ref<WebCore::Gradient> gradient)` (NotStreamEncodable)
- `CacheFilter(Ref<WebCore::Filter> filter)` (NotStreamEncodable)
- `ReleaseAllDrawingResources()`
- `ReleaseAllImageResources()`
- `ReleaseRenderingResource(WebCore::RenderingResourceIdentifier renderingResourceIdentifier)`
- `CreateRemoteImageBufferSet(WebKit::RemoteImageBufferSetIdentifier bufferSetIdentifier, WebCore::RenderingResourceIdentifier displayListIdentifier)`
- `ReleaseRemoteImageBufferSet(WebKit::RemoteImageBufferSetIdentifier bufferSetIdentifier)`
- `PrepareImageBufferSetsForDisplay(Vector<WebKit::ImageBufferSetPrepareBufferForDisplayInputData> swapBuffersInput)` (if PLATFORM(COCOA))
- `PrepareImageBufferSetsForDisplaySync(Vector<WebKit::ImageBufferSetPrepareBufferForDisplayInputData> swapBuffersInput) -> (Vector<WebKit::SwapBuffersDisplayRequirement> displayRequirements)` (sync, if PLATFORM(COCOA))
- `MarkSurfacesVolatile(WebKit::MarkSurfacesAsVolatileRequestIdentifier requestIdentifier, Vector<std::pair<WebKit::RemoteImageBufferSetIdentifier, OptionSet<WebKit::BufferInSetType>>> renderingResourceIdentifiers, bool forcePurge)`
- `FinalizeRenderingUpdate(WebKit::RenderingUpdateID renderingUpdateID)`
- `Flush(IPC::Semaphore semaphore)` (NotStreamEncodable, if USE(GRAPHICS_LAYER_WC))
- `MoveToSerializedBuffer(WebCore::RenderingResourceIdentifier sourceImageBuffer)`
- `MoveToImageBuffer(WebCore::RenderingResourceIdentifier destinationImageBuffer)`
- `DidDrawRemoteToPDF(WebCore::PageIdentifier pageID, WebCore::RenderingResourceIdentifier imageBufferIdentifier, WebCore::SnapshotIdentifier snapshotIdentifier)` (if PLATFORM(COCOA))
- `CreateRemoteBarcodeDetector(WebKit::ShapeDetectionIdentifier identifier, WebCore::ShapeDetection::BarcodeDetectorOptions barcodeDetectorOptions)` (AllowedWhenWaitingForSyncReply)
- `ReleaseRemoteBarcodeDetector(WebKit::ShapeDetectionIdentifier identifier)` (AllowedWhenWaitingForSyncReply)
- `GetRemoteBarcodeDetectorSupportedFormats() -> (Vector<WebCore::ShapeDetection::BarcodeFormat> formats)` (Async)
- `CreateRemoteFaceDetector(WebKit::ShapeDetectionIdentifier identifier, WebCore::ShapeDetection::FaceDetectorOptions faceDetectorOptions)` (AllowedWhenWaitingForSyncReply)
- `ReleaseRemoteFaceDetector(WebKit::ShapeDetectionIdentifier identifier)` (AllowedWhenWaitingForSyncReply)
- `CreateRemoteTextDetector(WebKit::ShapeDetectionIdentifier identifier)` (AllowedWhenWaitingForSyncReply)
- `ReleaseRemoteTextDetector(WebKit::ShapeDetectionIdentifier identifier)` (AllowedWhenWaitingForSyncReply)

## `RemoteSampleBufferDisplayLayer` - WebContent -> GPU

`GPUProcess/webrtc/RemoteSampleBufferDisplayLayer.messages.in`

- `SetLogIdentifier(String logIdentifier)` (if !RELEASE_LOG_DISABLED)
- `UpdateDisplayMode(bool hideDisplayLayer, bool hideRootLayer)`
- `Flush()`
- `FlushAndRemoveImage()`
- `EnqueueVideoFrame(WebKit::SharedVideoFrame frame)`
- `ClearVideoFrames()`
- `Play()`
- `Pause()`
- `SetSharedVideoFrameSemaphore(IPC::Semaphore semaphore)`
- `SetSharedVideoFrameMemory(WebCore::SharedMemory::Handle storageHandle)`
- `SetShouldMaintainAspectRatio(bool shouldMaintainAspectRatio)`

## `RemoteSampleBufferDisplayLayerManager` - WebContent -> GPU

`GPUProcess/webrtc/RemoteSampleBufferDisplayLayerManager.messages.in`

- `CreateLayer(WebKit::SampleBufferDisplayLayerIdentifier id, bool hideRootLayer, WebCore::IntSize size, bool shouldMaintainAspectRatio, bool canShowWhileLocked) -> (std::optional<WebKit::LayerHostingContextID> contextID)`
- `ReleaseLayer(WebKit::SampleBufferDisplayLayerIdentifier id)`

## `RemoteSampler` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteSampler.messages.in`

- `Destruct()`
- `SetLabel(String label)`

## `RemoteShaderModule` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteShaderModule.messages.in`

- `CompilationInfo() -> (Vector<WebKit::WebGPU::CompilationMessage> messages)`
- `SetLabel(String label)`
- `Destruct()`

## `RemoteSharedResourceCache` - WebContent -> GPU

`GPUProcess/RemoteSharedResourceCache.messages.in`

- `ReleaseSerializedImageBuffer(WebCore::RenderingResourceIdentifier imageBuffer)`

## `RemoteSourceBufferProxy` - WebContent -> GPU

`GPUProcess/media/RemoteSourceBufferProxy.messages.in`

- `SetActive(bool active)`
- `CanSwitchToType(WebCore::ContentType contentType) -> (bool canSwitch)` (sync)
- `SetMode(WebCore::SourceBufferAppendMode appendMode)`
- `Append(IPC::SharedBufferReference data) -> (Expected<void, WebCore::PlatformMediaError> result, MediaTime timestampOffset)`
- `Abort()`
- `ResetParserState()`
- `RemovedFromMediaSource()`
- `SetMediaSourceEnded(bool isEnded)`
- `StartChangingType()`
- `AddTrackBuffer(WebCore::TrackID trackID)`
- `ResetTrackBuffers()`
- `ClearTrackBuffers()`
- `SetAllTrackBuffersNeedRandomAccess()`
- `RemoveCodedFrames(MediaTime start, MediaTime end, MediaTime currentTime) -> ()`
- `EvictCodedFrames(uint64_t newDataSize, MediaTime currentTime) -> (Vector<WebCore::PlatformTimeRanges> trackBuffers, WebCore::SourceBufferEvictionData evictionData)` (sync)
- `AsyncEvictCodedFrames(uint64_t newDataSize, MediaTime currentTime)`
- `ReenqueueMediaIfNeeded(MediaTime currentMediaTime)`
- `SetGroupStartTimestamp(MediaTime timestamp)`
- `SetGroupStartTimestampToEndTimestamp()`
- `SetShouldGenerateTimestamps(bool shouldGenerateTimestamps)`
- `ResetTimestampOffsetInTrackBuffers()`
- `SetTimestampOffset(MediaTime timestampOffset)`
- `SetAppendWindowStart(MediaTime appendWindowStart)`
- `SetAppendWindowEnd(MediaTime appendWindowEnd)`
- `SetMaximumBufferSize(size_t size) -> ()`
- `ComputeSeekTime(WebCore::SeekTarget target) -> (Expected<MediaTime, WebCore::PlatformMediaError> seekedTime)`
- `SeekToTime(MediaTime time)`
- `UpdateTrackIds(Vector<std::pair<WebCore::TrackID, WebCore::TrackID>> identifierPairs)`
- `BufferedSamplesForTrackId(WebCore::TrackID trackID) -> (WebCore::SourceBufferPrivate::SamplesPromise::Result samples)`
- `EnqueuedSamplesForTrackID(WebCore::TrackID trackID) -> (WebCore::SourceBufferPrivate::SamplesPromise::Result samples)`
- `MemoryPressure(MediaTime currentTime)`
- `Detach()`
- `Attach()`
- `SetMaximumQueueDepthForTrackID(WebCore::TrackID trackID, uint64_t depth)`
- `MinimumUpcomingPresentationTimeForTrackID(WebCore::TrackID trackID) -> (MediaTime time)` (sync)

## `RemoteTextDetector` - WebContent -> GPU

`GPUProcess/ShapeDetection/RemoteTextDetector.messages.in`

- `Detect(WebCore::RenderingResourceIdentifier renderingResourceIdentifier) -> (Vector<WebCore::ShapeDetection::DetectedText> detectedText)`

## `RemoteTexture` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteTexture.messages.in`

- `CreateView(std::optional<WebKit::WebGPU::TextureViewDescriptor> descriptor, WebKit::WebGPUIdentifier identifier)`
- `Destroy()`
- `Undestroy()`
- `Destruct()`
- `SetLabel(String label)`

## `RemoteTextureView` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteTextureView.messages.in`

- `Destruct()`
- `SetLabel(String label)`

## `RemoteVideoFrameObjectHeap` - WebContent -> GPU

`GPUProcess/media/RemoteVideoFrameObjectHeap.messages.in`

- `GetVideoFrameBuffer(WebKit::RemoteVideoFrameReadReference read, bool canSendIOSurface)` (AllowedWhenWaitingForSyncReply, if PLATFORM(COCOA))
- `PixelBuffer(WebKit::RemoteVideoFrameReadReference read) -> (RetainPtr<CVPixelBufferRef> result)` (sync, if PLATFORM(COCOA))
- `SetSharedVideoFrameSemaphore(IPC::Semaphore semaphore)` (if PLATFORM(COCOA))
- `SetSharedVideoFrameMemory(WebCore::SharedMemory::Handle storageHandle)` (if PLATFORM(COCOA))
- `ConvertFrameBuffer(WebKit::SharedVideoFrame frame) -> (WebCore::DestinationColorSpace space)` (sync, if PLATFORM(COCOA))
- `ReleaseVideoFrame(WebKit::RemoteVideoFrameWriteReference write)` (AllowedWhenWaitingForSyncReply)

## `RemoteWCLayerTreeHost` - WebContent -> GPU

`GPUProcess/graphics/wc/RemoteWCLayerTreeHost.messages.in`

- `Update(WebKit::WCUpdateInfo updateInfo) -> (std::optional<WebKit::UpdateInfo> updateInfo)`

## `RemoteXRBinding` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteXRBinding.messages.in`

- `Destruct()`
- `CreateProjectionLayer(WebCore::WebGPU::TextureFormat colorFormat, std::optional<WebCore::WebGPU::TextureFormat> depthStencilFormat, WebCore::WebGPU::TextureUsageFlags textureUsage, double scaleFactor, WebKit::WebGPUIdentifier identifier)`
- `GetViewSubImage(WebKit::WebGPUIdentifier projectionLayerIdentifier, WebKit::WebGPUIdentifier identifier)`

## `RemoteXRProjectionLayer` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteXRProjectionLayer.messages.in`

- `StartFrame(size_t frameIndex, MachSendRight colorBuffer, MachSendRight depthBuffer, MachSendRight completionSyncEvent, size_t textureIndex)` (NotStreamEncodable, if PLATFORM(COCOA))
- `EndFrame()`
- `Destruct()`

## `RemoteXRSubImage` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteXRSubImage.messages.in`

- `Destruct()`
- `GetColorTexture(WebKit::WebGPUIdentifier identifier)`
- `GetDepthTexture(WebKit::WebGPUIdentifier identifier)`

## `RemoteXRView` - WebContent -> GPU

`GPUProcess/graphics/WebGPU/RemoteXRView.messages.in`

- `Destruct()`

## `UserMediaCaptureManagerProxy` - WebContent -> GPU

`UIProcess/Cocoa/UserMediaCaptureManagerProxy.messages.in`

- `CreateMediaSourceForCaptureDeviceWithConstraints(WebCore::RealtimeMediaSourceIdentifier id, WebCore::CaptureDevice device, WebCore::MediaDeviceHashSalts hashSalts, WebCore::MediaConstraints constraints, bool shouldUseGPUProcessRemoteFrames, WebCore::PageIdentifier pageIdentifier) -> (WebCore::CaptureSourceError error, WebCore::RealtimeMediaSourceSettings settings, WebCore::RealtimeMediaSourceCapabilities capabilities)` (Async)
- `StartProducingData(WebCore::RealtimeMediaSourceIdentifier id, WebCore::PageIdentifier pageIdentifier)`
- `StopProducingData(WebCore::RealtimeMediaSourceIdentifier id)`
- `RemoveSource(WebCore::RealtimeMediaSourceIdentifier id)`
- `ApplyConstraints(WebCore::RealtimeMediaSourceIdentifier id, WebCore::MediaConstraints constraints)`
- `TakePhoto(WebCore::RealtimeMediaSourceIdentifier sourceID, WebCore::PhotoSettings settings) -> (Expected<std::pair<Vector<uint8_t>, String>, String> result)`
- `GetPhotoCapabilities(WebCore::RealtimeMediaSourceIdentifier sourceID) -> (Expected<WebCore::PhotoCapabilities, String> result)` (Async)
- `GetPhotoSettings(WebCore::RealtimeMediaSourceIdentifier sourceID) -> (Expected<WebCore::PhotoSettings, String> result)` (Async)
- `Clone(WebCore::RealtimeMediaSourceIdentifier clonedID, WebCore::RealtimeMediaSourceIdentifier cloneID, WebCore::PageIdentifier pageIdentifier)`
- `EndProducingData(WebCore::RealtimeMediaSourceIdentifier sourceID)`
- `SetShouldApplyRotation(WebCore::RealtimeMediaSourceIdentifier sourceID, bool shouldApplyRotation)`
- `SetIsInBackground(WebCore::RealtimeMediaSourceIdentifier sourceID, bool isInBackground)`
- `IsPowerEfficient(WebCore::RealtimeMediaSourceIdentifier sourceID) -> (bool isPowerEfficient)` (sync)

## `NetworkBroadcastChannelRegistry` - WebContent -> Networking

`NetworkProcess/NetworkBroadcastChannelRegistry.messages.in`

- `RegisterChannel(WebCore::ClientOrigin origin, String name)`
- `UnregisterChannel(WebCore::ClientOrigin origin, String name)`
- `PostMessage(WebCore::ClientOrigin origin, String name, WebCore::MessageWithMessagePorts message) -> ()`

## `NetworkConnectionToWebProcess` - WebContent -> Networking

`NetworkProcess/NetworkConnectionToWebProcess.messages.in`

- `ScheduleResourceLoad(WebKit::NetworkResourceLoadParameters resourceLoadParameters, std::optional<WebKit::NetworkResourceLoadIdentifier> existingLoaderToResume)`
- `PerformSynchronousLoad(WebKit::NetworkResourceLoadParameters resourceLoadParameters) -> (WebCore::ResourceError error, WebCore::ResourceResponse response, Vector<uint8_t> data)` (sync)
- `TestProcessIncomingSyncMessagesWhenWaitingForSyncReply(WebKit::WebPageProxyIdentifier pageID) -> (bool handled)` (sync)
- `LoadPing(WebKit::NetworkResourceLoadParameters resourceLoadParameters)`
- `RemoveLoadIdentifier(WebCore::ResourceLoaderIdentifier resourceLoadIdentifier)`
- `PageLoadCompleted(WebCore::PageIdentifier webPageID)`
- `BrowsingContextRemoved(WebKit::WebPageProxyIdentifier webPageProxyID, WebCore::PageIdentifier webPageID, WebCore::FrameIdentifier webFrameID)`
- `PrefetchDNS(String hostname)`
- `SendH2Ping(WebKit::NetworkResourceLoadParameters parameters) -> (Expected<Seconds, WebCore::ResourceError> result)`
- `PreconnectTo(std::optional<WebCore::ResourceLoaderIdentifier> preconnectionIdentifier, WebKit::NetworkResourceLoadParameters loadParameters)`
- `IsResourceLoadFinished(WebCore::ResourceLoaderIdentifier resourceLoadIdentifier) -> (bool isFinished)`
- `StartDownload(WebKit::DownloadID downloadID, WebCore::ResourceRequest request, std::optional<WebCore::SecurityOriginData> topOrigin, std::optional<WebKit::NavigatingToAppBoundDomain> isNavigatingToAppBoundDomain, String suggestedName, WebCore::FromDownloadAttribute fromDownloadAttribute, std::optional<WebCore::FrameIdentifier> frameID, std::optional<WebCore::PageIdentifier> pageID)`
- `ConvertMainResourceLoadToDownload(std::optional<WebCore::ResourceLoaderIdentifier> mainResourceLoadIdentifier, WebKit::DownloadID downloadID, WebCore::ResourceRequest request, std::optional<WebCore::SecurityOriginData> topOrigin, WebCore::ResourceResponse response, std::optional<WebKit::NavigatingToAppBoundDomain> isNavigatingToAppBoundDomain)`
- `CookiesForDOM(URL firstParty, WebCore::SameSiteInfo sameSiteInfo, URL url, WebCore::FrameIdentifier frameID, WebCore::PageIdentifier pageID, WebCore::IncludeSecureCookies includeSecureCookies, WebKit::WebPageProxyIdentifier webPageProxyID) -> (String cookieString, bool didAccessSecureCookies)` (sync)
- `SetCookiesFromDOM(URL firstParty, WebCore::SameSiteInfo sameSiteInfo, URL url, WebCore::FrameIdentifier frameID, WebCore::PageIdentifier pageID, String cookieString, WebKit::WebPageProxyIdentifier webPageProxyID)`
- `CookiesEnabledSync(URL firstParty, URL url, std::optional<WebCore::FrameIdentifier> frameID, std::optional<WebCore::PageIdentifier> pageID, WebKit::WebPageProxyIdentifier webPageProxyID) -> (bool enabled)` (sync)
- `CookiesEnabled(URL firstParty, URL url, std::optional<WebCore::FrameIdentifier> frameID, std::optional<WebCore::PageIdentifier> pageID, WebKit::WebPageProxyIdentifier webPageProxyID) -> (bool enabled)`
- `CookieRequestHeaderFieldValue(URL firstParty, WebCore::SameSiteInfo sameSiteInfo, URL url, std::optional<WebCore::FrameIdentifier> frameID, std::optional<WebCore::PageIdentifier> pageID, WebCore::IncludeSecureCookies includeSecureCookies, std::optional<WebKit::WebPageProxyIdentifier> webPageProxyID) -> (String cookieString, bool didAccessSecureCookies)` (sync)
- `SetRawCookie(URL firstParty, URL url, WebCore::Cookie cookie, WebCore::ShouldPartitionCookie shouldPartitionCookie)`
- `GetRawCookies(URL firstParty, WebCore::SameSiteInfo sameSiteInfo, URL url, std::optional<WebCore::FrameIdentifier> frameID, std::optional<WebCore::PageIdentifier> pageID, std::optional<WebKit::WebPageProxyIdentifier> webPageProxyID) -> (Vector<WebCore::Cookie> cookies)` (sync)
- `DeleteCookie(URL firstParty, URL url, String cookieName) -> ()`
- `DomCookiesForHost(URL host) -> (Vector<WebCore::Cookie> cookies)` (sync)
- `CookiesForDOMAsync(URL firstParty, WebCore::SameSiteInfo sameSiteInfo, URL url, std::optional<WebCore::FrameIdentifier> frameID, std::optional<WebCore::PageIdentifier> pageID, WebCore::IncludeSecureCookies includeSecureCookies, WebCore::CookieStoreGetOptions options, std::optional<WebKit::WebPageProxyIdentifier> webPageProxyID) -> (std::optional<Vector<WebCore::Cookie>> cookies)`
- `SetCookieFromDOMAsync(URL firstParty, WebCore::SameSiteInfo sameSiteInfo, URL url, std::optional<WebCore::FrameIdentifier> frameID, std::optional<WebCore::PageIdentifier> pageID, WebCore::Cookie cookie, std::optional<WebKit::WebPageProxyIdentifier> webPageProxyID) -> (bool setSuccessfully)`
- `SubscribeToCookieChangeNotifications(URL url, URL firstParty, WebCore::FrameIdentifier frameID, WebCore::PageIdentifier pageID, WebKit::WebPageProxyIdentifier webPageProxyID) -> (bool result)` (AllowedWhenWaitingForSyncReply, if HAVE(COOKIE_CHANGE_LISTENER_API))
- `UnsubscribeFromCookieChangeNotifications(String host)` (AllowedWhenWaitingForSyncReply, if HAVE(COOKIE_CHANGE_LISTENER_API))
- `RegisterInternalFileBlobURL(URL url, String path, String replacementPath, WebKit::SandboxExtensionHandle extensionHandle, String contentType)`
- `RegisterInternalBlobURL(URL url, Vector<WebCore::BlobPart> blobParts, String contentType)`
- `RegisterBlobURL(URL url, URL srcURL, WebCore::PolicyContainer policyContainer, std::optional<WebCore::SecurityOriginData> topOrigin)`
- `RegisterInternalBlobURLOptionallyFileBacked(URL url, URL srcURL, String fileBackedPath, String contentType)`
- `RegisterInternalBlobURLForSlice(URL url, URL srcURL, int64_t start, int64_t end, String contentType)`
- `UnregisterBlobURL(URL url, std::optional<WebCore::SecurityOriginData> topOrigin)`
- `BlobType(URL url) -> (String result)` (sync)
- `BlobSize(URL url) -> (uint64_t resultSize)` (sync)
- `WriteBlobsToTemporaryFilesForIndexedDB(Vector<String> blobURLs) -> (Vector<String> fileNames)`
- `RegisterBlobURLHandle(URL url, std::optional<WebCore::SecurityOriginData> topOrigin)`
- `UnregisterBlobURLHandle(URL url, std::optional<WebCore::SecurityOriginData> topOrigin)`
- `RegisterBlobPathForTesting(String path) -> ()`
- `SetCaptureExtraNetworkLoadMetricsEnabled(bool enabled)`
- `CreateSocketChannel(WebCore::ResourceRequest request, String protocol, WebCore::WebSocketIdentifier identifier, WebKit::WebPageProxyIdentifier webPageProxyID, std::optional<WebCore::FrameIdentifier> frameID, std::optional<WebCore::PageIdentifier> pageID, WebCore::ClientOrigin clientOrigin, bool hadMainFrameMainResourcePrivateRelayed, bool allowPrivacyProxy, OptionSet<WebCore::AdvancedPrivacyProtections> protections, WebCore::StoredCredentialsPolicy storedCredentialsPolicy)`
- `ClearPageSpecificData(WebCore::PageIdentifier pageID)`
- `RemoveStorageAccessForFrame(WebCore::FrameIdentifier frameID, WebCore::PageIdentifier pageID)`
- `LogUserInteraction(WebCore::RegistrableDomain domain)`
- `ResourceLoadStatisticsUpdated(Vector<WebCore::ResourceLoadStatistics> statistics) -> ()`
- `HasStorageAccess(WebCore::RegistrableDomain subFrameDomain, WebCore::RegistrableDomain topFrameDomain, WebCore::FrameIdentifier frameID, WebCore::PageIdentifier pageID) -> (bool hasStorageAccess)`
- `RequestStorageAccess(WebCore::RegistrableDomain subFrameDomain, WebCore::RegistrableDomain topFrameDomain, WebCore::FrameIdentifier frameID, WebCore::PageIdentifier webPageID, WebKit::WebPageProxyIdentifier webPageProxyID, WebCore::StorageAccessScope scope) -> (WebCore::RequestStorageAccessResult result)`
- `StorageAccessQuirkForTopFrameDomain(URL topFrameURL) -> (Vector<WebCore::RegistrableDomain> domains)`
- `RequestStorageAccessUnderOpener(WebCore::RegistrableDomain domainInNeedOfStorageAccess, WebCore::PageIdentifier openerPageID, WebCore::RegistrableDomain openerDomain)`
- `AddOriginAccessAllowListEntry(String sourceOrigin, String destinationProtocol, String destinationHost, bool allowDestinationSubdomains)`
- `RemoveOriginAccessAllowListEntry(String sourceOrigin, String destinationProtocol, String destinationHost, bool allowDestinationSubdomains)`
- `ResetOriginAccessAllowLists()`
- `GetNetworkLoadInformationResponse(WebCore::ResourceLoaderIdentifier resourceLoadIdentifier) -> (WebCore::ResourceResponse response)` (sync)
- `GetNetworkLoadIntermediateInformation(WebCore::ResourceLoaderIdentifier resourceLoadIdentifier) -> (Vector<WebCore::NetworkTransactionInformation> transactions)` (sync)
- `TakeNetworkLoadInformationMetrics(WebCore::ResourceLoaderIdentifier resourceLoadIdentifier) -> (WebCore::NetworkLoadMetrics networkMetrics)` (sync)
- `EstablishSWContextConnection(WebKit::WebPageProxyIdentifier webPageProxyID, WebCore::Site site, std::optional<WebCore::ScriptExecutionContextIdentifier> serviceWorkerPageIdentifier) -> ()`
- `CloseSWContextConnection()`
- `PingPongForServiceWorkers() -> (bool isSuccess)`
- `EstablishSharedWorkerContextConnection(WebKit::WebPageProxyIdentifier webPageProxyID, WebCore::Site site) -> ()`
- `CloseSharedWorkerContextConnection()`
- `CreateRTCProvider() -> ()`
- `ConnectToRTCDataChannelRemoteSource(WebCore::RTCDataChannelIdentifier source, WebCore::RTCDataChannelIdentifier handler) -> (std::optional<bool> result)` (if ENABLE(WEB_RTC))
- `CreateNewMessagePortChannel(WebCore::MessagePortIdentifier port1, WebCore::MessagePortIdentifier port2)`
- `EntangleLocalPortInThisProcessToRemote(WebCore::MessagePortIdentifier local, WebCore::MessagePortIdentifier remote)`
- `MessagePortDisentangled(WebCore::MessagePortIdentifier local)`
- `MessagePortClosed(WebCore::MessagePortIdentifier local)`
- `TakeAllMessagesForPort(WebCore::MessagePortIdentifier port) -> (Vector<WebCore::MessageWithMessagePorts> messages, std::optional<WebKit::MessageBatchIdentifier> messageBatchIdentifier)`
- `PostMessageToRemote(WebCore::MessageWithMessagePorts message, WebCore::MessagePortIdentifier remote)`
- `DidDeliverMessagePortMessages(WebKit::MessageBatchIdentifier messageBatchIdentifier)`
- `RegisterURLSchemesAsCORSEnabled(Vector<String> schemes)`
- `SetCORSDisablingPatterns(WebCore::PageIdentifier pageIdentifier, Vector<String> patterns)`
- `GetProcessDisplayName(WebKit::CoreIPCAuditToken auditToken) -> (String displayName)` (if PLATFORM(MAC))
- `UpdateActivePages(String name, Vector<String> activePagesOrigins, WebKit::CoreIPCAuditToken auditToken)` (if PLATFORM(MAC))
- `SetResourceLoadSchedulingMode(WebCore::PageIdentifier webPageID, WebCore::LoadSchedulingMode mode)`
- `PrioritizeResourceLoads(Vector<WebCore::ResourceLoaderIdentifier> loadIdentifiers)`
- `InstallMockContentFilter(WebCore::MockContentFilterSettings settings)` (if ENABLE(CONTENT_FILTERING))
- `UseRedirectionForCurrentNavigation(WebCore::ResourceLoaderIdentifier resourceLoadIdentifier, WebCore::ResourceResponse response)`
- `NavigatorSubscribeToPushService(URL scopeURL, Vector<uint8_t> applicationServerKey) -> (Expected<WebCore::PushSubscriptionData, WebCore::ExceptionData> result)` (if ENABLE(DECLARATIVE_WEB_PUSH))
- `NavigatorUnsubscribeFromPushService(URL scopeURL, WebCore::PushSubscriptionIdentifier pushSubscriptionIdentifier) -> (Expected<bool, WebCore::ExceptionData> result)` (if ENABLE(DECLARATIVE_WEB_PUSH))
- `NavigatorGetPushSubscription(URL scopeURL) -> (Expected<std::optional<WebCore::PushSubscriptionData>, WebCore::ExceptionData> result)` (if ENABLE(DECLARATIVE_WEB_PUSH))
- `NavigatorGetPushPermissionState(URL scopeURL) -> (Expected<uint8_t, WebCore::ExceptionData> result)` (if ENABLE(DECLARATIVE_WEB_PUSH))
- `InitializeWebTransportSession(URL url, WebKit::WebPageProxyIdentifier pageID, WebCore::ClientOrigin clientOrigin) -> (std::optional<WebKit::WebTransportSessionIdentifier> identifier)`
- `DestroyWebTransportSession(WebKit::WebTransportSessionIdentifier identifier)`
- `ClearFrameLoadRecordsForStorageAccess(WebCore::FrameIdentifier frameID)`
- `LoadImageForDecoding(WebCore::ResourceRequest request, WebKit::WebPageProxyIdentifier pageID, size_t maximumBytesFromNetwork) -> (std::variant<WebCore::ResourceError, Ref<WebCore::FragmentedSharedBuffer>> result)`
- `SetLoginStatus(WebCore::RegistrableDomain domain, WebCore::IsLoggedIn loggedInStatus, std::optional<WebCore::LoginStatus> lastAuthentication) -> ()`
- `IsLoggedIn(WebCore::RegistrableDomain domain) -> (bool result)`

## `NetworkMDNSRegister` - WebContent -> Networking

`NetworkProcess/webrtc/NetworkMDNSRegister.messages.in`

- `UnregisterMDNSNames(WebCore::ScriptExecutionContextIdentifier documentIdentifier)`
- `RegisterMDNSName(WebCore::ScriptExecutionContextIdentifier documentIdentifier, String ipAddress) -> (String mdnsName, std::optional<WebCore::MDNSRegisterError> error)`

## `NetworkRTCMonitor` - WebContent -> Networking

`NetworkProcess/webrtc/NetworkRTCMonitor.messages.in`

- `StartUpdatingIfNeeded()`
- `StopUpdating()`

## `NetworkRTCProvider` - WebContent -> Networking

`NetworkProcess/webrtc/NetworkRTCProvider.messages.in`

- `CreateUDPSocket(WebCore::LibWebRTCSocketIdentifier identifier, WebKit::RTC::Network::SocketAddress localAddress, uint16_t minPort, uint16_t maxPort, WebKit::WebPageProxyIdentifier pageIdentifier, bool isFirstParty, bool isRelayDisabled, WebCore::RegistrableDomain domain)`
- `CreateClientTCPSocket(WebCore::LibWebRTCSocketIdentifier identifier, WebKit::RTC::Network::SocketAddress localAddress, WebKit::RTC::Network::SocketAddress remoteAddress, String userAgent, int options, WebKit::WebPageProxyIdentifier pageIdentifier, bool isFirstParty, bool isRelayDisabled, WebCore::RegistrableDomain domain)`
- `CreateResolver(WebKit::LibWebRTCResolverIdentifier identifier, String address)`
- `StopResolver(WebKit::LibWebRTCResolverIdentifier identifier)`
- `GetInterfaceName(URL url, WebKit::WebPageProxyIdentifier pageIdentifier, bool isFirstParty, bool isRelayDisabled, WebCore::RegistrableDomain domain) -> (String interfaceName)` (async, if PLATFORM(COCOA))
- `SendToSocket(WebCore::LibWebRTCSocketIdentifier identifier, std::span<const uint8_t> data, WebKit::RTC::Network::SocketAddress address, WebKit::RTCPacketOptions options)`
- `CloseSocket(WebCore::LibWebRTCSocketIdentifier identifier)`
- `SetSocketOption(WebCore::LibWebRTCSocketIdentifier identifier, int option, int value)`

## `NetworkResourceLoader` - WebContent -> Networking

`NetworkProcess/NetworkResourceLoader.messages.in`

- `ContinueDidReceiveResponse()`

## `NetworkSocketChannel` - WebContent -> Networking

`NetworkProcess/NetworkSocketChannel.messages.in`

- `SendString(std::span<const uint8_t> message) -> ()`
- `SendData(std::span<const uint8_t> data) -> ()`
- `Close(int32_t code, String reason)`

## `NetworkStorageManager` - WebContent -> Networking

`NetworkProcess/storage/NetworkStorageManager.messages.in`

- `Persisted(WebCore::ClientOrigin origin) -> (bool persisted)`
- `Persist(WebCore::ClientOrigin origin) -> (bool persisted)`
- `Estimate(WebCore::ClientOrigin origin) -> (std::optional<WebCore::StorageEstimate> result)`
- `FileSystemGetDirectory(WebCore::ClientOrigin origin) -> (Expected<std::optional<WebCore::FileSystemHandleIdentifier>, WebKit::FileSystemStorageError> result)`
- `CloseHandle(WebCore::FileSystemHandleIdentifier identifier)`
- `IsSameEntry(WebCore::FileSystemHandleIdentifier identifier, WebCore::FileSystemHandleIdentifier targetIdentifier) -> (bool result)`
- `GetFileHandle(WebCore::FileSystemHandleIdentifier identifier, String name, bool createIfNecessary) -> (Expected<WebCore::FileSystemHandleIdentifier, WebKit::FileSystemStorageError> result)`
- `GetDirectoryHandle(WebCore::FileSystemHandleIdentifier identifier, String name, bool createIfNecessary) -> (Expected<WebCore::FileSystemHandleIdentifier, WebKit::FileSystemStorageError> result)`
- `RemoveEntry(WebCore::FileSystemHandleIdentifier identifier, String name, bool deleteRecursively) -> (std::optional<WebKit::FileSystemStorageError> result)`
- `Resolve(WebCore::FileSystemHandleIdentifier identifier, WebCore::FileSystemHandleIdentifier targetIdentifier) -> (Expected<Vector<String>, WebKit::FileSystemStorageError> result)`
- `Move(WebCore::FileSystemHandleIdentifier identifier, WebCore::FileSystemHandleIdentifier destinationIdentifier, String newName) -> (std::optional<WebKit::FileSystemStorageError> result)`
- `GetFile(WebCore::FileSystemHandleIdentifier identifier) -> (Expected<String, WebKit::FileSystemStorageError> result)`
- `CreateSyncAccessHandle(WebCore::FileSystemHandleIdentifier identifier) -> (Expected<WebKit::FileSystemSyncAccessHandleInfo, WebKit::FileSystemStorageError> result)`
- `CloseSyncAccessHandle(WebCore::FileSystemHandleIdentifier identifier, WebCore::FileSystemSyncAccessHandleIdentifier accessHandleIdentifier) -> ()`
- `RequestNewCapacityForSyncAccessHandle(WebCore::FileSystemHandleIdentifier identifier, WebCore::FileSystemSyncAccessHandleIdentifier accessHandleIdentifier, uint64_t newCapacity) -> (std::optional<uint64_t> result)`
- `CreateWritable(WebCore::FileSystemHandleIdentifier identifier, bool keepExistingData) -> (std::optional<WebKit::FileSystemStorageError> result)`
- `CloseWritable(WebCore::FileSystemHandleIdentifier identifier, WebCore::FileSystemWriteCloseReason reason) -> (std::optional<WebKit::FileSystemStorageError> result)`
- `ExecuteCommandForWritable(WebCore::FileSystemHandleIdentifier identifier, WebCore::FileSystemWriteCommandType type, std::optional<uint64_t> position, std::optional<uint64_t> size, std::span<const uint8_t> dataBytes, bool hasDataError) -> (std::optional<WebKit::FileSystemStorageError> result)`
- `GetHandleNames(WebCore::FileSystemHandleIdentifier identifier) -> (Expected<Vector<String>, WebKit::FileSystemStorageError> result)`
- `GetHandle(WebCore::FileSystemHandleIdentifier identifier, String name) -> (Expected<std::optional<std::pair<WebCore::FileSystemHandleIdentifier, bool>>, WebKit::FileSystemStorageError> result)`
- `ConnectToStorageArea(WebCore::StorageType type, WebKit::StorageAreaMapIdentifier sourceIdentifier, std::optional<WebKit::StorageNamespaceIdentifier> namespaceIdentifier, WebCore::ClientOrigin origin) -> (std::optional<WebKit::StorageAreaIdentifier> identifier, HashMap<String, String> items, uint64_t messageIdentifier)`
- `ConnectToStorageAreaSync(WebCore::StorageType type, WebKit::StorageAreaMapIdentifier sourceIdentifier, std::optional<WebKit::StorageNamespaceIdentifier> namespaceIdentifier, WebCore::ClientOrigin origin) -> (std::optional<WebKit::StorageAreaIdentifier> identifier, HashMap<String, String> items, uint64_t messageIdentifier)` (sync)
- `CancelConnectToStorageArea(WebCore::StorageType type, std::optional<WebKit::StorageNamespaceIdentifier> namespaceIdentifier, WebCore::ClientOrigin origin)`
- `DisconnectFromStorageArea(WebKit::StorageAreaIdentifier identifier)`
- `SetItem(WebKit::StorageAreaIdentifier identifier, WebKit::StorageAreaImplIdentifier implIdentifier, String key, String value, String urlString) -> (bool hasError, HashMap<String, String> allItems)`
- `RemoveItem(WebKit::StorageAreaIdentifier identifier, WebKit::StorageAreaImplIdentifier implIdentifier, String key, String urlString) -> (bool hasError, HashMap<String, String> allItems)`
- `Clear(WebKit::StorageAreaIdentifier identifier, WebKit::StorageAreaImplIdentifier implIdentifier, String urlString) -> ()`
- `OpenDatabase(WebCore::IDBOpenRequestData requestData)`
- `OpenDBRequestCancelled(WebCore::IDBOpenRequestData requestData)`
- `DeleteDatabase(WebCore::IDBOpenRequestData requestData)`
- `EstablishTransaction(WebCore::IDBDatabaseConnectionIdentifier databaseConnectionIdentifier, WebCore::IDBTransactionInfo info)`
- `DatabaseConnectionPendingClose(WebCore::IDBDatabaseConnectionIdentifier databaseConnectionIdentifier)`
- `DatabaseConnectionClosed(WebCore::IDBDatabaseConnectionIdentifier databaseConnectionIdentifier)`
- `AbortOpenAndUpgradeNeeded(WebCore::IDBDatabaseConnectionIdentifier databaseConnectionIdentifier, std::optional<WebCore::IDBResourceIdentifier> transactionIdentifier)`
- `DidFireVersionChangeEvent(WebCore::IDBDatabaseConnectionIdentifier databaseConnectionIdentifier, WebCore::IDBResourceIdentifier requestIdentifier, WebCore::IndexedDB::ConnectionClosedOnBehalfOfServer connectionClosedOnBehalfOfServer)`
- `DidFinishHandlingVersionChangeTransaction(WebCore::IDBDatabaseConnectionIdentifier databaseConnectionIdentifier, WebCore::IDBResourceIdentifier transactionIdentifier)`
- `AbortTransaction(WebCore::IDBResourceIdentifier transactionIdentifier)`
- `CommitTransaction(WebCore::IDBResourceIdentifier transactionIdentifier, uint64_t handledRequestResultsCount)`
- `CreateObjectStore(WebCore::IDBRequestData requestData, WebCore::IDBObjectStoreInfo info)`
- `DeleteObjectStore(WebCore::IDBRequestData requestData, String objectStoreName)`
- `RenameObjectStore(WebCore::IDBRequestData requestData, WebCore::IDBObjectStoreIdentifier objectStoreIdentifier, String newName)`
- `ClearObjectStore(WebCore::IDBRequestData requestData, WebCore::IDBObjectStoreIdentifier objectStoreIdentifier)`
- `CreateIndex(WebCore::IDBRequestData requestData, WebCore::IDBIndexInfo info)`
- `DeleteIndex(WebCore::IDBRequestData requestData, WebCore::IDBObjectStoreIdentifier objectStoreIdentifier, String indexName)`
- `RenameIndex(WebCore::IDBRequestData requestData, WebCore::IDBObjectStoreIdentifier objectStoreIdentifier, WebCore::IDBIndexIdentifier indexIdentifier, String newName)`
- `PutOrAdd(WebCore::IDBRequestData requestData, WebCore::IDBKeyData key, WebCore::IDBValue value, WebCore::IndexedDB::ObjectStoreOverwriteMode overwriteMode)`
- `GetRecord(WebCore::IDBRequestData requestData, WebCore::IDBGetRecordData getRecordData)`
- `GetAllRecords(WebCore::IDBRequestData requestData, WebCore::IDBGetAllRecordsData getAllRecordsData)`
- `GetCount(WebCore::IDBRequestData requestData, WebCore::IDBKeyRangeData range)`
- `DeleteRecord(WebCore::IDBRequestData requestData, WebCore::IDBKeyRangeData range)`
- `OpenCursor(WebCore::IDBRequestData requestData, WebCore::IDBCursorInfo info)`
- `IterateCursor(WebCore::IDBRequestData requestData, WebCore::IDBIterateCursorData data)`
- `GetAllDatabaseNamesAndVersions(WebCore::IDBResourceIdentifier requestIdentifier, WebCore::ClientOrigin origin)`
- `CacheStorageOpenCache(WebCore::ClientOrigin origin, String cacheName) -> (WebCore::DOMCacheEngine::CacheIdentifierOrError result)`
- `CacheStorageRemoveCache(WebCore::DOMCacheIdentifier cacheIdentifier) -> (WebCore::DOMCacheEngine::RemoveCacheIdentifierOrError result)`
- `CacheStorageAllCaches(WebCore::ClientOrigin origin, uint64_t updateCounter) -> (WebCore::DOMCacheEngine::CacheInfosOrError result)`
- `CacheStorageReference(WebCore::DOMCacheIdentifier cacheIdentifier)`
- `CacheStorageDereference(WebCore::DOMCacheIdentifier cacheIdentifier)`
- `LockCacheStorage(WebCore::ClientOrigin origin)`
- `UnlockCacheStorage(WebCore::ClientOrigin origin)`
- `CacheStorageRetrieveRecords(WebCore::DOMCacheIdentifier cacheIdentifier, WebCore::RetrieveRecordsOptions options) -> (WebCore::DOMCacheEngine::CrossThreadRecordsOrError result)`
- `CacheStorageRemoveRecords(WebCore::DOMCacheIdentifier cacheIdentifier, WebCore::ResourceRequest request, WebCore::CacheQueryOptions options) -> (WebCore::DOMCacheEngine::RecordIdentifiersOrError result)`
- `CacheStoragePutRecords(WebCore::DOMCacheIdentifier cacheIdentifier, Vector<WebCore::DOMCacheEngine::CrossThreadRecord> records) -> (WebCore::DOMCacheEngine::RecordIdentifiersOrError result)`
- `CacheStorageClearMemoryRepresentation(WebCore::ClientOrigin origin) -> ()`
- `CacheStorageRepresentation() -> (String representation)`
- `ResetQuotaUpdatedBasedOnUsageForTesting(WebCore::ClientOrigin origin)`

## `NetworkTransportSession` - WebContent -> Networking

`NetworkProcess/webtransport/NetworkTransportSession.messages.in`

- `SendDatagram(std::span<const uint8_t> datagram) -> (std::optional<WebCore::Exception> exception)`
- `CreateOutgoingUnidirectionalStream() -> (std::optional<WebCore::WebTransportStreamIdentifier> identifier)`
- `CreateBidirectionalStream() -> (std::optional<WebCore::WebTransportStreamIdentifier> identifier)`
- `StreamSendBytes(WebCore::WebTransportStreamIdentifier identifier, std::span<const uint8_t> bytes, bool withFin) -> (std::optional<WebCore::Exception> exception)`
- `CancelReceiveStream(WebCore::WebTransportStreamIdentifier identifier, std::optional<uint64_t> errorCode)`
- `CancelSendStream(WebCore::WebTransportStreamIdentifier identifier, std::optional<uint64_t> errorCode)`
- `DestroyStream(WebCore::WebTransportStreamIdentifier identifier, std::optional<uint64_t> errorCode)`
- `Terminate(uint32_t code, CString reason)`

## `RTCDataChannelRemoteManagerProxy` - WebContent -> Networking

`NetworkProcess/webrtc/RTCDataChannelRemoteManagerProxy.messages.in`

- `SendData(WebCore::RTCDataChannelIdentifier source, bool isRaw, std::span<const uint8_t> text)`
- `Close(WebCore::RTCDataChannelIdentifier source)`
- `ChangeReadyState(WebCore::RTCDataChannelIdentifier handler, WebCore::RTCDataChannelState state)`
- `ReceiveData(WebCore::RTCDataChannelIdentifier handler, bool isRaw, std::span<const uint8_t> data)`
- `DetectError(WebCore::RTCDataChannelIdentifier handler, WebCore::RTCErrorDetailType type, String message)`
- `BufferedAmountIsDecreasing(WebCore::RTCDataChannelIdentifier handler, size_t amount)`

## `ServiceWorkerDownloadTask` - WebContent -> Networking

`NetworkProcess/ServiceWorker/ServiceWorkerDownloadTask.messages.in`

- `DidFail(WebCore::ResourceError error)`
- `DidReceiveData(IPC::SharedBufferReference data, uint64_t encodedDataLength)`
- `DidReceiveFormData(IPC::FormDataReference data)`
- `DidFinish()`

## `ServiceWorkerFetchTask` - WebContent -> Networking

`NetworkProcess/ServiceWorker/ServiceWorkerFetchTask.messages.in`

- `DidNotHandle()`
- `DidFail(WebCore::ResourceError error)`
- `DidReceiveRedirectResponse(WebCore::ResourceResponse response)`
- `DidReceiveResponse(WebCore::ResourceResponse response, bool needsContinueDidReceiveResponseMessage)`
- `DidReceiveData(IPC::SharedBufferReference data, uint64_t encodedDataLength)`
- `DidReceiveFormData(IPC::FormDataReference data)`
- `DidFinish(WebCore::NetworkLoadMetrics metrics)`
- `UsePreload()`
- `WorkerClosed()`

## `WebSWServerConnection` - WebContent -> Networking

`NetworkProcess/ServiceWorker/WebSWServerConnection.messages.in`

- `ScheduleJobInServer(WebCore::ServiceWorkerJobData jobData)`
- `ScheduleUnregisterJobInServer(WebCore::ServiceWorkerJobIdentifier jobIdentifier, WebCore::ServiceWorkerRegistrationIdentifier identifier, WebCore::ServiceWorkerOrClientIdentifier documentIdentifier) -> (Expected<bool, WebCore::ExceptionData> result)`
- `FinishFetchingScriptInServer(WebCore::ServiceWorkerJobDataIdentifier jobDataIdentifier, WebCore::ServiceWorkerRegistrationKey registrationKey, WebCore::WorkerFetchResult result)`
- `AddServiceWorkerRegistrationInServer(WebCore::ServiceWorkerRegistrationIdentifier identifier)`
- `RemoveServiceWorkerRegistrationInServer(WebCore::ServiceWorkerRegistrationIdentifier identifier)`
- `PostMessageToServiceWorker(WebCore::ServiceWorkerIdentifier destination, WebCore::MessageWithMessagePorts message, WebCore::ServiceWorkerOrClientIdentifier source)`
- `DidResolveRegistrationPromise(WebCore::ServiceWorkerRegistrationKey key)`
- `MatchRegistration(WebCore::SecurityOriginData topOrigin, URL clientURL) -> (std::optional<WebCore::ServiceWorkerRegistrationData> registration)`
- `WhenRegistrationReady(WebCore::SecurityOriginData topOrigin, URL clientURL) -> (std::optional<WebCore::ServiceWorkerRegistrationData> registration)`
- `GetRegistrations(WebCore::SecurityOriginData topOrigin, URL clientURL) -> (Vector<WebCore::ServiceWorkerRegistrationData> registrations)`
- `RegisterServiceWorkerClient(WebCore::ClientOrigin clientOrigin, WebCore::ServiceWorkerClientData data, std::optional<WebCore::ServiceWorkerRegistrationIdentifier> controllingServiceWorkerRegistrationIdentifier, String userAgent)`
- `UnregisterServiceWorkerClient(WebCore::ScriptExecutionContextIdentifier identifier)`
- `TerminateWorkerFromClient(WebCore::ServiceWorkerIdentifier workerIdentifier) -> ()`
- `WhenServiceWorkerIsTerminatedForTesting(WebCore::ServiceWorkerIdentifier workerIdentifier) -> ()`
- `SetThrottleState(bool isThrottleable)`
- `StoreRegistrationsOnDisk() -> ()`
- `SubscribeToPushService(WebCore::ServiceWorkerRegistrationIdentifier identifier, Vector<uint8_t> applicationServerKey) -> (Expected<WebCore::PushSubscriptionData, WebCore::ExceptionData> result)`
- `UnsubscribeFromPushService(WebCore::ServiceWorkerRegistrationIdentifier serviceWorkerRegistrationIdentifier, WebCore::PushSubscriptionIdentifier pushSubscriptionIdentifier) -> (Expected<bool, WebCore::ExceptionData> result)`
- `GetPushSubscription(WebCore::ServiceWorkerRegistrationIdentifier identifier) -> (Expected<std::optional<WebCore::PushSubscriptionData>, WebCore::ExceptionData> result)`
- `GetPushPermissionState(WebCore::ServiceWorkerRegistrationIdentifier identifier) -> (Expected<uint8_t, WebCore::ExceptionData> result)`
- `EnableNavigationPreload(WebCore::ServiceWorkerRegistrationIdentifier identifier) -> (std::optional<WebCore::ExceptionData> result)`
- `DisableNavigationPreload(WebCore::ServiceWorkerRegistrationIdentifier identifier) -> (std::optional<WebCore::ExceptionData> result)`
- `SetNavigationPreloadHeaderValue(WebCore::ServiceWorkerRegistrationIdentifier identifier, String value) -> (std::optional<WebCore::ExceptionData> result)`
- `GetNavigationPreloadState(WebCore::ServiceWorkerRegistrationIdentifier identifier) -> (Expected<WebCore::NavigationPreloadState, WebCore::ExceptionData> result)`
- `StartBackgroundFetch(WebCore::ServiceWorkerRegistrationIdentifier registrationIdentifier, String backgroundFetchIdentifier, Vector<WebCore::BackgroundFetchRequest> requests, WebCore::BackgroundFetchOptions options) -> (Expected<std::optional<WebCore::BackgroundFetchInformation>, WebCore::ExceptionData> result)`
- `BackgroundFetchInformation(WebCore::ServiceWorkerRegistrationIdentifier registrationIdentifier, String backgroundFetchIdentifier) -> (Expected<std::optional<WebCore::BackgroundFetchInformation>, WebCore::ExceptionData> result)`
- `BackgroundFetchIdentifiers(WebCore::ServiceWorkerRegistrationIdentifier registrationIdentifier) -> (Vector<String> result)`
- `AbortBackgroundFetch(WebCore::ServiceWorkerRegistrationIdentifier registrationIdentifier, String backgroundFetchIdentifier) -> (bool result)`
- `MatchBackgroundFetch(WebCore::ServiceWorkerRegistrationIdentifier registrationIdentifier, String backgroundFetchIdentifier, WebCore::RetrieveRecordsOptions options) -> (Vector<WebCore::BackgroundFetchRecordInformation> results)`
- `RetrieveRecordResponse(WebCore::BackgroundFetchRecordIdentifier recordIdentifier) -> (Expected<WebCore::ResourceResponse, WebCore::ExceptionData> result)`
- `RetrieveRecordResponseBody(WebCore::BackgroundFetchRecordIdentifier recordIdentifier, WebKit::RetrieveRecordResponseBodyCallbackIdentifier callbackIdentifier)`
- `AddCookieChangeSubscriptions(WebCore::ServiceWorkerRegistrationIdentifier identifier, Vector<WebCore::CookieChangeSubscription> subscriptions) -> (std::optional<WebCore::ExceptionData> result)`
- `RemoveCookieChangeSubscriptions(WebCore::ServiceWorkerRegistrationIdentifier identifier, Vector<WebCore::CookieChangeSubscription> subscriptions) -> (std::optional<WebCore::ExceptionData> result)`
- `CookieChangeSubscriptions(WebCore::ServiceWorkerRegistrationIdentifier identifier) -> (Expected<Vector<WebCore::CookieChangeSubscription>, WebCore::ExceptionData> result)`
- `GetNotifications(URL registrationURL, String tag) -> (Expected<Vector<WebCore::NotificationData>, WebCore::ExceptionData> result)` (if ENABLE(WEB_PUSH_NOTIFICATIONS))

## `WebSWServerToContextConnection` - WebContent -> Networking

`NetworkProcess/ServiceWorker/WebSWServerToContextConnection.messages.in`

- `ScriptContextFailedToStart(std::optional<WebCore::ServiceWorkerJobDataIdentifier> jobDataIdentifier, WebCore::ServiceWorkerIdentifier serviceWorkerIdentifier, String message)`
- `ScriptContextStarted(std::optional<WebCore::ServiceWorkerJobDataIdentifier> jobDataIdentifier, WebCore::ServiceWorkerIdentifier serviceWorkerIdentifier, bool doesHandleFetch)`
- `DidFinishInstall(std::optional<WebCore::ServiceWorkerJobDataIdentifier> jobDataIdentifier, WebCore::ServiceWorkerIdentifier serviceWorkerIdentifier, bool wasSuccessful)`
- `DidFinishActivation(WebCore::ServiceWorkerIdentifier identifier)`
- `SetServiceWorkerHasPendingEvents(WebCore::ServiceWorkerIdentifier identifier, bool hasPendingEvents)`
- `SkipWaiting(WebCore::ServiceWorkerIdentifier identifier) -> ()`
- `WorkerTerminated(WebCore::ServiceWorkerIdentifier identifier)`
- `FindClientByVisibleIdentifier(WebCore::ServiceWorkerIdentifier serviceWorkerIdentifier, String clientIdentifier) -> (std::optional<WebCore::ServiceWorkerClientData> data)`
- `MatchAll(WebCore::ServiceWorkerIdentifier serviceWorkerIdentifier, WebCore::ServiceWorkerClientQueryOptions options) -> (Vector<WebCore::ServiceWorkerClientData> clientsData)`
- `Claim(WebCore::ServiceWorkerIdentifier serviceWorkerIdentifier) -> (std::optional<WebCore::ExceptionData> result)`
- `Focus(WebCore::ScriptExecutionContextIdentifier serviceWorkerClientIdentifier) -> (std::optional<WebCore::ServiceWorkerClientData> result)`
- `Navigate(WebCore::ScriptExecutionContextIdentifier clientIdentifier, WebCore::ServiceWorkerIdentifier serviceWorkerIdentifier, URL url) -> (Expected<std::optional<WebCore::ServiceWorkerClientData>, WebCore::ExceptionData> result)`
- `SetScriptResource(WebCore::ServiceWorkerIdentifier identifier, URL scriptURL, WebCore::ServiceWorkerImportedScript script)`
- `PostMessageToServiceWorkerClient(WebCore::ScriptExecutionContextIdentifier destination, WebCore::MessageWithMessagePorts message, WebCore::ServiceWorkerIdentifier source, String sourceOrigin)`
- `DidFailHeartBeatCheck(WebCore::ServiceWorkerIdentifier identifier)`
- `SetAsInspected(WebCore::ServiceWorkerIdentifier identifier, bool isInspected)`
- `OpenWindow(WebCore::ServiceWorkerIdentifier identifier, URL url) -> (Expected<std::optional<WebCore::ServiceWorkerClientData>, WebCore::ExceptionData> newClientData)`
- `ReportConsoleMessage(WebCore::ServiceWorkerIdentifier identifier, JSC::MessageSource messageSource, JSC::MessageLevel messageLevel, String message, unsigned long requestIdentifier)`

## `WebSharedWorkerServerConnection` - WebContent -> Networking

`NetworkProcess/SharedWorker/WebSharedWorkerServerConnection.messages.in`

- `RequestSharedWorker(WebCore::SharedWorkerKey sharedWorkerKey, WebCore::SharedWorkerObjectIdentifier sharedWorkerObjectIdentifier, WebCore::TransferredMessagePort port, WebCore::WorkerOptions workerOptions)`
- `SharedWorkerObjectIsGoingAway(WebCore::SharedWorkerKey sharedWorkerKey, WebCore::SharedWorkerObjectIdentifier sharedWorkerObjectIdentifier)`
- `SuspendForBackForwardCache(WebCore::SharedWorkerKey sharedWorkerKey, WebCore::SharedWorkerObjectIdentifier sharedWorkerObjectIdentifier)`
- `ResumeForBackForwardCache(WebCore::SharedWorkerKey sharedWorkerKey, WebCore::SharedWorkerObjectIdentifier sharedWorkerObjectIdentifier)`

## `WebSharedWorkerServerToContextConnection` - WebContent -> Networking

`NetworkProcess/SharedWorker/WebSharedWorkerServerToContextConnection.messages.in`

- `PostErrorToWorkerObject(WebCore::SharedWorkerIdentifier sharedWorkerIdentifier, String errorMessage, int lineNumber, int columnNumber, String sourceURL, bool isErrorEvent)`
- `SharedWorkerTerminated(WebCore::SharedWorkerIdentifier sharedWorkerIdentifier)`

## `ModelConnectionToWebProcess` - WebContent -> Model

`ModelProcess/ModelConnectionToWebProcess.messages.in`

- `CreateVisibilityPropagationContextForPage(WebKit::WebPageProxyIdentifier pageProxyID, WebCore::PageIdentifier pageID, bool canShowWhileLocked)` (if HAVE(VISIBILITY_PROPAGATION_VIEW))
- `DestroyVisibilityPropagationContextForPage(WebKit::WebPageProxyIdentifier pageProxyID, WebCore::PageIdentifier pageID)` (if HAVE(VISIBILITY_PROPAGATION_VIEW))
- `ConfigureLoggingChannel(String channelName, WTFLogChannelState state, WTFLogLevel level)`

## `ModelProcessModelPlayerManagerProxy` - WebContent -> Model

`ModelProcess/ModelProcessModelPlayerManagerProxy.messages.in`

- `CreateModelPlayer(WebCore::ModelPlayerIdentifier identifier)`
- `DeleteModelPlayer(WebCore::ModelPlayerIdentifier identifier)`

## `ModelProcessModelPlayerProxy` - WebContent -> Model

`ModelProcess/cocoa/ModelProcessModelPlayerProxy.messages.in`

- `CreateLayer()`
- `LoadModel(Ref<WebCore::Model> url, WebCore::LayoutSize layoutSize)`
- `SizeDidChange(WebCore::LayoutSize layoutSize)`
- `SetBackgroundColor(WebCore::Color color)`
- `SetEntityTransform(WebCore::TransformationMatrix transform)`
- `SetAutoplay(bool autoplay)`
- `SetLoop(bool loop)`
- `SetPlaybackRate(double playbackRate) -> (double effectivePlaybackRate)` (Async)
- `SetPaused(bool paused) -> (bool succeeded)` (Async)
- `SetCurrentTime(Seconds currentTime) -> ()` (Async)
- `SetEnvironmentMap(Ref<WebCore::SharedBuffer> data)`
- `SetHasPortal(bool hasPortal)`

## `AcceleratedSurfaceDMABuf` - UI -> WebContent

`WebProcess/WebPage/dmabuf/AcceleratedSurfaceDMABuf.messages.in`

- `ReleaseBuffer(uint64_t id, UnixFileDescriptor releaseFence)`
- `FrameDone()`

## `AuxiliaryProcess` - UI -> WebContent, GPU, Networking, Model

`Shared/AuxiliaryProcess.messages.in`

- `ShutDown()`
- `SetProcessSuppressionEnabled(bool flag)`
- `MainThreadPing() -> ()`
- `PreferenceDidUpdate(String domain, String key, std::optional<String> encodedValue)` (if ENABLE(CFPREFS_DIRECT_MODE))
- `DidReceiveMemoryPressureEvent(bool isCritical)` (if OS(LINUX))

## `DrawingArea` - UI -> WebContent

`WebProcess/WebPage/DrawingArea.messages.in`

- `UpdateGeometry(WebCore::IntSize size) -> ()` (if USE(COORDINATED_GRAPHICS) || USE(TEXTURE_MAPPER))
- `ForceUpdate()` (if USE(COORDINATED_GRAPHICS) || USE(TEXTURE_MAPPER))
- `DidDiscardBackingStore()` (if USE(COORDINATED_GRAPHICS) || USE(TEXTURE_MAPPER))
- `SetDeviceScaleFactor(float deviceScaleFactor) -> ()`
- `DisplayDidRefresh()`
- `UpdateGeometry(WebCore::IntSize viewSize, bool flushSynchronously, MachSendRight fencePort) -> ()` (if PLATFORM(COCOA))
- `SetColorSpace(std::optional<WebCore::DestinationColorSpace> colorSpace)` (if PLATFORM(COCOA))
- `SetViewExposedRect(std::optional<WebCore::FloatRect> viewExposedRect)` (if PLATFORM(COCOA))
- `AcceleratedAnimationDidStart(WebCore::PlatformLayerIdentifier layerID, String key, MonotonicTime startTime)` (if PLATFORM(COCOA))
- `AcceleratedAnimationDidEnd(WebCore::PlatformLayerIdentifier layerID, String key)` (if PLATFORM(COCOA))
- `DispatchAfterEnsuringDrawing() -> ()` (CallWithReplyID, if PLATFORM(COCOA) || PLATFORM(GTK) || PLATFORM(WPE))
- `UpdateGeometryWC(uint64_t backingStoreStateID, WebCore::IntSize viewSize, float deviceScaleFactor, float intrinsicDeviceScaleFactor)` (if USE(GRAPHICS_LAYER_WC))
- `AdjustTransientZoom(double scale, WebCore::FloatPoint origin)` (if PLATFORM(COCOA) || PLATFORM(GTK))
- `CommitTransientZoom(double scale, WebCore::FloatPoint origin) -> ()` (if PLATFORM(COCOA) || PLATFORM(GTK))

## `EventDispatcher` - UI -> WebContent

`WebProcess/WebPage/EventDispatcher.messages.in`

- `WheelEvent(WebCore::PageIdentifier pageID, WebKit::WebWheelEvent event, WebCore::RectEdges<bool> rubberBandableEdges)`
- `TouchEvent(WebCore::PageIdentifier pageID, WebCore::FrameIdentifier frameID, WebKit::WebTouchEvent event) -> (bool handled, std::optional<WebCore::RemoteUserInputEventData> remoteTouchEventData)` (MainThreadCallback, if ENABLE(IOS_TOUCH_EVENTS))
- `GestureEvent(WebCore::FrameIdentifier frameID, WebCore::PageIdentifier pageID, WebKit::WebGestureEvent event) -> (std::optional<WebKit::WebEventType> eventType, bool handled, std::optional<WebCore::RemoteUserInputEventData> remoteUserInputEventData)` (MainThreadCallback, if ENABLE(MAC_GESTURE_EVENTS))
- `DisplayDidRefresh(uint32_t displayID, WebCore::DisplayUpdate update, bool sendToMainThread)` (if HAVE(DISPLAY_LINK))
- `SetScrollingAccelerationCurve(WebCore::PageIdentifier pageID, std::optional<WebKit::ScrollingAccelerationCurve> curve)` (if ENABLE(MOMENTUM_EVENT_DISPATCHER))
- `PageScreenDidChange(WebCore::PageIdentifier pageID, uint32_t displayID, std::optional<unsigned> nominalFramesPerSecond)`

## `PlatformXRSystemProxy` - UI -> WebContent

`WebProcess/XR/PlatformXRSystemProxy.messages.in`

- `SessionDidEnd(WebKit::XRDeviceIdentifier deviceIdentifier)`
- `SessionDidUpdateVisibilityState(WebKit::XRDeviceIdentifier deviceIdentifier, PlatformXR::VisibilityState visibilityState)`

## `PlaybackSessionManager` - UI -> WebContent

`WebProcess/cocoa/PlaybackSessionManager.messages.in`

- `Play(WebKit::PlaybackSessionContextIdentifier contextId)`
- `Pause(WebKit::PlaybackSessionContextIdentifier contextId)`
- `TogglePlayState(WebKit::PlaybackSessionContextIdentifier contextId)`
- `BeginScrubbing(WebKit::PlaybackSessionContextIdentifier contextId)`
- `EndScrubbing(WebKit::PlaybackSessionContextIdentifier contextId)`
- `SeekToTime(WebKit::PlaybackSessionContextIdentifier contextId, double time, double toleranceBefore, double toleranceAfter)`
- `FastSeek(WebKit::PlaybackSessionContextIdentifier contextId, double time)`
- `BeginScanningForward(WebKit::PlaybackSessionContextIdentifier contextId)`
- `BeginScanningBackward(WebKit::PlaybackSessionContextIdentifier contextId)`
- `EndScanning(WebKit::PlaybackSessionContextIdentifier contextId)`
- `SetDefaultPlaybackRate(WebKit::PlaybackSessionContextIdentifier contextId, float defaultPlaybackRate)`
- `SetPlaybackRate(WebKit::PlaybackSessionContextIdentifier contextId, float playbackRate)`
- `SelectAudioMediaOption(WebKit::PlaybackSessionContextIdentifier contextId, uint64_t index)`
- `SelectLegibleMediaOption(WebKit::PlaybackSessionContextIdentifier contextId, uint64_t index)`
- `HandleControlledElementIDRequest(WebKit::PlaybackSessionContextIdentifier contextId)`
- `TogglePictureInPicture(WebKit::PlaybackSessionContextIdentifier contextId)`
- `EnterFullscreen(WebKit::PlaybackSessionContextIdentifier contextId)`
- `ExitFullscreen(WebKit::PlaybackSessionContextIdentifier contextId)`
- `EnterInWindow(WebKit::PlaybackSessionContextIdentifier contextId)`
- `ExitInWindow(WebKit::PlaybackSessionContextIdentifier contextId)`
- `ToggleMuted(WebKit::PlaybackSessionContextIdentifier contextId)`
- `SetMuted(WebKit::PlaybackSessionContextIdentifier contextId, bool muted)`
- `SetVolume(WebKit::PlaybackSessionContextIdentifier contextId, double volume)`
- `SetPlayingOnSecondScreen(WebKit::PlaybackSessionContextIdentifier contextId, bool value)`
- `SendRemoteCommand(WebKit::PlaybackSessionContextIdentifier contextId, WebCore::PlatformMediaSessionRemoteControlCommandType type, WebCore::PlatformMediaSession::RemoteCommandArgument argument)`
- `SetSoundStageSize(WebKit::PlaybackSessionContextIdentifier contextId, WebCore::AudioSessionSoundStageSize size)`
- `SetSpatialTrackingLabel(WebKit::PlaybackSessionContextIdentifier contextId, String label)` (if HAVE(SPATIAL_TRACKING_LABEL))

## `RemoteMediaSessionCoordinator` - UI -> WebContent

`WebProcess/MediaSession/RemoteMediaSessionCoordinator.messages.in`

- `SeekSessionToTime(double time) -> (bool result)`
- `PlaySession(std::optional<double> atTime, std::optional<MonotonicTime> hostTime) -> (bool result)`
- `PauseSession() -> (bool result)`
- `SetSessionTrack(String trackIdentifier) -> (bool result)`
- `CoordinatorStateChanged(WebCore::MediaSessionCoordinatorState state)`

## `RemoteObjectRegistry` - UI, WebContent -> WebContent, UI

`Shared/API/Cocoa/RemoteObjectRegistry.messages.in`

- `InvokeMethod(WebKit::RemoteObjectInvocation invocation)`
- `CallReplyBlock(uint64_t replyID, WebKit::UserData blockInvocation)`
- `ReleaseUnusedReplyBlock(uint64_t replyID)`

## `RemoteScrollingCoordinator` - UI -> WebContent

`WebProcess/WebPage/RemoteLayerTree/RemoteScrollingCoordinator.messages.in`

- `ScrollPositionChangedForNode(WebCore::ScrollingNodeID nodeID, WebCore::FloatPoint scrollPosition, std::optional<WebCore::FloatPoint> layoutViewportOrigin, bool syncLayerPosition) -> ()`
- `AnimatedScrollDidEndForNode(WebCore::ScrollingNodeID nodeID)`
- `CurrentSnapPointIndicesChangedForNode(WebCore::ScrollingNodeID nodeID, std::optional<unsigned> horizontal, std::optional<unsigned> vertical)`
- `ScrollingStateInUIProcessChanged(WebKit::RemoteScrollingUIState uiState)`
- `ReceivedWheelEventWithPhases(WebCore::PlatformWheelEventPhase phase, WebCore::PlatformWheelEventPhase momentumPhase)`
- `StartDeferringScrollingTestCompletionForNode(WebCore::ScrollingNodeID nodeID, OptionSet<WebCore::WheelEventTestMonitorDeferReason> reason)`
- `StopDeferringScrollingTestCompletionForNode(WebCore::ScrollingNodeID nodeID, OptionSet<WebCore::WheelEventTestMonitorDeferReason> reason)`
- `ScrollingTreeNodeScrollbarVisibilityDidChange(WebCore::ScrollingNodeID nodeID, WebCore::ScrollbarOrientation orientation, bool isVisible)`
- `ScrollingTreeNodeScrollbarMinimumThumbLengthDidChange(WebCore::ScrollingNodeID nodeID, WebCore::ScrollbarOrientation orientation, int minimumThumbLength)`

## `RemoteWebInspectorUI` - UI -> WebContent

`WebProcess/Inspector/RemoteWebInspectorUI.messages.in`

- `Initialize(WebKit::DebuggableInfoData debuggableInfo, String backendCommandsURL)`
- `UpdateFindString(String findString)`
- `SetDiagnosticLoggingAvailable(bool available)` (if ENABLE(INSPECTOR_TELEMETRY))
- `ShowConsole()`
- `ShowResources()`
- `SendMessageToFrontend(String message)`

## `RemoteWebLockRegistry` - UI -> WebContent

`WebProcess/WebCoreSupport/RemoteWebLockRegistry.messages.in`

- `DidCompleteLockRequest(WebCore::WebLockIdentifier lockIdentifier, WebCore::ScriptExecutionContextIdentifier clientID, bool success)`
- `DidStealLock(WebCore::WebLockIdentifier lockIdentifier, WebCore::ScriptExecutionContextIdentifier clientID)`

## `SpeechRecognitionRealtimeMediaSourceManager` - UI -> WebContent

`WebProcess/Speech/SpeechRecognitionRealtimeMediaSourceManager.messages.in`

- `CreateSource(WebCore::RealtimeMediaSourceIdentifier identifier, WebCore::CaptureDevice device, WebCore::PageIdentifier pageIdentifier)`
- `DeleteSource(WebCore::RealtimeMediaSourceIdentifier identifier)`
- `Start(WebCore::RealtimeMediaSourceIdentifier identifier)`
- `Stop(WebCore::RealtimeMediaSourceIdentifier identifier)`

## `SystemSettingsManager` - UI -> WebContent

`WebProcess/glib/SystemSettingsManager.messages.in`

- `DidChange(WebCore::SystemSettings::State state)`

## `TextCheckingControllerProxy` - UI -> WebContent

`WebProcess/WebPage/Cocoa/TextCheckingControllerProxy.messages.in`

- `ReplaceRelativeToSelection(WebCore::AttributedString annotatedString, int64_t selectionOffset, uint64_t length, uint64_t relativeReplacementLocation, uint64_t relativeReplacementLength)`
- `RemoveAnnotationRelativeToSelection(String annotationName, int64_t selectionOffset, uint64_t length)`

## `UserMediaCaptureManager` - UI -> WebContent

`WebProcess/cocoa/UserMediaCaptureManager.messages.in`

- `SourceStopped(WebCore::RealtimeMediaSourceIdentifier id, bool didFail)`
- `SourceMutedChanged(WebCore::RealtimeMediaSourceIdentifier id, bool muted, bool interrupted)`
- `SourceSettingsChanged(WebCore::RealtimeMediaSourceIdentifier id, WebCore::RealtimeMediaSourceSettings settings)`
- `SourceConfigurationChanged(WebCore::RealtimeMediaSourceIdentifier id, String persistentID, WebCore::RealtimeMediaSourceSettings settings, WebCore::RealtimeMediaSourceCapabilities capabilities)`
- `ApplyConstraintsSucceeded(WebCore::RealtimeMediaSourceIdentifier id, WebCore::RealtimeMediaSourceSettings settings)`
- `ApplyConstraintsFailed(WebCore::RealtimeMediaSourceIdentifier id, WebCore::MediaConstraintType invalidConstraint, String message)`

## `UserMediaCaptureManager` - UI -> WebContent

`WebProcess/glib/UserMediaCaptureManager.messages.in`

- `ValidateUserMediaRequestConstraints(WebCore::MediaStreamRequest request, WebCore::MediaDeviceHashSalts mediaDeviceIdentifierHashSalts) -> (std::optional<WebCore::MediaConstraintType> invalidConstraint, Vector<WebCore::CaptureDevice> audioDevices, Vector<WebCore::CaptureDevice> videoDevices)`
- `GetMediaStreamDevices(bool revealIdsAndLabels) -> (Vector<WebCore::CaptureDeviceWithCapabilities> devices)`

## `VideoPresentationManager` - UI -> WebContent

`WebProcess/cocoa/VideoPresentationManager.messages.in`

- `RequestFullscreenMode(WebKit::PlaybackSessionContextIdentifier contextId, WebCore::MediaPlayerEnums::VideoFullscreenMode videoFullscreenMode, bool finishedWithMedia)`
- `RequestUpdateInlineRect(WebKit::PlaybackSessionContextIdentifier contextId)`
- `RequestVideoContentLayer(WebKit::PlaybackSessionContextIdentifier contextId)`
- `ReturnVideoContentLayer(WebKit::PlaybackSessionContextIdentifier contextId)`
- `DidSetupFullscreen(WebKit::PlaybackSessionContextIdentifier contextId)` (if !PLATFORM(IOS_FAMILY))
- `WillExitFullscreen(WebKit::PlaybackSessionContextIdentifier contextId)`
- `DidExitFullscreen(WebKit::PlaybackSessionContextIdentifier contextId)`
- `DidEnterFullscreen(WebKit::PlaybackSessionContextIdentifier contextId, std::optional<WebCore::FloatSize> size)`
- `FailedToEnterFullscreen(WebKit::PlaybackSessionContextIdentifier contextId)`
- `DidCleanupFullscreen(WebKit::PlaybackSessionContextIdentifier contextId)`
- `SetVideoLayerFrameFenced(WebKit::PlaybackSessionContextIdentifier contextId, WebCore::FloatRect bounds, MachSendRight machSendRight)`
- `SetVideoLayerGravityEnum(WebKit::PlaybackSessionContextIdentifier contextId, unsigned gravity)`
- `SetVideoFullscreenFrame(WebKit::PlaybackSessionContextIdentifier contextId, WebCore::FloatRect frame)`
- `FullscreenModeChanged(WebKit::PlaybackSessionContextIdentifier contextId, WebCore::MediaPlayerEnums::VideoFullscreenMode videoFullscreenMode)`
- `FullscreenMayReturnToInline(WebKit::PlaybackSessionContextIdentifier contextId, bool isPageVisible)`
- `RequestRouteSharingPolicyAndContextUID(WebKit::PlaybackSessionContextIdentifier contextId) -> (WebCore::RouteSharingPolicy routeSharingPolicy, String routingContextUID)`
- `EnsureUpdatedVideoDimensions(WebKit::PlaybackSessionContextIdentifier contextId, WebCore::FloatSize existingVideoDimensions)`
- `SetRequiresTextTrackRepresentation(WebKit::PlaybackSessionContextIdentifier contextId, bool requiresTextTrackRepresentation)`
- `SetTextTrackRepresentationBounds(WebKit::PlaybackSessionContextIdentifier contextId, WebCore::IntRect bounds)`

## `ViewGestureGeometryCollector` - UI -> WebContent

`WebProcess/WebPage/ViewGestureGeometryCollector.messages.in`

- `CollectGeometryForSmartMagnificationGesture(WebCore::FloatPoint origin)` (if PLATFORM(COCOA))
- `CollectGeometryForMagnificationGesture()` (if !PLATFORM(IOS_FAMILY))
- `SetRenderTreeSizeNotificationThreshold(uint64_t size)` (if !PLATFORM(IOS_FAMILY))

## `ViewUpdateDispatcher` - UI -> WebContent

`WebProcess/WebPage/ViewUpdateDispatcher.messages.in`

- `VisibleContentRectUpdate(WebCore::PageIdentifier pageID, WebKit::VisibleContentRectUpdateInfo visibleContentRectUpdateInfo)`

## `VisitedLinkTableController` - UI -> WebContent

`WebProcess/WebPage/VisitedLinkTableController.messages.in`

- `SetVisitedLinkTable(WebCore::SharedMemory::Handle handle)`
- `VisitedLinkStateChanged(Vector<WebCore::SharedStringHash> linkHashes)`
- `AllVisitedLinkStateChanged()`
- `RemoveAllVisitedLinks()`

## `WebAutomationSessionProxy` - UI -> WebContent

`WebProcess/Automation/WebAutomationSessionProxy.messages.in`

- `EvaluateJavaScriptFunction(WebCore::PageIdentifier pageID, std::optional<WebCore::FrameIdentifier> frameID, String function, Vector<String> arguments, bool expectsImplicitCallbackArgument, bool forceUserGesture, std::optional<double> callbackTimeout) -> (String result, String errorType)`
- `ResolveChildFrameWithOrdinal(WebCore::PageIdentifier pageID, std::optional<WebCore::FrameIdentifier> frameID, uint32_t ordinal) -> (std::optional<String> errorType, std::optional<WebCore::FrameIdentifier> frameID)`
- `ResolveChildFrameWithNodeHandle(WebCore::PageIdentifier pageID, std::optional<WebCore::FrameIdentifier> frameID, String nodeHandle) -> (std::optional<String> errorType, std::optional<WebCore::FrameIdentifier> frameID)`
- `ResolveChildFrameWithName(WebCore::PageIdentifier pageID, std::optional<WebCore::FrameIdentifier> frameID, String name) -> (std::optional<String> errorType, std::optional<WebCore::FrameIdentifier> frameID)`
- `ResolveParentFrame(WebCore::PageIdentifier pageID, std::optional<WebCore::FrameIdentifier> frameID) -> (std::optional<String> errorType, std::optional<WebCore::FrameIdentifier> frameID)`
- `ComputeElementLayout(WebCore::PageIdentifier pageID, std::optional<WebCore::FrameIdentifier> frameID, String nodeHandle, bool scrollIntoViewIfNeeded, WebKit::CoordinateSystem coordinateSystem) -> (std::optional<String> errorType, WebCore::FloatRect rect, std::optional<WebCore::IntPoint> inViewCenterPoint, bool isObscured)`
- `GetComputedRole(WebCore::PageIdentifier pageID, std::optional<WebCore::FrameIdentifier> frameID, String nodeHandle) -> (std::optional<String> role, std::optional<String> errorType)`
- `GetComputedLabel(WebCore::PageIdentifier pageID, std::optional<WebCore::FrameIdentifier> frameID, String nodeHandle) -> (std::optional<String> role, std::optional<String> errorType)`
- `SelectOptionElement(WebCore::PageIdentifier pageID, std::optional<WebCore::FrameIdentifier> frameID, String nodeHandle) -> (std::optional<String> errorType)`
- `SetFilesForInputFileUpload(WebCore::PageIdentifier pageID, std::optional<WebCore::FrameIdentifier> frameID, String nodeHandle, Vector<String> filenames) -> (std::optional<String> errorType)`
- `TakeScreenshot(WebCore::PageIdentifier pageID, std::optional<WebCore::FrameIdentifier> frameID, String nodeHandle, bool scrollIntoViewIfNeeded, bool clipToViewport) -> (std::optional<WebCore::ShareableBitmapHandle> imageDataHandle, String errorType)`
- `SnapshotRectForScreenshot(WebCore::PageIdentifier pageID, std::optional<WebCore::FrameIdentifier> frameID, String nodeHandle, bool scrollIntoViewIfNeeded, bool clipToViewport) -> (std::optional<String> errorType, WebCore::IntRect rect)`
- `GetCookiesForFrame(WebCore::PageIdentifier pageID, std::optional<WebCore::FrameIdentifier> frameID) -> (std::optional<String> errorType, Vector<WebCore::Cookie> cookies)`
- `DeleteCookie(WebCore::PageIdentifier pageID, std::optional<WebCore::FrameIdentifier> frameID, String cookieName) -> (std::optional<String> errorType)`

## `WebDeviceOrientationUpdateProvider` - UI -> WebContent

`WebProcess/WebCoreSupport/WebDeviceOrientationUpdateProvider.messages.in`

- `DeviceOrientationChanged(double alpha, double beta, double gamma, double compassHeading, double compassAccuracy)`
- `DeviceMotionChanged(double xAcceleration, double yAcceleration, double zAcceleration, double xAccelerationIncludingGravity, double yAccelerationIncludingGravity, double zAccelerationIncludingGravity, std::optional<double> xRotationRate, std::optional<double> yRotationRate, std::optional<double> zRotationRate)`

## `WebExtensionContextProxy` - UI -> WebContent

`WebProcess/Extensions/WebExtensionContextProxy.messages.in`

- `DispatchActionClickedEvent(std::optional<WebKit::WebExtensionTabParameters> tabParameters)`
- `DispatchAlarmsEvent(WebKit::WebExtensionAlarmParameters alarmInfo)`
- `DispatchCommandsCommandEvent(String identifier, std::optional<WebKit::WebExtensionTabParameters> tabParameters)`
- `DispatchCommandsChangedEvent(String identifier, String oldShortcut, String newShortcut)`
- `DispatchCookiesChangedEvent()`
- `AddInspectorPageIdentifier(WebCore::PageIdentifier pageID, std::optional<WebKit::WebExtensionTabIdentifier> tabIdentifier, std::optional<WebKit::WebExtensionWindowIdentifier> windowIdentifier)` (if ENABLE(INSPECTOR_EXTENSIONS))
- `AddInspectorBackgroundPageIdentifier(WebCore::PageIdentifier pageID, std::optional<WebKit::WebExtensionTabIdentifier> tabIdentifier, std::optional<WebKit::WebExtensionWindowIdentifier> windowIdentifier)` (if ENABLE(INSPECTOR_EXTENSIONS))
- `DispatchDevToolsExtensionPanelShownEvent(Inspector::ExtensionTabID identifier, WebCore::FrameIdentifier frameIdentifier)` (if ENABLE(INSPECTOR_EXTENSIONS))
- `DispatchDevToolsExtensionPanelHiddenEvent(Inspector::ExtensionTabID identifier)` (if ENABLE(INSPECTOR_EXTENSIONS))
- `DispatchDevToolsNetworkNavigatedEvent(URL url)` (if ENABLE(INSPECTOR_EXTENSIONS))
- `DispatchDevToolsPanelsThemeChangedEvent(Inspector::ExtensionAppearance appearance)` (if ENABLE(INSPECTOR_EXTENSIONS))
- `SetBackgroundPageIdentifier(WebCore::PageIdentifier pageID)`
- `AddPopupPageIdentifier(WebCore::PageIdentifier pageID, std::optional<WebKit::WebExtensionTabIdentifier> tabIdentifier, std::optional<WebKit::WebExtensionWindowIdentifier> windowIdentifier)`
- `AddTabPageIdentifier(WebCore::PageIdentifier pageID, WebKit::WebExtensionTabIdentifier tabIdentifier, std::optional<WebKit::WebExtensionWindowIdentifier> windowIdentifier)`
- `DispatchMenusClickedEvent(WebKit::WebExtensionMenuItemParameters menuItemParameters, bool wasChecked, WebKit::WebExtensionMenuItemContextParameters contextParameters, std::optional<WebKit::WebExtensionTabParameters> tabParameters)`
- `UpdateGrantedPermissions(HashMap<String, WallTime> permissions)`
- `DispatchPermissionsEvent(WebKit::WebExtensionEventListenerType type, HashSet<String> permissions, HashSet<String> origins)`
- `DispatchPortMessageEvent(std::optional<WebKit::WebPageProxyIdentifier> sendingPageProxyIdentifier, WebKit::WebExtensionPortChannelIdentifier channelIdentifier, String messageJSON)`
- `DispatchPortDisconnectEvent(WebKit::WebExtensionPortChannelIdentifier channelIdentifier)`
- `DispatchRuntimeMessageEvent(WebKit::WebExtensionContentWorldType contentWorldType, String messageJSON, std::optional<WebKit::WebExtensionMessageTargetParameters> targetParameters, WebKit::WebExtensionMessageSenderParameters senderParameters) -> (String replyJSON)`
- `DispatchRuntimeConnectEvent(WebKit::WebExtensionContentWorldType contentWorldType, WebKit::WebExtensionPortChannelIdentifier channelIdentifier, String name, std::optional<WebKit::WebExtensionMessageTargetParameters> targetParameters, WebKit::WebExtensionMessageSenderParameters senderParameters) -> (HashCountedSet<WebKit::WebPageProxyIdentifier> addedPortCounts)`
- `DispatchRuntimeInstalledEvent(WebKit::WebExtensionContextInstallReason installReason, String previousVersion)`
- `DispatchRuntimeStartupEvent()`
- `SetStorageAccessLevel(bool allowedInContentScripts)`
- `DispatchStorageChangedEvent(String onChangedJSON, WebKit::WebExtensionDataType dataType, WebKit::WebExtensionContentWorldType contentWorldType)`
- `DispatchTabsCreatedEvent(WebKit::WebExtensionTabParameters tabParameters)`
- `DispatchTabsUpdatedEvent(WebKit::WebExtensionTabParameters tabParameters, WebKit::WebExtensionTabParameters changedParameters)`
- `DispatchTabsReplacedEvent(WebKit::WebExtensionTabIdentifier replacedTabIdentifier, WebKit::WebExtensionTabIdentifier newTabIdentifier)`
- `DispatchTabsDetachedEvent(WebKit::WebExtensionTabIdentifier tabIdentifier, WebKit::WebExtensionWindowIdentifier oldWindowIdentifier, size_t oldIndex)`
- `DispatchTabsMovedEvent(WebKit::WebExtensionTabIdentifier tabIdentifier, WebKit::WebExtensionWindowIdentifier windowIdentifier, size_t oldIndex, size_t newIndex)`
- `DispatchTabsAttachedEvent(WebKit::WebExtensionTabIdentifier tabIdentifier, WebKit::WebExtensionWindowIdentifier newWindowIdentifier, size_t newIndex)`
- `DispatchTabsActivatedEvent(WebKit::WebExtensionTabIdentifier previousActiveTabIdentifier, WebKit::WebExtensionTabIdentifier newActiveTabIdentifier, WebKit::WebExtensionWindowIdentifier windowIdentifier)`
- `DispatchTabsHighlightedEvent(Vector<WebKit::WebExtensionTabIdentifier> tabs, WebKit::WebExtensionWindowIdentifier windowIdentifier)`
- `DispatchTabsRemovedEvent(WebKit::WebExtensionTabIdentifier tabIdentifier, WebKit::WebExtensionWindowIdentifier windowIdentifier, WebKit::WebExtensionContext::WindowIsClosing windowIsClosing)`
- `DispatchTestMessageEvent(String message, String argumentJSON, WebKit::WebExtensionContentWorldType contentWorldType)`
- `DispatchWebNavigationEvent(WebKit::WebExtensionEventListenerType type, WebKit::WebExtensionTabIdentifier tabID, WebKit::WebExtensionFrameParameters frameParamaters, WallTime timestamp)`
- `ResourceLoadDidSendRequest(WebKit::WebExtensionTabIdentifier tabIdentifier, WebKit::WebExtensionWindowIdentifier windowIdentifier, WebCore::ResourceRequest request, WebKit::ResourceLoadInfo resourceLoadInfo, std::optional<IPC::FormDataReference> formData)`
- `ResourceLoadDidPerformHTTPRedirection(WebKit::WebExtensionTabIdentifier tabIdentifier, WebKit::WebExtensionWindowIdentifier windowIdentifier, WebCore::ResourceResponse response, WebKit::ResourceLoadInfo resourceLoadInfo, WebCore::ResourceRequest newRequest)`
- `ResourceLoadDidReceiveChallenge(WebKit::WebExtensionTabIdentifier tabIdentifier, WebKit::WebExtensionWindowIdentifier windowIdentifier, WebCore::AuthenticationChallenge challenge, WebKit::ResourceLoadInfo resourceLoadInfo)`
- `ResourceLoadDidReceiveResponse(WebKit::WebExtensionTabIdentifier tabIdentifier, WebKit::WebExtensionWindowIdentifier windowIdentifier, WebCore::ResourceResponse response, WebKit::ResourceLoadInfo resourceLoadInfo)`
- `ResourceLoadDidCompleteWithError(WebKit::WebExtensionTabIdentifier tabIdentifier, WebKit::WebExtensionWindowIdentifier windowIdentifier, WebCore::ResourceResponse response, WebCore::ResourceError error, WebKit::ResourceLoadInfo resourceLoadInfo)`
- `DispatchWindowsEvent(WebKit::WebExtensionEventListenerType type, std::optional<WebKit::WebExtensionWindowParameters> windowParameters)`

## `WebExtensionControllerProxy` - UI -> WebContent

`WebProcess/Extensions/WebExtensionControllerProxy.messages.in`

- `Load(WebKit::WebExtensionContextParameters contextParameters)`
- `Unload(WebKit::WebExtensionContextIdentifier contextIdentifier)`

## `WebFullScreenManager` - UI -> WebContent

`WebProcess/FullScreen/WebFullScreenManager.messages.in`

- `RequestRestoreFullScreen() -> (bool succeeded)` (Async)
- `RequestExitFullScreen()`
- `DidEnterFullScreen()`
- `WillExitFullScreen()`
- `DidExitFullScreen()`
- `SetAnimatingFullScreen(bool animating)`
- `SaveScrollPosition()`
- `RestoreScrollPosition()`
- `SetFullscreenInsets(WebCore::FloatBoxExtent insets)`
- `SetFullscreenAutoHideDuration(Seconds duration)`

## `WebGeolocationManager` - UI -> WebContent

`WebProcess/Geolocation/WebGeolocationManager.messages.in`

- `DidChangePosition(WebCore::RegistrableDomain registrableDomain, WebCore::GeolocationPositionData position)`
- `DidFailToDeterminePosition(WebCore::RegistrableDomain registrableDomain, String errorMessage)`
- `ResetPermissions(WebCore::RegistrableDomain registrableDomain)` (if PLATFORM(IOS_FAMILY))

## `WebInspector` - UI -> WebContent

`WebProcess/Inspector/WebInspector.messages.in`

- `Show() -> ()` (Async)
- `Close()`
- `SetAttached(bool attached)`
- `ShowConsole()`
- `ShowResources()`
- `ShowMainResourceForFrame(WebCore::FrameIdentifier frameIdentifier)`
- `StartPageProfiling()`
- `StopPageProfiling()`
- `StartElementSelection()`
- `StopElementSelection()`
- `SetFrontendConnection(IPC::ConnectionHandle connectionHandle)`

## `WebInspectorInterruptDispatcher` - UI -> WebContent

`WebProcess/Inspector/WebInspectorInterruptDispatcher.messages.in`

- `NotifyNeedDebuggerBreak()`

## `WebInspectorUI` - UI -> WebContent

`WebProcess/Inspector/WebInspectorUI.messages.in`

- `EstablishConnection(WebKit::WebPageProxyIdentifier inspectedPageIdentifier, WebKit::DebuggableInfoData debuggableInfo, bool underTest, unsigned inspectionLevel)`
- `UpdateConnection()`
- `AttachedBottom()`
- `AttachedRight()`
- `AttachedLeft()`
- `Detached()`
- `SetDockingUnavailable(bool unavailable)`
- `SetIsVisible(bool visible)`
- `UpdateFindString(String findString)`
- `SetDiagnosticLoggingAvailable(bool available)` (if ENABLE(INSPECTOR_TELEMETRY))
- `ShowConsole()`
- `ShowResources()`
- `ShowMainResourceForFrame(String frameIdentifier)`
- `StartPageProfiling()`
- `StopPageProfiling()`
- `StartElementSelection()`
- `StopElementSelection()`
- `SendMessageToFrontend(String message)`
- `EvaluateInFrontendForTesting(String expression)`

## `WebInspectorUIExtensionController` - UI -> WebContent

`WebProcess/Inspector/WebInspectorUIExtensionController.messages.in`

- `RegisterExtension(String extensionID, String extensionBundleIdentifier, String displayName) -> (Expected<void, Inspector::ExtensionError> result)`
- `UnregisterExtension(String extensionID) -> (Expected<void, Inspector::ExtensionError> result)`
- `CreateTabForExtension(String extensionID, String tabName, URL tabIconURL, URL sourceURL) -> (Expected<String, Inspector::ExtensionError> result)`
- `EvaluateScriptForExtension(String extensionID, String scriptSource, std::optional<URL> frameURL, std::optional<URL> contextSecurityOrigin, std::optional<bool> useContentScriptContext) -> (std::span<const uint8_t> resultData, std::optional<WebCore::ExceptionDetails> details, std::optional<Inspector::ExtensionError> error)`
- `ReloadForExtension(String extensionID, std::optional<bool> ignoreCache, std::optional<String> userAgent, std::optional<String> injectedScript) -> (std::optional<Inspector::ExtensionError> error)`
- `ShowExtensionTab(String extensionTabIdentifier) -> (Expected<void, Inspector::ExtensionError> result)`
- `NavigateTabForExtension(String extensionTabIdentifier, URL sourceURL) -> (std::optional<Inspector::ExtensionError> error)`
- `EvaluateScriptInExtensionTab(String extensionTabID, String scriptSource) -> (std::span<const uint8_t> resultData, std::optional<WebCore::ExceptionDetails> details, std::optional<Inspector::ExtensionError> error)`

## `WebNotificationManager` - UI -> WebContent

`WebProcess/Notifications/WebNotificationManager.messages.in`

- `DidShowNotification(WTF::UUID notificationID)`
- `DidClickNotification(WTF::UUID notificationID)`
- `DidCloseNotifications(Vector<WTF::UUID> notificationIDs)`
- `DidUpdateNotificationDecision(String originString, bool allowed)`
- `DidRemoveNotificationDecisions(Vector<String> originStrings)`

## `WebPage` - UI, Networking -> WebContent

`WebProcess/WebPage/WebPage.messages.in`

- `SetInitialFocus(bool forward, bool isKeyboardEventValid, std::optional<WebKit::WebKeyboardEvent> event) -> ()`
- `SetActivityState(OptionSet<WebCore::ActivityState> activityState, WebKit::ActivityStateChangeID activityStateChangeID) -> ()`
- `SetLayerHostingMode(WebKit::LayerHostingMode layerHostingMode)`
- `SetBackgroundColor(std::optional<WebCore::Color> color)`
- `AddConsoleMessage(WebCore::FrameIdentifier frameID, JSC::MessageSource messageSource, JSC::MessageLevel messageLevel, String message, std::optional<WebCore::ResourceLoaderIdentifier> requestID)`
- `EnqueueSecurityPolicyViolationEvent(WebCore::FrameIdentifier frameID, WebCore::SecurityPolicyViolationEventInit eventInit)`
- `SendReportToEndpoints(WebCore::FrameIdentifier frameID, URL baseURL, Vector<String> endpointURIs, Vector<String> endpointTokens, IPC::FormDataReference reportData, WebCore::ViolationReportType reportType)`
- `NotifyReportObservers(WebCore::FrameIdentifier frameID, Ref<WebCore::Report> report)`
- `TestProcessIncomingSyncMessagesWhenWaitingForSyncReply() -> (bool handled)` (AllowedWhenWaitingForSyncReplyDuringUnboundedIPC, sync)
- `SetTopContentInsetFenced(float contentInset, MachSendRight machSendRight)` (if PLATFORM(COCOA))
- `SetTopContentInset(float contentInset)` (if !PLATFORM(COCOA))
- `SetUnderlayColor(WebCore::Color color)`
- `SetUnderPageBackgroundColorOverride(WebCore::Color underPageBackgroundColorOverride)`
- `ViewWillStartLiveResize()`
- `ViewWillEndLiveResize()`
- `ExecuteEditCommandWithCallback(String name, String argument) -> ()`
- `KeyEvent(WebCore::FrameIdentifier frameID, WebKit::WebKeyboardEvent event)`
- `MouseEvent(WebCore::FrameIdentifier frameID, WebKit::WebMouseEvent event, std::optional<Vector<WebKit::SandboxExtensionHandle>> sandboxExtensions)`
- `SetLastKnownMousePosition(WebCore::FrameIdentifier frameID, WebCore::IntPoint eventPoint, WebCore::IntPoint globalPoint)`
- `SetSceneIdentifier(String sceneIdentifier)` (if PLATFORM(IOS_FAMILY))
- `SetViewportConfigurationViewLayoutSize(WebCore::FloatSize size, double scaleFactor, double minimumEffectiveDeviceWidth)` (if PLATFORM(IOS_FAMILY))
- `SetDeviceOrientation(WebCore::IntDegrees deviceOrientation)` (if PLATFORM(IOS_FAMILY))
- `SetOverrideViewportArguments(std::optional<WebCore::ViewportArguments> arguments)` (if PLATFORM(IOS_FAMILY))
- `DynamicViewportSizeUpdate(WebKit::DynamicViewportSizeUpdate target)` (if PLATFORM(IOS_FAMILY))
- `SetScreenIsBeingCaptured(bool captured)` (if PLATFORM(IOS_FAMILY))
- `SetInsertionPointColor(WebCore::Color color)` (if PLATFORM(IOS_FAMILY))
- `AttemptSyntheticClick(WebCore::IntPoint point, OptionSet<WebKit::WebEventModifier> modifiers, WebKit::TransactionID lastLayerTreeTransactionId)` (if PLATFORM(IOS_FAMILY))
- `PotentialTapAtPosition(WebKit::TapIdentifier requestID, WebCore::FloatPoint point, bool shouldRequestMagnificationInformation)` (if PLATFORM(IOS_FAMILY))
- `CommitPotentialTap(OptionSet<WebKit::WebEventModifier> modifiers, WebKit::TransactionID lastLayerTreeTransactionId, WebCore::PointerID pointerId)` (if PLATFORM(IOS_FAMILY))
- `CancelPotentialTap()` (if PLATFORM(IOS_FAMILY))
- `TapHighlightAtPosition(WebKit::TapIdentifier requestID, WebCore::FloatPoint point)` (if PLATFORM(IOS_FAMILY))
- `DidRecognizeLongPress()` (if PLATFORM(IOS_FAMILY))
- `HandleDoubleTapForDoubleClickAtPoint(WebCore::IntPoint point, OptionSet<WebKit::WebEventModifier> modifiers, WebKit::TransactionID lastLayerTreeTransactionId)` (if PLATFORM(IOS_FAMILY))
- `InspectorNodeSearchMovedToPosition(WebCore::FloatPoint point)` (if PLATFORM(IOS_FAMILY))
- `InspectorNodeSearchEndedAtPosition(WebCore::FloatPoint point)` (if PLATFORM(IOS_FAMILY))
- `BlurFocusedElement()` (if PLATFORM(IOS_FAMILY))
- `SelectWithGesture(WebCore::IntPoint point, WebKit::GestureType gestureType, WebKit::GestureRecognizerState gestureState, bool isInteractingWithFocusedElement) -> (WebCore::IntPoint point, WebKit::GestureType gestureType, WebKit::GestureRecognizerState gestureState, OptionSet<WebKit::SelectionFlags> flags)` (if PLATFORM(IOS_FAMILY))
- `UpdateSelectionWithTouches(WebCore::IntPoint point, WebKit::SelectionTouch touches, bool baseIsStart) -> (WebCore::IntPoint point, WebKit::SelectionTouch touch, OptionSet<WebKit::SelectionFlags> selectionFlags)` (if PLATFORM(IOS_FAMILY))
- `SelectWithTwoTouches(WebCore::IntPoint from, WebCore::IntPoint to, WebKit::GestureType gestureType, WebKit::GestureRecognizerState gestureState) -> (WebCore::IntPoint point, WebKit::GestureType gestureType, WebKit::GestureRecognizerState gestureState, OptionSet<WebKit::SelectionFlags> selectionFlags)` (if PLATFORM(IOS_FAMILY))
- `ExtendSelection(WebCore::TextGranularity granularity) -> ()` (if PLATFORM(IOS_FAMILY))
- `SelectWordBackward()` (if PLATFORM(IOS_FAMILY))
- `ExtendSelectionForReplacement() -> ()` (if PLATFORM(IOS_FAMILY))
- `MoveSelectionByOffset(int32_t offset) -> ()` (if PLATFORM(IOS_FAMILY))
- `SelectTextWithGranularityAtPoint(WebCore::IntPoint point, WebCore::TextGranularity granularity, bool isInteractingWithFocusedElement) -> ()` (if PLATFORM(IOS_FAMILY))
- `SelectPositionAtBoundaryWithDirection(WebCore::IntPoint point, WebCore::TextGranularity granularity, WebCore::SelectionDirection direction, bool isInteractingWithFocusedElement) -> ()` (if PLATFORM(IOS_FAMILY))
- `MoveSelectionAtBoundaryWithDirection(WebCore::TextGranularity granularity, WebCore::SelectionDirection direction) -> ()` (if PLATFORM(IOS_FAMILY))
- `SelectPositionAtPoint(WebCore::IntPoint point, bool isInteractingWithFocusedElement) -> ()` (if PLATFORM(IOS_FAMILY))
- `BeginSelectionInDirection(WebCore::SelectionDirection direction) -> (bool endIsMoving)` (if PLATFORM(IOS_FAMILY))
- `UpdateSelectionWithExtentPoint(WebCore::IntPoint point, bool isInteractingWithFocusedElement, WebKit::RespectSelectionAnchor respectSelectionAnchor) -> (bool endIsMoving)` (if PLATFORM(IOS_FAMILY))
- `UpdateSelectionWithExtentPointAndBoundary(WebCore::IntPoint point, WebCore::TextGranularity granularity, bool isInteractingWithFocusedElement, WebKit::TextInteractionSource sources) -> (bool endIsMoving)` (if PLATFORM(IOS_FAMILY))
- `DidReleaseAllTouchPoints()` (if PLATFORM(IOS_FAMILY))
- `ClearSelectionAfterTappingSelectionHighlightIfNeeded(WebCore::FloatPoint location)` (if PLATFORM(IOS_FAMILY))
- `RequestRVItemInCurrentSelectedRange() -> (WebKit::RevealItem item)` (if (PLATFORM(IOS_FAMILY) && ENABLE(REVEAL)))
- `PrepareSelectionForContextMenuWithLocationInView(WebCore::IntPoint point) -> (bool shouldShowMenu, WebKit::RevealItem item)` (if (PLATFORM(IOS_FAMILY) && ENABLE(REVEAL)))
- `WillInsertFinalDictationResult()` (if PLATFORM(IOS_FAMILY))
- `DidInsertFinalDictationResult()` (if PLATFORM(IOS_FAMILY))
- `ReplaceDictatedText(String oldText, String newText)` (if PLATFORM(IOS_FAMILY))
- `ReplaceSelectedText(String oldText, String newText)` (if PLATFORM(IOS_FAMILY))
- `RequestAutocorrectionData(String textForAutocorrection) -> (WebKit::WebAutocorrectionData data)` (if PLATFORM(IOS_FAMILY))
- `ApplyAutocorrection(String correction, String originalText, bool isCandidate) -> (String string)` (if PLATFORM(IOS_FAMILY))
- `SyncApplyAutocorrection(String correction, String originalText, bool isCandidate) -> (bool autocorrectionApplied)` (sync, if PLATFORM(IOS_FAMILY))
- `HandleAutocorrectionContextRequest()` (if PLATFORM(IOS_FAMILY))
- `RequestEvasionRectsAboveSelection() -> (Vector<WebCore::FloatRect> rects)` (if PLATFORM(IOS_FAMILY))
- `RequestPositionInformation(WebKit::InteractionInformationRequest request)` (if PLATFORM(IOS_FAMILY))
- `StartInteractionWithElementContextOrPosition(std::optional<WebCore::ElementContext> elementContext, WebCore::IntPoint point)` (if PLATFORM(IOS_FAMILY))
- `StopInteraction()` (if PLATFORM(IOS_FAMILY))
- `PerformActionOnElement(uint32_t action, String authenticationToken) -> ()` (if PLATFORM(IOS_FAMILY))
- `PerformActionOnElements(uint32_t action, Vector<WebCore::ElementContext> elements)` (if PLATFORM(IOS_FAMILY))
- `FocusNextFocusedElement(bool isForward) -> ()` (if PLATFORM(IOS_FAMILY))
- `AutofillLoginCredentials(String username, String password)` (if PLATFORM(IOS_FAMILY))
- `SetFocusedElementValue(WebCore::ElementContext context, String value)` (if PLATFORM(IOS_FAMILY))
- `SetFocusedElementSelectedIndex(WebCore::ElementContext context, uint32_t index, bool allowMultipleSelection)` (if PLATFORM(IOS_FAMILY))
- `ApplicationWillResignActive()` (if PLATFORM(IOS_FAMILY))
- `ApplicationDidEnterBackground(bool isSuspendedUnderLock)` (if PLATFORM(IOS_FAMILY))
- `ApplicationDidFinishSnapshottingAfterEnteringBackground()` (if PLATFORM(IOS_FAMILY))
- `ApplicationWillEnterForeground(bool isSuspendedUnderLock)` (if PLATFORM(IOS_FAMILY))
- `ApplicationDidBecomeActive()` (if PLATFORM(IOS_FAMILY))
- `ApplicationDidEnterBackgroundForMedia(bool isSuspendedUnderLock)` (if PLATFORM(IOS_FAMILY))
- `ApplicationWillEnterForegroundForMedia(bool isSuspendedUnderLock)` (if PLATFORM(IOS_FAMILY))
- `ContentSizeCategoryDidChange(String contentSizeCategory)` (if PLATFORM(IOS_FAMILY))
- `GetSelectionContext() -> (String selectedText, String textBefore, String textAfter)` (if PLATFORM(IOS_FAMILY))
- `SetAllowsMediaDocumentInlinePlayback(bool allows)` (if PLATFORM(IOS_FAMILY))
- `HandleTwoFingerTapAtPoint(WebCore::IntPoint point, OptionSet<WebKit::WebEventModifier> modifiers, WebKit::TapIdentifier requestID)` (if PLATFORM(IOS_FAMILY))
- `SetForceAlwaysUserScalable(bool userScalable)` (if PLATFORM(IOS_FAMILY))
- `GetRectsForGranularityWithSelectionOffset(WebCore::TextGranularity granularity, int32_t offset) -> (Vector<WebCore::SelectionGeometry> rect)` (if PLATFORM(IOS_FAMILY))
- `GetRectsAtSelectionOffsetWithText(int32_t offset, String text) -> (Vector<WebCore::SelectionGeometry> rect)` (if PLATFORM(IOS_FAMILY))
- `StoreSelectionForAccessibility(bool shouldStore)` (if PLATFORM(IOS_FAMILY))
- `StartAutoscrollAtPosition(WebCore::FloatPoint positionInWindow)` (if PLATFORM(IOS_FAMILY))
- `CancelAutoscroll()` (if PLATFORM(IOS_FAMILY))
- `RequestFocusedElementInformation() -> (std::optional<WebKit::FocusedElementInformation> info)` (if PLATFORM(IOS_FAMILY))
- `HardwareKeyboardAvailabilityChanged(WebKit::HardwareKeyboardState state)` (if PLATFORM(IOS_FAMILY))
- `SetIsShowingInputViewForFocusedElement(bool showingInputView)` (if PLATFORM(IOS_FAMILY))
- `UpdateSelectionWithDelta(int64_t locationDelta, int64_t lengthDelta) -> ()` (if PLATFORM(IOS_FAMILY))
- `RequestDocumentEditingContext(WebKit::DocumentEditingContextRequest request) -> (WebKit::DocumentEditingContext response)` (if PLATFORM(IOS_FAMILY))
- `GenerateSyntheticEditingCommand(WebKit::SyntheticEditingCommandType command)` (if PLATFORM(IOS_FAMILY))
- `SetShouldRevealCurrentSelectionAfterInsertion(bool shouldRevealCurrentSelectionAfterInsertion)` (if PLATFORM(IOS_FAMILY))
- `TextInputContextsInRect(WebCore::FloatRect rect) -> (Vector<WebCore::ElementContext> contexts)` (if PLATFORM(IOS_FAMILY))
- `FocusTextInputContextAndPlaceCaret(WebCore::ElementContext context, WebCore::IntPoint point) -> (bool success)` (if PLATFORM(IOS_FAMILY))
- `ClearServiceWorkerEntitlementOverride() -> ()` (if PLATFORM(IOS_FAMILY))
- `RequestImageBitmap(WebCore::ElementContext elementContext) -> (std::optional<WebCore::ShareableBitmapHandle> image, String sourceMIMEType)`
- `SetControlledByAutomation(bool controlled)`
- `ConnectInspector(String targetId, Inspector::FrontendChannel::ConnectionType connectionType)`
- `DisconnectInspector(String targetId)`
- `SendMessageToTargetBackend(String targetId, String message)`
- `SetIndicating(bool indicating)` (if ENABLE(REMOTE_INSPECTOR))
- `DidBeginTouchPoint(WebCore::FloatPoint locationInRootView)` (if ENABLE(IOS_TOUCH_EVENTS))
- `TouchEvent(WebKit::WebTouchEvent event) -> (std::optional<WebKit::WebEventType> eventType, bool handled)` (if !ENABLE(IOS_TOUCH_EVENTS) && ENABLE(TOUCH_EVENTS))
- `CancelPointer(WebCore::PointerID pointerId, WebCore::IntPoint documentPoint)`
- `TouchWithIdentifierWasRemoved(WebCore::PointerID pointerId)`
- `DidEndColorPicker()`
- `DidChooseColor(WebCore::Color color)`
- `DidSelectDataListOption(String selectedOption)`
- `DidCloseSuggestions()`
- `DidChooseDate(String date)`
- `DidEndDateTimePicker()`
- `ScrollBy(WebCore::ScrollDirection scrollDirection, WebCore::ScrollGranularity scrollGranularity)`
- `CenterSelectionInVisibleArea()`
- `GoToBackForwardItem(WebKit::GoToBackForwardItemParameters parameters)`
- `GoToBackForwardItemWaitingForProcessLaunch(WebKit::GoToBackForwardItemParameters parameters, WebKit::WebPageProxyIdentifier pageID)`
- `TryRestoreScrollPosition()`
- `LoadURLInFrame(URL url, String referrer, WebCore::FrameIdentifier frameID)`
- `LoadDataInFrame(std::span<const uint8_t> data, String MIMEType, String encodingName, URL baseURL, WebCore::FrameIdentifier frameID)`
- `LoadRequest(WebKit::LoadParameters loadParameters)`
- `CreateProvisionalFrame(WebKit::ProvisionalFrameCreationParameters creationParameters, WebCore::FrameIdentifier frameID)`
- `DestroyProvisionalFrame(WebCore::FrameIdentifier frameID)`
- `LoadDidCommitInAnotherProcess(WebCore::FrameIdentifier frameID, std::optional<WebCore::LayerHostingContextIdentifier> layerHostingContextIdentifier)`
- `LoadRequestWaitingForProcessLaunch(WebKit::LoadParameters loadParameters, URL resourceDirectoryURL, WebKit::WebPageProxyIdentifier pageID, bool checkAssumedReadAccessToResourceURL)`
- `LoadData(WebKit::LoadParameters loadParameters)`
- `LoadSimulatedRequestAndResponse(WebKit::LoadParameters loadParameters, WebCore::ResourceResponse simulatedResponse)`
- `LoadAlternateHTML(WebKit::LoadParameters loadParameters)`
- `CreateRemoteSubframe(WebCore::FrameIdentifier parentID, WebCore::FrameIdentifier newChildID, String frameName)`
- `GetFrameInfo(WebCore::FrameIdentifier frameID) -> (std::optional<WebKit::FrameInfoData> data)`
- `GetFrameTree() -> (WebKit::FrameTreeNodeData data)`
- `DidFinishLoadInAnotherProcess(WebCore::FrameIdentifier frameID)`
- `FrameWasRemovedInAnotherProcess(WebCore::FrameIdentifier frameID)`
- `ProcessSyncDataChangedInAnotherProcess(WebCore::ProcessSyncData processSyncData)`
- `TopDocumentSyncDataChangedInAnotherProcess(Ref<WebCore::DocumentSyncData> documentSyncData)`
- `NavigateToPDFLinkWithSimulatedClick(String url, WebCore::IntPoint documentPoint, WebCore::IntPoint screenPoint)`
- `GetPDFFirstPageSize(WebCore::FrameIdentifier frameID) -> (WebCore::FloatSize size)`
- `Reload(WebCore::NavigationIdentifier navigationID, OptionSet<WebCore::ReloadOption> reloadOptions, WebKit::SandboxExtensionHandle sandboxExtensionHandle)`
- `StopLoading()`
- `StopLoadingDueToProcessSwap()`
- `SetCurrentHistoryItemForReattach(Ref<WebKit::FrameState> frameState)`
- `DidRemoveBackForwardItem(WebCore::BackForwardItemIdentifier backForwardItemID)`
- `UpdateWebsitePolicies(WebKit::WebsitePoliciesData websitePolicies)`
- `ClearSelection()`
- `RestoreSelectionInFocusedEditableElement()`
- `GetContentsAsString(WebKit::ContentAsStringIncludesChildFrames inChildFrames) -> (String string)`
- `GetContentsAsAttributedString() -> (WebCore::AttributedString result)` (if PLATFORM(COCOA))
- `GetContentsAsMHTMLData() -> (IPC::SharedBufferReference data)` (if ENABLE(MHTML))
- `GetMainResourceDataOfFrame(WebCore::FrameIdentifier frameID) -> (std::optional<IPC::SharedBufferReference> buffer)`
- `GetResourceDataFromFrame(WebCore::FrameIdentifier frameID, String resourceURL) -> (std::optional<IPC::SharedBufferReference> buffer)`
- `GetRenderTreeExternalRepresentation() -> (String string)`
- `GetSelectionOrContentsAsString() -> (String string)`
- `GetSelectionAsWebArchiveData() -> (std::optional<IPC::SharedBufferReference> data)`
- `GetSourceForFrame(WebCore::FrameIdentifier frameID) -> (String string)`
- `GetWebArchiveOfFrame(std::optional<WebCore::FrameIdentifier> frameID) -> (std::optional<IPC::SharedBufferReference> dataReference)`
- `GetWebArchiveOfFrameWithFileName(WebCore::FrameIdentifier frameID, Vector<WebCore::MarkupExclusionRule> markupExclusionRules, String fileName) -> (std::optional<IPC::SharedBufferReference> dataReference)`
- `RunJavaScriptInFrameInScriptWorld(WebCore::RunJavaScriptParameters parameters, std::optional<WebCore::FrameIdentifier> frameID, WebKit::ContentWorldData world) -> (std::span<const uint8_t> resultData, std::optional<WebCore::ExceptionDetails> details)`
- `GetAccessibilityTreeData() -> (std::optional<IPC::SharedBufferReference> dataReference)`
- `UpdateRenderingWithForcedRepaint() -> ()`
- `SelectAll()`
- `ScheduleFullEditorStateUpdate()`
- `PerformDictionaryLookupAtLocation(WebCore::FloatPoint point)` (if PLATFORM(COCOA))
- `DetectDataInAllFrames(OptionSet<WebCore::DataDetectorType> types) -> (WebKit::DataDetectionResult result)` (if ENABLE(DATA_DETECTION))
- `RemoveDataDetectedLinks() -> (WebKit::DataDetectionResult result)` (if ENABLE(DATA_DETECTION))
- `ChangeFont(WebCore::FontChanges changes)`
- `ChangeFontAttributes(WebCore::FontAttributeChanges changes)`
- `PreferencesDidChange(WebKit::WebPreferencesStore store, std::optional<uint64_t> sharedPreferencesVersion)`
- `PreferencesDidChangeDuringDOMPrintOperation(WebKit::WebPreferencesStore store, std::optional<uint64_t> sharedPreferencesVersion)` (AllowedWhenWaitingForSyncReplyDuringUnboundedIPC)
- `SetUserAgent(String userAgent)`
- `SetHasCustomUserAgent(bool hasCustomUserAgent)`
- `SetCustomTextEncodingName(String encodingName)`
- `SuspendActiveDOMObjectsAndAnimations()`
- `ResumeActiveDOMObjectsAndAnimations()`
- `Suspend() -> (bool success)`
- `Resume() -> (bool success)`
- `Close()`
- `TryClose() -> (bool shouldClose)`
- `SetEditable(bool editable)`
- `ValidateCommand(String name) -> (bool isEnabled, int32_t state)`
- `ExecuteEditCommand(String name, String argument)`
- `IncreaseListLevel()`
- `DecreaseListLevel()`
- `ChangeListType()`
- `SetBaseWritingDirection(WebCore::WritingDirection direction)`
- `SetNeedsFontAttributes(bool needsFontAttributes)`
- `RequestFontAttributesAtSelectionStart() -> (WebCore::FontAttributes attributes)`
- `DidRemoveEditCommand(uint64_t commandID)`
- `ReapplyEditCommand(uint64_t commandID)` (AllowedWhenWaitingForSyncReply)
- `UnapplyEditCommand(uint64_t commandID)` (AllowedWhenWaitingForSyncReply)
- `DidSetPageZoomFactor(double zoomFactor)`
- `DidSetTextZoomFactor(double zoomFactor)`
- `WindowScreenDidChange(uint32_t displayID, std::optional<unsigned> nominalFramesPerSecond)`
- `AccessibilitySettingsDidChange()`
- `DidScalePage(double scale, WebCore::IntPoint origin)`
- `DidScalePageInViewCoordinates(double scale, WebCore::IntPoint origin)`
- `DidScalePageRelativeToScrollPosition(double scale, WebCore::IntPoint origin)`
- `DidScaleView(double scale)`
- `SetPluginScaleFactor(double scale, WebCore::IntPoint origin)` (if ENABLE(PDF_PLUGIN))
- `SetUseFixedLayout(bool fixed)`
- `SetFixedLayoutSize(WebCore::IntSize size)`
- `SetDefaultUnobscuredSize(WebCore::FloatSize size)`
- `SetMinimumUnobscuredSize(WebCore::FloatSize size)`
- `SetMaximumUnobscuredSize(WebCore::FloatSize size)`
- `ListenForLayoutMilestones(OptionSet<WebCore::LayoutMilestone> layoutMilestones)`
- `SetSuppressScrollbarAnimations(bool suppressAnimations)`
- `SetEnableVerticalRubberBanding(bool enableVerticalRubberBanding)`
- `SetEnableHorizontalRubberBanding(bool enableHorizontalRubberBanding)`
- `SetBackgroundExtendsBeyondPage(bool backgroundExtendsBeyondPage)`
- `SetPaginationMode(WebCore::PaginationMode mode)`
- `SetPaginationBehavesLikeColumns(bool behavesLikeColumns)`
- `SetPageLength(double pageLength)`
- `SetGapBetweenPages(double gap)`
- `PostInjectedBundleMessage(String messageName, WebKit::UserData messageBody)`
- `FindString(String string, OptionSet<WebKit::FindOptions> findOptions, unsigned maxMatchCount) -> (std::optional<WebCore::FrameIdentifier> frameID, Vector<WebCore::IntRect> matchRects, uint32_t matchCount, int32_t matchIndex, bool didWrap)`
- `FindStringIncludingImages(String string, OptionSet<WebKit::FindOptions> findOptions, unsigned maxMatchCount) -> (std::optional<WebCore::FrameIdentifier> frameID, Vector<WebCore::IntRect> matchRects, uint32_t matchCount, int32_t matchIndex, bool didWrap)` (if ENABLE(IMAGE_ANALYSIS))
- `FindStringMatches(String string, OptionSet<WebKit::FindOptions> findOptions, unsigned maxMatchCount) -> (Vector<Vector<WebCore::IntRect>> matches, int32_t firstIndexAfterSelection)`
- `GetImageForFindMatch(uint32_t matchIndex)`
- `SelectFindMatch(uint32_t matchIndex)`
- `IndicateFindMatch(uint32_t matchIndex)`
- `HideFindUI()`
- `CountStringMatches(String string, OptionSet<WebKit::FindOptions> findOptions, unsigned maxMatchCount) -> (uint32_t matchCount)`
- `ReplaceMatches(Vector<uint32_t> matchIndices, String replacementText, bool selectionOnly) -> (uint64_t numberOfReplacements)`
- `FindRectsForStringMatches(String string, OptionSet<WebKit::FindOptions> findOptions, unsigned maxMatchCount) -> (Vector<WebCore::FloatRect> matches)`
- `HideFindIndicator()`
- `FindTextRangesForStringMatches(String string, OptionSet<WebKit::FindOptions> findOptions, unsigned maxMatchCount) -> (Vector<WebKit::WebFoundTextRange> ranges)`
- `ReplaceFoundTextRangeWithString(WebKit::WebFoundTextRange range, String string)`
- `DecorateTextRangeWithStyle(WebKit::WebFoundTextRange range, WebKit::FindDecorationStyle style)`
- `ScrollTextRangeToVisible(WebKit::WebFoundTextRange range)`
- `ClearAllDecoratedFoundText()`
- `DidBeginTextSearchOperation()`
- `RequestRectForFoundTextRange(WebKit::WebFoundTextRange range) -> (WebCore::FloatRect rect)`
- `AddLayerForFindOverlay() -> (std::optional<WebCore::PlatformLayerIdentifier> findLayerID)`
- `RemoveLayerForFindOverlay() -> ()`
- `PerformDragControllerAction(WebKit::DragControllerAction action, WebCore::IntPoint clientPosition, WebCore::IntPoint globalPosition, OptionSet<WebCore::DragOperation> draggingSourceOperationMask, WebCore::SelectionData selection, OptionSet<WebCore::DragApplicationFlags> flags) -> (std::optional<WebCore::DragOperation> dragOperation, WebCore::DragHandlingMethod dragHandlingMethod, bool mouseIsOverFileInput, unsigned numberOfItemsToBeAccepted, WebCore::IntRect insertionRect, WebCore::IntRect editableElementRect, std::optional<WebCore::RemoteUserInputEventData> remoteUserInputEventData)` (if PLATFORM(GTK) && ENABLE(DRAG_SUPPORT))
- `PerformDragControllerAction(std::optional<WebCore::FrameIdentifier> frameID, WebKit::DragControllerAction action, WebCore::DragData dragData) -> (std::optional<WebCore::DragOperation> dragOperation, WebCore::DragHandlingMethod dragHandlingMethod, bool mouseIsOverFileInput, unsigned numberOfItemsToBeAccepted, WebCore::IntRect insertionRect, WebCore::IntRect editableElementRect, std::optional<WebCore::RemoteUserInputEventData> remoteUserInputEventData)` (if !PLATFORM(GTK) && ENABLE(DRAG_SUPPORT))
- `PerformDragOperation(WebCore::DragData dragData, WebKit::SandboxExtensionHandle sandboxExtensionHandle, Vector<WebKit::SandboxExtensionHandle> sandboxExtensionsForUpload) -> (bool handled)` (if !PLATFORM(GTK) && ENABLE(DRAG_SUPPORT))
- `DidStartDrag()` (if ENABLE(DRAG_SUPPORT))
- `DragEnded(std::optional<WebCore::FrameIdentifier> frameID, WebCore::IntPoint clientPosition, WebCore::IntPoint globalPosition, OptionSet<WebCore::DragOperation> dragOperationMask) -> (std::optional<WebCore::RemoteUserInputEventData> remoteUserInputEventData)` (if ENABLE(DRAG_SUPPORT))
- `DragCancelled()` (if ENABLE(DRAG_SUPPORT))
- `RequestDragStart(WebCore::IntPoint clientPosition, WebCore::IntPoint globalPosition, OptionSet<WebCore::DragSourceAction> allowedActionsMask)` (if PLATFORM(IOS_FAMILY) && ENABLE(DRAG_SUPPORT))
- `RequestAdditionalItemsForDragSession(WebCore::IntPoint clientPosition, WebCore::IntPoint globalPosition, OptionSet<WebCore::DragSourceAction> allowedActionsMask)` (if PLATFORM(IOS_FAMILY) && ENABLE(DRAG_SUPPORT))
- `InsertDroppedImagePlaceholders(Vector<WebCore::IntSize> imageSize) -> (Vector<WebCore::IntRect> dropPreviewRects, std::optional<WebCore::TextIndicatorData> textIndicator)` (if PLATFORM(IOS_FAMILY) && ENABLE(DRAG_SUPPORT))
- `DidConcludeDrop()` (if PLATFORM(IOS_FAMILY) && ENABLE(DRAG_SUPPORT))
- `InsertTextPlaceholder(WebCore::IntSize size) -> (std::optional<WebCore::ElementContext> placeholder)` (if PLATFORM(COCOA))
- `RemoveTextPlaceholder(WebCore::ElementContext placeholder) -> ()` (if PLATFORM(COCOA))
- `DidChangeSelectedIndexForActivePopupMenu(int32_t newIndex)`
- `SetTextForActivePopupMenu(int32_t index)`
- `FailedToShowPopupMenu()` (if PLATFORM(GTK))
- `DidDismissContextMenu()` (if ENABLE(CONTEXT_MENUS))
- `DidSelectItemFromActiveContextMenu(WebKit::WebContextMenuItemData menuItem)` (if ENABLE(CONTEXT_MENUS))
- `ContextMenuForKeyEvent()` (if ENABLE(CONTEXT_MENUS))
- `DidChooseFilesForOpenPanelWithDisplayStringAndIcon(Vector<String> fileURLs, String displayString, std::span<const uint8_t> iconData)` (if PLATFORM(IOS_FAMILY))
- `DidChooseFilesForOpenPanel(Vector<String> fileURLs, Vector<String> replacementURLs)`
- `DidCancelForOpenPanel()`
- `ExtendSandboxForFilesFromOpenPanel(Vector<WebKit::SandboxExtensionHandle> sandboxExtensions)` (if ENABLE(SANDBOX_EXTENSIONS))
- `AdvanceToNextMisspelling(bool startBeforeSelection)`
- `ChangeSpellingToWord(String word)`
- `DidFinishCheckingText(WebKit::TextCheckerRequestID requestID, Vector<WebCore::TextCheckingResult> result)`
- `DidCancelCheckingText(WebKit::TextCheckerRequestID requestID)`
- `UppercaseWord(WebCore::FrameIdentifier frameID)` (if USE(APPKIT))
- `LowercaseWord(WebCore::FrameIdentifier frameID)` (if USE(APPKIT))
- `CapitalizeWord(WebCore::FrameIdentifier frameID)` (if USE(APPKIT))
- `SetSmartInsertDeleteEnabled(bool isSmartInsertDeleteEnabled)` (if PLATFORM(COCOA))
- `DidReceiveGeolocationPermissionDecision(WebKit::GeolocationIdentifier geolocationID, String authorizationToken)` (if ENABLE(GEOLOCATION))
- `UserMediaAccessWasGranted(WebCore::UserMediaRequestIdentifier userMediaID, WebCore::CaptureDevice audioDevice, WebCore::CaptureDevice videoDevice, WebCore::MediaDeviceHashSalts mediaDeviceIdentifierHashSalts, Vector<WebKit::SandboxExtensionHandle> sandboxExtensionHandles) -> ()` (if ENABLE(MEDIA_STREAM))
- `UserMediaAccessWasDenied(WebCore::UserMediaRequestIdentifier userMediaID, uint64_t reason, String messsage, WebCore::MediaConstraintType invalidConstraint)` (if ENABLE(MEDIA_STREAM))
- `CaptureDevicesChanged()` (if ENABLE(MEDIA_STREAM))
- `VoiceActivityDetected()` (if ENABLE(MEDIA_STREAM))
- `SetOrientationForMediaCapture(uint64_t rotation)` (if (ENABLE(MEDIA_STREAM) && USE(GSTREAMER)))
- `SetMockCaptureDevicesInterrupted(bool isCameraInterrupted, bool isMicrophoneInterrupted)` (if (ENABLE(MEDIA_STREAM) && USE(GSTREAMER)))
- `MediaKeySystemWasGranted(WebCore::MediaKeySystemRequestIdentifier mediaKeySystemID)` (if ENABLE(ENCRYPTED_MEDIA))
- `MediaKeySystemWasDenied(WebCore::MediaKeySystemRequestIdentifier mediaKeySystemID, String message)` (if ENABLE(ENCRYPTED_MEDIA))
- `RequestMediaPlaybackState() -> (WebKit::MediaPlaybackState state)`
- `PauseAllMediaPlayback() -> ()`
- `SuspendAllMediaPlayback() -> ()`
- `ResumeAllMediaPlayback() -> ()`
- `SwipeAnimationDidStart()`
- `SwipeAnimationDidEnd()`
- `BeginPrinting(WebCore::FrameIdentifier frameID, WebKit::PrintInfo printInfo)`
- `BeginPrintingDuringDOMPrintOperation(WebCore::FrameIdentifier frameID, WebKit::PrintInfo printInfo)` (AllowedWhenWaitingForSyncReplyDuringUnboundedIPC)
- `EndPrinting() -> ()`
- `EndPrintingDuringDOMPrintOperation() -> ()` (AllowedWhenWaitingForSyncReplyDuringUnboundedIPC)
- `ComputePagesForPrinting(WebCore::FrameIdentifier frameID, WebKit::PrintInfo printInfo) -> (Vector<WebCore::IntRect> pageRects, double totalScaleFactorForPrinting, WebCore::FloatBoxExtent computedPageMargin)`
- `ComputePagesForPrintingDuringDOMPrintOperation(WebCore::FrameIdentifier frameID, WebKit::PrintInfo printInfo) -> (Vector<WebCore::IntRect> pageRects, double totalScaleFactorForPrinting, WebCore::FloatBoxExtent computedPageMargin)` (AllowedWhenWaitingForSyncReplyDuringUnboundedIPC)
- `DrawRectToImage(WebCore::FrameIdentifier frameID, WebKit::PrintInfo printInfo, WebCore::IntRect rect, WebCore::IntSize imageSize) -> (std::optional<WebCore::ShareableBitmapHandle> image)` (ReplyCanDispatchOutOfOrder, if PLATFORM(COCOA))
- `DrawRectToImageDuringDOMPrintOperation(WebCore::FrameIdentifier frameID, WebKit::PrintInfo printInfo, WebCore::IntRect rect, WebCore::IntSize imageSize) -> (std::optional<WebCore::ShareableBitmapHandle> image)` (AllowedWhenWaitingForSyncReplyDuringUnboundedIPC, if PLATFORM(COCOA))
- `DrawPagesToPDF(WebCore::FrameIdentifier frameID, WebKit::PrintInfo printInfo, uint32_t first, uint32_t count) -> (RefPtr<WebCore::SharedBuffer> data)` (if PLATFORM(COCOA))
- `DrawPagesToPDFDuringDOMPrintOperation(WebCore::FrameIdentifier frameID, WebKit::PrintInfo printInfo, uint32_t first, uint32_t count) -> (RefPtr<WebCore::SharedBuffer> data)` (AllowedWhenWaitingForSyncReplyDuringUnboundedIPC, if PLATFORM(COCOA))
- `ComputePagesForPrintingiOS(WebCore::FrameIdentifier frameID, WebKit::PrintInfo printInfo) -> (size_t pageCount)` (sync, if (PLATFORM(COCOA) && PLATFORM(IOS_FAMILY)))
- `DrawToPDFiOS(WebCore::FrameIdentifier frameID, WebKit::PrintInfo printInfo, size_t pageCount) -> (RefPtr<WebCore::SharedBuffer> data)` (ReplyCanDispatchOutOfOrder, if (PLATFORM(COCOA) && PLATFORM(IOS_FAMILY)))
- `DrawToImage(WebCore::FrameIdentifier frameID, WebKit::PrintInfo printInfo) -> (std::optional<WebCore::ShareableBitmapHandle> data)` (ReplyCanDispatchOutOfOrder, if (PLATFORM(COCOA) && PLATFORM(IOS_FAMILY)))
- `DrawToPDF(WebCore::FrameIdentifier frameID, std::optional<WebCore::FloatRect> rect, bool allowTransparentBackground) -> (RefPtr<WebCore::SharedBuffer> data)` (if PLATFORM(COCOA))
- `DrawRemoteToPDF(WebCore::FrameIdentifier frameID, std::optional<WebCore::FloatRect> rect, bool allowTransparentBackground, WebCore::SnapshotIdentifier snapshotIdentifier)` (if PLATFORM(COCOA))
- `DrawPagesForPrinting(WebCore::FrameIdentifier frameID, WebKit::PrintInfo printInfo) -> (std::optional<WebCore::SharedMemory::Handle> data, WebCore::ResourceError error)` (if PLATFORM(GTK))
- `DrawPagesForPrintingDuringDOMPrintOperation(WebCore::FrameIdentifier frameID, WebKit::PrintInfo printInfo) -> (std::optional<WebCore::SharedMemory::Handle> data, WebCore::ResourceError error)` (AllowedWhenWaitingForSyncReplyDuringUnboundedIPC, if PLATFORM(GTK))
- `SetMediaVolume(float volume)`
- `SetMuted(OptionSet<WebCore::MediaProducerMutedState> muted) -> ()`
- `SetMayStartMediaWhenInWindow(bool mayStartMedia)`
- `StopMediaCapture(WebCore::MediaProducerMediaCaptureKind kind) -> ()`
- `SetCanRunBeforeUnloadConfirmPanel(bool canRunBeforeUnloadConfirmPanel)`
- `SetCanRunModal(bool canRunModal)`
- `CancelComposition(String text)` (if PLATFORM(GTK) || PLATFORM(WPE))
- `DeleteSurrounding(int64_t offset, unsigned characterCount)` (if PLATFORM(GTK) || PLATFORM(WPE))
- `CollapseSelectionInFrame(WebCore::FrameIdentifier frameID)` (if PLATFORM(GTK))
- `CopyLinkWithHighlight()`
- `BindRemoteAccessibilityFrames(int processIdentifier, WebCore::FrameIdentifier frameID, Vector<uint8_t> dataToken) -> (Vector<uint8_t> token, int processIdentifier)` (sync)
- `UpdateRemotePageAccessibilityOffset(WebCore::FrameIdentifier frameID, WebCore::IntPoint offset)`
- `ResolveAccessibilityHitTestForTesting(WebCore::IntPoint point) -> (String result)`
- `EnableAccessibility()`
- `WindowAndViewFramesChanged(WebKit::ViewWindowCoordinates coordinates)` (if PLATFORM(COCOA))
- `SetMainFrameIsScrollable(bool isScrollable)` (if PLATFORM(COCOA))
- `RegisterUIProcessAccessibilityTokens(std::span<const uint8_t> elementToken, std::span<const uint8_t> windowToken)` (if PLATFORM(COCOA))
- `GetStringSelectionForPasteboard() -> (String stringValue)` (sync, if PLATFORM(COCOA))
- `GetDataSelectionForPasteboard(String pasteboardType) -> (RefPtr<WebCore::SharedBuffer> buffer)` (sync, if PLATFORM(COCOA))
- `ReadSelectionFromPasteboard(String pasteboardName) -> (bool result)` (sync, if PLATFORM(COCOA))
- `ReplaceSelectionWithPasteboardData(Vector<String> types, std::span<const uint8_t> data)` (if PLATFORM(COCOA))
- `InsertMultiRepresentationHEIC(std::span<const uint8_t> data, String altText)` (if (PLATFORM(COCOA) && ENABLE(MULTI_REPRESENTATION_HEIC)))
- `ShouldDelayWindowOrderingEvent(WebKit::WebMouseEvent event) -> (bool result)` (sync, if PLATFORM(COCOA))
- `SetTextAsync(String text)` (if PLATFORM(COCOA))
- `InsertTextAsync(String text, WebKit::EditingRange replacementRange, WebKit::InsertTextOptions options)` (if PLATFORM(COCOA))
- `InsertDictatedTextAsync(String text, WebKit::EditingRange replacementRange, Vector<WebCore::DictationAlternative> dictationAlternatives, WebKit::InsertTextOptions options)` (if PLATFORM(COCOA))
- `AddDictationAlternative(String text, WebCore::DictationContext context) -> (bool success)` (Async, if PLATFORM(COCOA))
- `DictationAlternativesAtSelection() -> (Vector<WebCore::DictationContext> contexts)` (Async, if PLATFORM(COCOA))
- `ClearDictationAlternatives(Vector<WebCore::DictationContext> contexts)` (if PLATFORM(COCOA))
- `HasMarkedText() -> (bool hasMarkedText)` (if PLATFORM(COCOA))
- `GetMarkedRangeAsync() -> (WebKit::EditingRange range)` (if PLATFORM(COCOA))
- `GetSelectedRangeAsync() -> (WebKit::EditingRange range)` (if PLATFORM(COCOA))
- `CharacterIndexForPointAsync(WebCore::IntPoint point) -> (uint64_t location)` (if PLATFORM(COCOA))
- `FirstRectForCharacterRangeAsync(WebKit::EditingRange range) -> (WebCore::IntRect rect, WebKit::EditingRange actualRange)` (if PLATFORM(COCOA))
- `SetCompositionAsync(String text, Vector<WebCore::CompositionUnderline> underlines, Vector<WebCore::CompositionHighlight> highlights, HashMap<String, Vector<WebCore::CharacterRange>> annotations, WebKit::EditingRange selectionRange, WebKit::EditingRange replacementRange)` (if PLATFORM(COCOA))
- `SetWritingSuggestion(String text, WebKit::EditingRange selectionRange)` (if PLATFORM(COCOA))
- `ConfirmCompositionAsync()` (if PLATFORM(COCOA))
- `AttributedSubstringForCharacterRangeAsync(WebKit::EditingRange range) -> (WebCore::AttributedString string, WebKit::EditingRange range)` (if PLATFORM(MAC))
- `RequestAcceptsFirstMouse(int eventNumber, WebKit::WebMouseEvent event)` (AllowedWhenWaitingForSyncReplyDuringUnboundedIPC, if PLATFORM(MAC))
- `SetCaretAnimatorType(WebCore::CaretAnimatorType caretType)` (if PLATFORM(MAC))
- `SetCaretBlinkingSuspended(bool blinkSuspended)` (if PLATFORM(MAC))
- `ReplaceImageForRemoveBackground(WebCore::ElementContext context, Vector<String> types, std::span<const uint8_t> data)` (if ENABLE(IMAGE_ANALYSIS_ENHANCEMENTS))
- `ShouldAllowRemoveBackground(WebCore::ElementContext context) -> (bool result)` (if ENABLE(IMAGE_ANALYSIS_ENHANCEMENTS))
- `SetAlwaysShowsHorizontalScroller(bool alwaysShowsHorizontalScroller)`
- `SetAlwaysShowsVerticalScroller(bool alwaysShowsVerticalScroller)`
- `SetMinimumSizeForAutoLayout(WebCore::IntSize size)`
- `SetSizeToContentAutoSizeMaximumSize(WebCore::IntSize size)`
- `SetAutoSizingShouldExpandToViewHeight(bool shouldExpand)`
- `SetViewportSizeForCSSViewportUnits(std::optional<WebCore::FloatSize> viewportSize)`
- `HandleAlternativeTextUIResult(String result)` (if PLATFORM(COCOA))
- `WillStartUserTriggeredZooming()` (if PLATFORM(IOS_FAMILY))
- `DidEndUserTriggeredZooming()` (if PLATFORM(IOS_FAMILY))
- `SetScrollPinningBehavior(WebCore::ScrollPinningBehavior pinning)`
- `SetScrollbarOverlayStyle(std::optional<uint32_t> scrollbarStyle)`
- `GetBytecodeProfile() -> (String string)`
- `GetSamplingProfilerOutput() -> (String string)`
- `TakeSnapshot(WebCore::IntRect snapshotRect, WebCore::IntSize bitmapSize, OptionSet<WebKit::SnapshotOption> options) -> (std::optional<WebCore::ShareableBitmapHandle> image)`
- `PerformImmediateActionHitTestAtLocation(WebCore::FrameIdentifier frameID, WebCore::FloatPoint location)` (if PLATFORM(MAC))
- `ImmediateActionDidUpdate()` (if PLATFORM(MAC))
- `ImmediateActionDidCancel()` (if PLATFORM(MAC))
- `ImmediateActionDidComplete()` (if PLATFORM(MAC))
- `DataDetectorsDidPresentUI(WebCore::PageOverlay::PageOverlayID pageOverlay)` (if PLATFORM(MAC))
- `DataDetectorsDidChangeUI(WebCore::PageOverlay::PageOverlayID pageOverlay)` (if PLATFORM(MAC))
- `DataDetectorsDidHideUI(WebCore::PageOverlay::PageOverlayID pageOverlay)` (if PLATFORM(MAC))
- `HandleAcceptedCandidate(WebCore::TextCheckingResult acceptedCandidate)` (if PLATFORM(MAC))
- `SemanticContextDidChange(bool useFormSemanticContext)` (if PLATFORM(MAC))
- `SetHeaderBannerHeight(int height)` (if PLATFORM(MAC))
- `SetFooterBannerHeight(int height)` (if PLATFORM(MAC))
- `DidBeginMagnificationGesture()` (if PLATFORM(MAC))
- `DidEndMagnificationGesture()` (if PLATFORM(MAC))
- `StartDeferringResizeEvents()`
- `FlushDeferredResizeEvents()`
- `StartDeferringScrollEvents()`
- `FlushDeferredScrollEvents()`
- `FlushDeferredDidReceiveMouseEvent()`
- `PerformHitTestForMouseEvent(WebKit::WebMouseEvent event) -> (WebKit::WebHitTestResultData hitTestResult, OptionSet<WebKit::WebEventModifier> modifiers, WebKit::UserData messageBody)`
- `SetUseColorAppearance(bool useDarkAppearance, bool useElevatedUserInterfaceLevel)`
- `SetAccentColor(WebCore::Color color)` (if HAVE(APP_ACCENT_COLORS))
- `RequestActiveNowPlayingSessionInfo() -> (bool registeredAsNowPlayingApplication, WebCore::NowPlayingInfo nowPlayingInfo)` (if PLATFORM(COCOA))
- `SetShouldDispatchFakeMouseMoveEvents(bool shouldDispatchFakeMouseMoveEvents)`
- `PlaybackTargetSelected(WebCore::PlaybackTargetClientContextIdentifier contextId, WebKit::MediaPlaybackTargetContextSerialized target)` (if ENABLE(WIRELESS_PLAYBACK_TARGET) && !PLATFORM(IOS_FAMILY))
- `PlaybackTargetAvailabilityDidChange(WebCore::PlaybackTargetClientContextIdentifier contextId, bool available)` (if ENABLE(WIRELESS_PLAYBACK_TARGET) && !PLATFORM(IOS_FAMILY))
- `SetShouldPlayToPlaybackTarget(WebCore::PlaybackTargetClientContextIdentifier contextId, bool shouldPlay)` (if ENABLE(WIRELESS_PLAYBACK_TARGET) && !PLATFORM(IOS_FAMILY))
- `PlaybackTargetPickerWasDismissed(WebCore::PlaybackTargetClientContextIdentifier contextId)` (if ENABLE(WIRELESS_PLAYBACK_TARGET) && !PLATFORM(IOS_FAMILY))
- `DidAcquirePointerLock()` (if ENABLE(POINTER_LOCK))
- `DidNotAcquirePointerLock()` (if ENABLE(POINTER_LOCK))
- `DidLosePointerLock()` (if ENABLE(POINTER_LOCK))
- `SetShouldScaleViewToFitDocument(bool shouldScaleViewToFitDocument)`
- `SetUserInterfaceLayoutDirection(uint32_t direction)`
- `DidGetLoadDecisionForIcon(bool decision, WebKit::CallbackID loadIdentifier) -> (IPC::SharedBufferReference iconData)`
- `SetUseIconLoadingClient(bool useIconLoadingClient)`
- `GamepadActivity(Vector<std::optional<WebKit::GamepadData>> gamepadDatas, WebCore::EventMakesGamepadsVisible eventVisibility)` (if ENABLE(GAMEPAD))
- `AllowGamepadAccess()` (if (ENABLE(GAMEPAD) && PLATFORM(VISION)))
- `RegisterURLSchemeHandler(WebKit::WebURLSchemeHandlerIdentifier handlerIdentifier, String scheme)`
- `URLSchemeTaskWillPerformRedirection(WebKit::WebURLSchemeHandlerIdentifier handlerIdentifier, WebCore::ResourceLoaderIdentifier taskIdentifier, WebCore::ResourceResponse response, WebCore::ResourceRequest proposedRequest) -> (WebCore::ResourceRequest actualRequest)`
- `URLSchemeTaskDidPerformRedirection(WebKit::WebURLSchemeHandlerIdentifier handlerIdentifier, WebCore::ResourceLoaderIdentifier taskIdentifier, WebCore::ResourceResponse response, WebCore::ResourceRequest proposedRequest)`
- `URLSchemeTaskDidReceiveResponse(WebKit::WebURLSchemeHandlerIdentifier handlerIdentifier, WebCore::ResourceLoaderIdentifier taskIdentifier, WebCore::ResourceResponse response)`
- `URLSchemeTaskDidReceiveData(WebKit::WebURLSchemeHandlerIdentifier handlerIdentifier, WebCore::ResourceLoaderIdentifier taskIdentifier, Ref<WebCore::SharedBuffer> data)`
- `URLSchemeTaskDidComplete(WebKit::WebURLSchemeHandlerIdentifier handlerIdentifier, WebCore::ResourceLoaderIdentifier taskIdentifier, WebCore::ResourceError error)`
- `SetIsSuspended(bool suspended)`
- `InsertAttachment(String identifier, std::optional<uint64_t> fileSize, String fileName, String contentType) -> ()` (if ENABLE(ATTACHMENT_ELEMENT))
- `UpdateAttachmentAttributes(String identifier, std::optional<uint64_t> fileSize, String contentType, String fileName, IPC::SharedBufferReference associatedElementData) -> ()` (if ENABLE(ATTACHMENT_ELEMENT))
- `UpdateAttachmentThumbnail(String identifier, std::optional<WebCore::ShareableBitmapHandle> qlThumbnailHandle)` (if ENABLE(ATTACHMENT_ELEMENT))
- `UpdateAttachmentIcon(String identifier, std::optional<WebCore::ShareableBitmapHandle> icon, WebCore::FloatSize size)` (if ENABLE(ATTACHMENT_ELEMENT))
- `GetApplicationManifest() -> (std::optional<WebCore::ApplicationManifest> manifest)` (if ENABLE(APPLICATION_MANIFEST))
- `GetTextFragmentMatch() -> (String match)`
- `ZoomPDFIn(WebKit::PDFPluginIdentifier identifier)` (if ENABLE(PDF_PLUGIN) && PLATFORM(MAC))
- `ZoomPDFOut(WebKit::PDFPluginIdentifier identifier)` (if ENABLE(PDF_PLUGIN) && PLATFORM(MAC))
- `SavePDF(WebKit::PDFPluginIdentifier identifier) -> (String filename, URL url, std::span<const uint8_t> data)` (if ENABLE(PDF_PLUGIN) && PLATFORM(MAC))
- `OpenPDFWithPreview(WebKit::PDFPluginIdentifier identifier) -> (String filename, WebKit::FrameInfoData frameInfo, std::span<const uint8_t> data, String uuid)` (if ENABLE(PDF_PLUGIN) && PLATFORM(MAC))
- `UpdateCurrentModifierState(OptionSet<WebCore::PlatformEventModifier> modifiers)`
- `SimulateDeviceOrientationChange(double alpha, double beta, double gamma)`
- `SpeakingErrorOccurred()` (if ENABLE(SPEECH_SYNTHESIS))
- `BoundaryEventOccurred(bool wordBoundary, unsigned charIndex, unsigned charLength)` (if ENABLE(SPEECH_SYNTHESIS))
- `VoicesDidChange()` (if ENABLE(SPEECH_SYNTHESIS))
- `SetCanShowPlaceholder(WebCore::ElementContext context, bool canShowPlaceholder)`
- `WasLoadedWithDataTransferFromPrevalentResource()`
- `ClearLoadedSubresourceDomains()`
- `GetLoadedSubresourceDomains() -> (Vector<WebCore::RegistrableDomain> domains)`
- `SystemPreviewActionTriggered(WebCore::SystemPreviewInfo previewInfo, String message)` (if USE(SYSTEM_PREVIEW))
- `SendMessageToWebProcessExtension(WebKit::UserMessage userMessage)` (if PLATFORM(GTK) || PLATFORM(WPE))
- `SendMessageToWebProcessExtensionWithReply(WebKit::UserMessage userMessage) -> (WebKit::UserMessage replyMessage)` (if PLATFORM(GTK) || PLATFORM(WPE))
- `PreferredBufferFormatsDidChange(Vector<WebKit::DMABufRendererBufferFormat> preferredBufferFormats)` (if PLATFORM(WPE) && USE(GBM) && ENABLE(WPE_PLATFORM))
- `StartTextManipulations(Vector<WebCore::TextManipulationControllerExclusionRule> exclusionRules, bool includeSubframes) -> ()`
- `CompleteTextManipulation(Vector<WebCore::TextManipulationItem> items) -> (bool allFailed, Vector<WebCore::TextManipulationControllerManipulationFailure> failures)`
- `SetOverriddenMediaType(String mediaType)`
- `GetProcessDisplayName() -> (String displayName)`
- `UpdateCORSDisablingPatterns(Vector<String> patterns)`
- `SetIsTakingSnapshotsForApplicationSuspension(bool isTakingSnapshotsForApplicationSuspension)`
- `SetNeedsDOMWindowResizeEvent()`
- `SetHasResourceLoadClient(bool has)`
- `SetCanUseCredentialStorage(bool canUse)`
- `CreateAppHighlightInSelectedRange(WebCore::CreateNewGroupForHighlight createNewGroup, WebCore::HighlightRequestOriginatedInApp requestOrigin) -> (WebCore::AppHighlight info)` (if ENABLE(APP_HIGHLIGHTS))
- `RestoreAppHighlightsAndScrollToIndex(Vector<WebCore::SharedMemory::Handle> memoryHandles, std::optional<unsigned> index)` (if ENABLE(APP_HIGHLIGHTS))
- `SetAppHighlightsVisibility(WebCore::HighlightVisibility highlightVisibility)` (if ENABLE(APP_HIGHLIGHTS))
- `HandleWheelEvent(WebCore::FrameIdentifier frameID, WebKit::WebWheelEvent event, OptionSet<WebCore::WheelEventProcessingSteps> processingSteps, std::optional<bool> willStartSwipe) -> (std::optional<WebCore::ScrollingNodeID> scrollingNodeID, std::optional<WebCore::WheelScrollGestureState> gestureState, bool handled, std::optional<WebCore::RemoteUserInputEventData> remoteUserInputEventData)`
- `DispatchWheelEventWithoutScrolling(WebCore::FrameIdentifier frameID, WebKit::WebWheelEvent event) -> (bool defaultPrevented)` (if PLATFORM(IOS_FAMILY))
- `LastNavigationWasAppInitiated() -> (bool wasAppBound)`
- `CreateMediaSessionCoordinator(String identifier) -> (bool success)` (if ENABLE(MEDIA_SESSION_COORDINATOR))
- `UpdateWithTextRecognitionResult(WebCore::TextRecognitionResult result, WebCore::ElementContext element, WebCore::FloatPoint location) -> (WebKit::TextRecognitionUpdateResult result)` (if ENABLE(IMAGE_ANALYSIS))
- `StartVisualTranslation(String sourceLanguageIdentifier, String targetLanguageIdentifier)` (if ENABLE(IMAGE_ANALYSIS))
- `ScrollToRect(WebCore::FloatRect targetRect, WebCore::FloatPoint origin)`
- `NavigateServiceWorkerClient(WebCore::ScriptExecutionContextIdentifier documentIdentifier, URL url) -> (WebCore::ScheduleLocationChangeResult result)`
- `ModelInlinePreviewDidLoad(WebCore::PlatformLayerIdentifier layerID)` (if ENABLE(ARKIT_INLINE_PREVIEW_IOS))
- `ModelInlinePreviewDidFailToLoad(WebCore::PlatformLayerIdentifier layerID, WebCore::ResourceError error)` (if ENABLE(ARKIT_INLINE_PREVIEW_IOS))
- `SetIsWindowResizingEnabled(bool hasResizableWindows)` (if HAVE(UIKIT_RESIZABLE_WINDOWS))
- `SetInteractionRegionsEnabled(bool enable)` (if ENABLE(INTERACTION_REGIONS_IN_EVENT_REGION))
- `GenerateTestReport(String message, String group)`
- `SetLinkDecorationFilteringData(Vector<WebCore::LinkDecorationFilteringData> strings)` (if ENABLE(ADVANCED_PRIVACY_PROTECTIONS))
- `SetAllowedQueryParametersForAdvancedPrivacyProtections(Vector<WebCore::LinkDecorationFilteringData> allowedStrings)` (if ENABLE(ADVANCED_PRIVACY_PROTECTIONS))
- `PauseAllAnimations() -> ()` (if ENABLE(ACCESSIBILITY_ANIMATION_CONTROL))
- `PlayAllAnimations() -> ()` (if ENABLE(ACCESSIBILITY_ANIMATION_CONTROL))
- `UseRedirectionForCurrentNavigation(WebCore::ResourceResponse response)`
- `UpdateFrameScrollingMode(WebCore::FrameIdentifier frame, WebCore::ScrollbarMode scrollingMode)`
- `UpdateFrameSize(WebCore::FrameIdentifier frame, WebCore::IntSize newSize)`
- `DispatchLoadEventToFrameOwnerElement(WebCore::FrameIdentifier frameID)`
- `FrameWasFocusedInAnotherProcess(WebCore::FrameIdentifier frameID)`
- `RemotePostMessage(WebCore::FrameIdentifier source, String sourceOrigin, WebCore::FrameIdentifier target, std::optional<WebCore::SecurityOriginData> targetOrigin, WebCore::MessageWithMessagePorts message)`
- `RenderTreeAsTextForTesting(WebCore::FrameIdentifier frameID, size_t baseIndent, OptionSet<WebCore::RenderAsTextFlag> behavior) -> (String renderTreeDump)` (sync)
- `LayerTreeAsTextForTesting(WebCore::FrameIdentifier frameID, size_t baseIndent, OptionSet<WebCore::LayerTreeAsTextOptions> options) -> (String layerTreeDump)` (sync)
- `FrameTextForTesting(WebCore::FrameIdentifier frameID) -> (String text)` (sync)
- `RequestAllTextAndRects() -> (Vector<std::pair<String, WebCore::FloatRect>> textAndRects)`
- `RequestTargetedElement(WebCore::TargetedElementRequest request) -> (Vector<WebCore::TargetedElementInfo> elements)`
- `RequestAllTargetableElements(float hitTestInterval) -> (Vector<Vector<WebCore::TargetedElementInfo>> elements)`
- `RequestTextExtraction(std::optional<WebCore::FloatRect> collectionRectInRootView) -> (WebCore::TextExtraction::Item item)`
- `ShouldDismissKeyboardAfterTapAtPoint(WebCore::FloatPoint point) -> (bool shouldDismiss)` (if PLATFORM(IOS_FAMILY))
- `SetMediaEnvironment(String mediaEnvironment)` (if ENABLE(EXTENSION_CAPABILITIES))
- `WillBeginWritingToolsSession(std::optional<WebCore::WritingTools::Session> session) -> (Vector<WebCore::WritingTools::Context> contexts)` (if ENABLE(WRITING_TOOLS))
- `DidBeginWritingToolsSession(WebCore::WritingTools::Session session, Vector<WebCore::WritingTools::Context> contexts)` (if ENABLE(WRITING_TOOLS))
- `ProofreadingSessionDidReceiveSuggestions(WebCore::WritingTools::Session session, Vector<WebCore::WritingTools::TextSuggestion> suggestions, WebCore::CharacterRange processedRange, WebCore::WritingTools::Context context, bool finished) -> ()` (if ENABLE(WRITING_TOOLS))
- `ProofreadingSessionDidUpdateStateForSuggestion(WebCore::WritingTools::Session session, WebCore::WritingTools::TextSuggestionState state, WebCore::WritingTools::TextSuggestion suggestion, WebCore::WritingTools::Context context)` (if ENABLE(WRITING_TOOLS))
- `WillEndWritingToolsSession(WebCore::WritingTools::Session session, bool accepted) -> ()` (if ENABLE(WRITING_TOOLS))
- `DidEndWritingToolsSession(WebCore::WritingTools::Session session, bool accepted)` (if ENABLE(WRITING_TOOLS))
- `CompositionSessionDidReceiveTextWithReplacementRange(WebCore::WritingTools::Session session, WebCore::AttributedString attributedText, WebCore::CharacterRange range, WebCore::WritingTools::Context context, bool finished) -> ()` (if ENABLE(WRITING_TOOLS))
- `WritingToolsSessionDidReceiveAction(WebCore::WritingTools::Session session, WebCore::WritingTools::Action action)` (if ENABLE(WRITING_TOOLS))
- `ProofreadingSessionSuggestionTextRectsInRootViewCoordinates(WebCore::CharacterRange enclosingRangeRelativeToSessionRange) -> (Vector<WebCore::FloatRect> rects)` (if ENABLE(WRITING_TOOLS))
- `UpdateTextVisibilityForActiveWritingToolsSession(WebCore::CharacterRange rangeRelativeToSessionRange, bool visible, WTF::UUID identifier) -> ()` (if ENABLE(WRITING_TOOLS))
- `TextPreviewDataForActiveWritingToolsSession(WebCore::CharacterRange rangeRelativeToSessionRange) -> (std::optional<WebCore::TextIndicatorData> data)` (if ENABLE(WRITING_TOOLS))
- `SetSelectionForActiveWritingToolsSession(WebCore::CharacterRange rangeRelativeToSessionRange) -> ()` (if ENABLE(WRITING_TOOLS))
- `DecorateTextReplacementsForActiveWritingToolsSession(WebCore::CharacterRange rangeRelativeToSessionRange) -> ()` (if ENABLE(WRITING_TOOLS))
- `CreateTextIndicatorForTextAnimationID(WTF::UUID uuid) -> (std::optional<WebCore::TextIndicatorData> textIndicator)` (if ENABLE(WRITING_TOOLS))
- `UpdateUnderlyingTextVisibilityForTextAnimationID(WTF::UUID uuid, bool visible) -> ()` (if ENABLE(WRITING_TOOLS))
- `IntelligenceTextAnimationsDidComplete()` (if ENABLE(WRITING_TOOLS))
- `CreateTextIndicatorForElementWithID(String elementID) -> (std::optional<WebCore::TextIndicatorData> textIndicator)` (if PLATFORM(COCOA))
- `TakeSnapshotForTargetedElement(WebCore::ElementIdentifier elementID, WebCore::ScriptExecutionContextIdentifier documentID) -> (std::optional<WebCore::ShareableBitmapHandle> image)`
- `ResetVisibilityAdjustmentsForTargetedElements(Vector<std::pair<WebCore::ElementIdentifier, WebCore::ScriptExecutionContextIdentifier>> identifiers) -> (bool success)`
- `AdjustVisibilityForTargetedElements(Vector<WebCore::TargetedElementAdjustment> adjustments) -> (bool success)`
- `NumberOfVisibilityAdjustmentRects() -> (uint64_t count)`
- `RemoteViewRectToRootView(WebCore::FrameIdentifier frameID, WebCore::FloatRect rect) -> (WebCore::FloatRect rect)`
- `RemoteViewPointToRootView(WebCore::FrameIdentifier frameID, WebCore::FloatPoint point) -> (WebCore::FloatPoint point)`
- `RemoteDictionaryPopupInfoToRootView(WebCore::FrameIdentifier frameID, WebCore::DictionaryPopupInfo popupInfo) -> (WebCore::DictionaryPopupInfo popupInfo)`
- `SetDefaultSpatialTrackingLabel(String label)` (if HAVE(SPATIAL_TRACKING_LABEL))
- `StartObservingNowPlayingMetadata()`
- `StopObservingNowPlayingMetadata()`
- `LoadAndDecodeImage(WebCore::ResourceRequest request, std::optional<WebCore::FloatSize> sizeConstraint, size_t maximumBytesFromNetwork) -> (std::variant<WebCore::ResourceError, Ref<WebCore::ShareableBitmap>> result)`
- `GetInformationFromImageData(Vector<uint8_t> imageData) -> (Expected<std::pair<String, Vector<WebCore::IntSize>>, WebCore::ImageDecodingError> result)` (if PLATFORM(COCOA))
- `CreateBitmapsFromImageData(Ref<WebCore::SharedBuffer> imageData, Vector<unsigned> lengths) -> (Vector<Ref<WebCore::ShareableBitmap>> result)` (if PLATFORM(COCOA))
- `DecodeImageData(Ref<WebCore::SharedBuffer> imageData, std::optional<WebCore::FloatSize> preferredSize) -> (RefPtr<WebCore::ShareableBitmap> result)` (if PLATFORM(COCOA))
- `FrameNameWasChangedInAnotherProcess(WebCore::FrameIdentifier frameID, String frameName)`
- `StartPlayingPredominantVideo() -> (bool success)` (if ENABLE(VIDEO_PRESENTATION_MODE))
- `CloseCurrentTypingCommand()`
- `SimulateClickOverFirstMatchingTextInViewportWithUserInteraction(String targetText) -> (bool success)`
- `UpdateOpener(WebCore::FrameIdentifier frameID, WebCore::FrameIdentifier newOpener)`
- `SetPresentingApplicationAuditTokenAndBundleIdentifier(WebKit::CoreIPCAuditToken auditToken, String bundleIdentifier)` (if HAVE(AUDIT_TOKEN))

## `WebPageTesting` - UI -> WebContent

`WebProcess/WebPage/WebPageTesting.messages.in`

- `IsLayerTreeFrozen() -> (bool isFrozen)`
- `SetPermissionLevel(String origin, bool allowed)`
- `IsEditingCommandEnabled(String commandName) -> (bool result)` (sync)
- `ClearNotificationPermissionState()` (if ENABLE(NOTIFICATIONS))
- `ClearWheelEventTestMonitor()`
- `ResetStateBetweenTests()`
- `SetTopContentInset(float contentInset) -> ()`
- `ClearCachedBackForwardListCounts() -> ()`
- `SetTracksRepaints(bool trackRepaints) -> ()`
- `DisplayAndTrackRepaints() -> ()`

## `WebPaymentCoordinator` - UI -> WebContent

`WebProcess/ApplePay/WebPaymentCoordinator.messages.in`

- `ValidateMerchant(String validationURLString)`
- `DidAuthorizePayment(WebCore::Payment payment)`
- `DidSelectShippingMethod(WebCore::ApplePayShippingMethod shippingMethod)`
- `DidSelectShippingContact(WebCore::PaymentContact shippingContact)`
- `DidSelectPaymentMethod(WebCore::PaymentMethod paymentMethod)`
- `DidChangeCouponCode(String couponCode)` (if ENABLE(APPLE_PAY_COUPON_CODE))
- `DidCancelPaymentSession(WebCore::PaymentSessionError sessionError)`

## `WebPermissionController` - UI -> WebContent

`WebProcess/WebCoreSupport/WebPermissionController.messages.in`

- `permissionChanged(WebCore::PermissionName permissionName, WebCore::SecurityOriginData topOrigin)`

## `WebProcess` - UI -> WebContent

`WebProcess/WebProcess.messages.in`

- `InitializeWebProcess(WebKit::WebProcessCreationParameters processCreationParameters) -> (WebCore::ProcessIdentity processIdentity)`
- `SetWebsiteDataStoreParameters(WebKit::WebProcessDataStoreParameters parameters)`
- `CreateWebPage(WebCore::PageIdentifier newPageID, WebKit::WebPageCreationParameters pageCreationParameters)`
- `PrewarmWithDomainInformation(WebCore::PrewarmInformation prewarmInformation)`
- `SetCacheModel(WebKit::CacheModel cacheModel)`
- `RegisterURLSchemeAsEmptyDocument(String scheme)`
- `RegisterURLSchemeAsSecure(String scheme)`
- `RegisterURLSchemeAsBypassingContentSecurityPolicy(String scheme)`
- `SetDomainRelaxationForbiddenForURLScheme(String scheme)`
- `RegisterURLSchemeAsLocal(String scheme)`
- `RegisterURLSchemeAsNoAccess(String scheme)`
- `RegisterURLSchemeAsDisplayIsolated(String scheme)`
- `RegisterURLSchemeAsCORSEnabled(String scheme)`
- `RegisterURLSchemeAsCachePartitioned(String scheme)`
- `RegisterURLSchemeAsCanDisplayOnlyIfCanRequest(String scheme)`
- `RegisterURLSchemeAsWebExtension(String scheme)` (if ENABLE(WK_WEB_EXTENSIONS))
- `SetDefaultRequestTimeoutInterval(double timeoutInterval)`
- `SetAlwaysUsesComplexTextCodePath(bool alwaysUseComplexText)`
- `SetDisableFontSubpixelAntialiasingForTesting(bool disable)`
- `SetTrackingPreventionEnabled(bool enabled)`
- `ClearResourceLoadStatistics()`
- `UserPreferredLanguagesChanged(Vector<String> languages)`
- `FullKeyboardAccessModeChanged(bool fullKeyboardAccessEnabled)`
- `UpdateStorageAccessUserAgentStringQuirks(HashMap<WebCore::RegistrableDomain, String> userAgentStringQuirks)`
- `SetOptInCookiePartitioningEnabled(bool enabled)` (if HAVE(ALLOW_ONLY_PARTITIONED_COOKIES))
- `SetHasMouseDevice(bool hasMouseDevice)` (if HAVE(MOUSE_DEVICE_OBSERVATION))
- `SetHasStylusDevice(bool hasStylusDevice)` (if HAVE(STYLUS_DEVICE_OBSERVATION))
- `StartMemorySampler(WebKit::SandboxExtensionHandle sampleLogFileHandle, String sampleLogFilePath, double interval)`
- `StopMemorySampler()`
- `SetTextCheckerState(OptionSet<WebKit::TextCheckerState> textCheckerState)`
- `SetEnhancedAccessibility(bool flag)`
- `BindAccessibilityFrameWithData(WebCore::FrameIdentifier frameID, std::span<const uint8_t> data)`
- `GarbageCollectJavaScriptObjects()`
- `SetJavaScriptGarbageCollectorTimerEnabled(bool enable)`
- `SetInjectedBundleParameter(String parameter, std::span<const uint8_t> value)`
- `SetInjectedBundleParameters(std::span<const uint8_t> parameters)`
- `HandleInjectedBundleMessage(String messageName, WebKit::UserData messageBody)`
- `FetchWebsiteData(OptionSet<WebKit::WebsiteDataType> websiteDataTypes) -> (WebKit::WebsiteData websiteData)`
- `DeleteWebsiteData(OptionSet<WebKit::WebsiteDataType> websiteDataTypes, WallTime modifiedSince) -> ()`
- `DeleteWebsiteDataForOrigins(OptionSet<WebKit::WebsiteDataType> websiteDataTypes, Vector<WebCore::SecurityOriginData> origins) -> ()`
- `DeleteWebsiteDataForOrigin(OptionSet<WebKit::WebsiteDataType> websiteDataTypes, WebCore::ClientOrigin origin) -> ()`
- `ReloadExecutionContextsForOrigin(WebCore::ClientOrigin origin, std::optional<WebCore::FrameIdentifier> triggeringFrame) -> ()`
- `DeleteAllCookies() -> ()`
- `SetHiddenPageDOMTimerThrottlingIncreaseLimit(Seconds seconds)`
- `SetMemoryCacheDisabled(bool disabled)`
- `SetEnabledServices(bool hasImageServices, bool hasSelectionServices, bool hasRichContentServices)` (if ENABLE(SERVICE_CONTROLS))
- `EnsureAutomationSessionProxy(String sessionIdentifier)`
- `DestroyAutomationSessionProxy()`
- `PrepareToSuspend(bool isSuspensionImminent, MonotonicTime estimatedSuspendTime) -> ()`
- `ProcessDidResume()`
- `BackgroundResponsivenessPing()`
- `SetInitialGamepads(Vector<std::optional<WebKit::GamepadData>> gamepadDatas)` (if ENABLE(GAMEPAD))
- `GamepadConnected(WebKit::GamepadData gamepadData, WebCore::EventMakesGamepadsVisible eventVisibility)` (if ENABLE(GAMEPAD))
- `GamepadDisconnected(unsigned index)` (if ENABLE(GAMEPAD))
- `EstablishRemoteWorkerContextConnectionToNetworkProcess(WebKit::RemoteWorkerType workerType, WebKit::PageGroupIdentifier pageGroupID, WebKit::WebPageProxyIdentifier webPageProxyID, WebCore::PageIdentifier pageID, WebKit::WebPreferencesStore store, WebCore::Site site, std::optional<WebCore::ScriptExecutionContextIdentifier> serviceWorkerPageIdentifier, WebKit::RemoteWorkerInitializationData initializationData) -> ()`
- `RegisterServiceWorkerClients() -> (bool isSuccess)`
- `SetHasSuspendedPageProxy(bool hasSuspendedPageProxy)`
- `SetIsInProcessCache(bool isInProcessCache) -> ()`
- `MarkIsNoLongerPrewarmed()`
- `GetActivePagesOriginsForTesting() -> (Vector<String> activeOrigins)`
- `SetScreenProperties(WebCore::ScreenProperties screenProperties)` (if PLATFORM(COCOA) || PLATFORM(GTK) || PLATFORM(WPE))
- `ScrollerStylePreferenceChanged(bool useOvelayScrollbars)` (if PLATFORM(MAC))
- `UserInterfaceIdiomDidChange(PAL::UserInterfaceIdiom idiom)` (if PLATFORM(IOS_FAMILY))
- `BacklightLevelDidChange(float backlightLevel)` (if PLATFORM(IOS_FAMILY) && !PLATFORM(MACCATALYST))
- `ColorPreferencesDidChange()` (if PLATFORM(MAC) || PLATFORM(MACCATALYST))
- `IsJITEnabled() -> (bool enabled)`
- `SetMediaMIMETypes(Vector<String> types)` (if PLATFORM(COCOA))
- `EnableRemoteWebInspector()` (if (PLATFORM(COCOA) && ENABLE(REMOTE_INSPECTOR)))
- `AddMockMediaDevice(WebCore::MockMediaDevice device)` (if ENABLE(MEDIA_STREAM))
- `ClearMockMediaDevices()` (if ENABLE(MEDIA_STREAM))
- `RemoveMockMediaDevice(String persistentId)` (if ENABLE(MEDIA_STREAM))
- `SetMockMediaDeviceIsEphemeral(String persistentId, bool isEphemeral)` (if ENABLE(MEDIA_STREAM))
- `ResetMockMediaDevices()` (if ENABLE(MEDIA_STREAM))
- `GrantUserMediaDeviceSandboxExtensions(WebKit::MediaDeviceSandboxExtensions sandboxExtensions)` (if (ENABLE(MEDIA_STREAM) && ENABLE(SANDBOX_EXTENSIONS)))
- `RevokeUserMediaDeviceSandboxExtensions(Vector<String> sandboxExtensionIDs)` (if (ENABLE(MEDIA_STREAM) && ENABLE(SANDBOX_EXTENSIONS)))
- `ClearCurrentModifierStateForTesting()`
- `SetBackForwardCacheCapacity(unsigned capacity)`
- `ClearCachedPage(WebCore::BackForwardItemIdentifier backForwardItemID) -> ()`
- `SendMessageToWebProcessExtension(WebKit::UserMessage userMessage)` (if PLATFORM(GTK) || PLATFORM(WPE))
- `SeedResourceLoadStatisticsForTesting(WebCore::RegistrableDomain firstPartyDomain, WebCore::RegistrableDomain thirdPartyDomain, bool shouldScheduleNotification) -> ()`
- `SetThirdPartyCookieBlockingMode(WebCore::ThirdPartyCookieBlockingMode blockingMode) -> ()`
- `SetDomainsWithUserInteraction(HashSet<WebCore::RegistrableDomain> domains)`
- `SetDomainsWithCrossPageStorageAccess(HashMap<WebCore::RegistrableDomain, Vector<WebCore::RegistrableDomain>> domains) -> ()`
- `SendResourceLoadStatisticsDataImmediately() -> ()`
- `UpdateDomainsWithStorageAccessQuirks(HashSet<WebCore::RegistrableDomain> domainsWithStorageAccessQuirks)`
- `UpdateScriptTelemetryFilter(WebKit::ScriptTelemetryRules rules)`
- `GrantAccessToAssetServices(Vector<WebKit::SandboxExtensionHandle> assetServicesHandles)`
- `RevokeAccessToAssetServices()`
- `SwitchFromStaticFontRegistryToUserFontRegistry(Vector<WebKit::SandboxExtensionHandle> fontMachExtensionHandles)`
- `DisableURLSchemeCheckInDataDetectors()` (if PLATFORM(COCOA))
- `UnblockServicesRequiredByAccessibility(Vector<WebKit::SandboxExtensionHandle> handleArray)` (if PLATFORM(COCOA))
- `PowerSourceDidChange(bool hasAC)` (if PLATFORM(COCOA))
- `SetUseSystemAppearanceForScrollbars(bool useSystemAppearanceForScrollbars)` (if PLATFORM(GTK) && !USE(GTK4) && USE(CAIRO))
- `DidWriteToPasteboardAsynchronously(String pasteboardName)` (CanDispatchOutOfOrder, if PLATFORM(COCOA))
- `DisplayDidRefresh(uint32_t displayID, WebCore::DisplayUpdate update)` (if HAVE(DISPLAY_LINK))
- `SystemWillPowerOn()` (if PLATFORM(MAC))
- `SystemWillSleep()` (if PLATFORM(MAC))
- `SystemDidWake()` (if PLATFORM(MAC))
- `ConsumeAudioComponentRegistrations(IPC::SharedBufferReference registrationData)` (if HAVE(AUDIO_COMPONENT_SERVER_REGISTRATIONS))
- `AccessibilityPreferencesDidChange(WebKit::AccessibilityPreferences accessibilityPreferences)` (if PLATFORM(COCOA))
- `SetMediaAccessibilityPreferences(WebCore::CaptionUserPreferencesDisplayMode displayMode, Vector<String> languages)` (if HAVE(MEDIA_ACCESSIBILITY_FRAMEWORK))
- `OpenDirectoryCacheInvalidated(WebKit::SandboxExtensionHandle handle, WebKit::SandboxExtensionHandle machBootstrapHandle)` (if PLATFORM(MAC))
- `ReleaseMemory() -> ()`
- `PostNotification(String message, std::optional<uint64_t> state)` (if ENABLE(NOTIFY_BLOCKING))
- `PostObserverNotification(String message)` (if ENABLE(NOTIFY_BLOCKING))
- `GetNotifyStateForTesting(String notificationName) -> (std::optional<uint64_t> state)` (if ENABLE(NOTIFY_BLOCKING))
- `SetResourceMonitorContentRuleList(WebKit::WebCompiledContentRuleListData ruleListData)` (if ENABLE(CONTENT_EXTENSIONS))
- `SetResourceMonitorContentRuleListAsync(WebKit::WebCompiledContentRuleListData ruleListData) -> ()` (if ENABLE(CONTENT_EXTENSIONS))
- `RegisterAdditionalFonts(WebKit::AdditionalFonts fonts)` (if PLATFORM(COCOA))

## `WebScreenOrientationManager` - UI -> WebContent

`WebProcess/WebCoreSupport/WebScreenOrientationManager.messages.in`

- `OrientationDidChange(WebCore::ScreenOrientationType orientation)`

## `WebSharedWorkerContextManagerConnection` - UI -> WebContent

`WebProcess/Storage/WebSharedWorkerContextManagerConnection.messages.in`

- `LaunchSharedWorker(WebCore::ClientOrigin origin, WebCore::SharedWorkerIdentifier sharedWorkerIdentifier, WebCore::WorkerOptions workerOptions, WebCore::WorkerFetchResult workerFetchResult, WebCore::WorkerInitializationData workerInitializationData)`
- `PostConnectEvent(WebCore::SharedWorkerIdentifier sharedWorkerIdentifier, WebCore::TransferredMessagePort port, String sourceOrigin) -> (bool success)`
- `TerminateSharedWorker(WebCore::SharedWorkerIdentifier sharedWorkerIdentifier)`
- `UpdatePreferencesStore(WebKit::WebPreferencesStore store)`
- `SetUserAgent(String userAgent)`
- `Close()`
- `SuspendSharedWorker(WebCore::SharedWorkerIdentifier sharedWorkerIdentifier)`
- `ResumeSharedWorker(WebCore::SharedWorkerIdentifier sharedWorkerIdentifier)`

## `WebSpeechRecognitionConnection` - UI -> WebContent

`WebProcess/WebCoreSupport/WebSpeechRecognitionConnection.messages.in`

- `DidReceiveUpdate(WebCore::SpeechRecognitionUpdate update)`

## `WebUserContentController` - UI -> WebContent

`WebProcess/UserContent/WebUserContentController.messages.in`

- `AddContentWorlds(Vector<WebKit::ContentWorldData> worlds)`
- `RemoveContentWorlds(Vector<WebKit::ContentWorldIdentifier> worldIdentifiers)`
- `AddUserScripts(Vector<WebKit::WebUserScriptData> userScripts, WebKit::InjectUserScriptImmediately immediately)`
- `RemoveUserScript(WebKit::ContentWorldIdentifier worldIdentifier, WebKit::UserScriptIdentifier identifier)`
- `RemoveAllUserScripts(Vector<WebKit::ContentWorldIdentifier> worldIdentifiers)`
- `AddUserStyleSheets(Vector<WebKit::WebUserStyleSheetData> userStyleSheets)`
- `RemoveUserStyleSheet(WebKit::ContentWorldIdentifier worldIdentifier, WebKit::UserStyleSheetIdentifier identifier)`
- `RemoveAllUserStyleSheets(Vector<WebKit::ContentWorldIdentifier> worldIdentifiers)`
- `AddUserScriptMessageHandlers(Vector<WebKit::WebScriptMessageHandlerData> scriptMessageHandlers)`
- `RemoveUserScriptMessageHandler(WebKit::ContentWorldIdentifier worldIdentifier, WebKit::ScriptMessageHandlerIdentifier identifier)`
- `RemoveAllUserScriptMessageHandlersForWorlds(Vector<WebKit::ContentWorldIdentifier> worldIdentifiers)`
- `RemoveAllUserScriptMessageHandlers()`
- `AddContentRuleLists(Vector<std::pair<WebKit::WebCompiledContentRuleListData, URL>> contentFilters)` (if ENABLE(CONTENT_EXTENSIONS))
- `RemoveContentRuleList(String name)` (if ENABLE(CONTENT_EXTENSIONS))
- `RemoveAllContentRuleLists()` (if ENABLE(CONTENT_EXTENSIONS))

## `GPUProcess` - UI -> GPU

`GPUProcess/GPUProcess.messages.in`

- `InitializeGPUProcess(WebKit::GPUProcessCreationParameters processCreationParameters) -> ()`
- `CreateGPUConnectionToWebProcess(WebCore::ProcessIdentifier processIdentifier, PAL::SessionID sessionID, IPC::ConnectionHandle connectionHandle, WebKit::GPUProcessConnectionParameters parameters) -> ()` (AllowedWhenWaitingForSyncReply)
- `SharedPreferencesForWebProcessDidChange(WebCore::ProcessIdentifier processIdentifier, WebKit::SharedPreferencesForWebProcess sharedPreferencesForWebProcess) -> ()`
- `UpdateGPUProcessPreferences(WebKit::GPUProcessPreferences preferences)`
- `UpdateSandboxAccess(Vector<WebKit::SandboxExtensionHandle> extensions)`
- `PrepareToSuspend(bool isSuspensionImminent, MonotonicTime estimatedSuspendTime) -> ()`
- `ProcessDidResume()`
- `AddSession(PAL::SessionID sessionID, WebKit::GPUProcessSessionParameters parameters)`
- `RemoveSession(PAL::SessionID sessionID)`
- `SetMockCaptureDevicesEnabled(bool isEnabled)` (if ENABLE(MEDIA_STREAM))
- `SetOrientationForMediaCapture(WebCore::IntDegrees orientation)` (if ENABLE(MEDIA_STREAM))
- `RotationAngleForCaptureDeviceChanged(String persistentId, WebCore::VideoFrameRotation rotation)` (if ENABLE(MEDIA_STREAM))
- `UpdateCaptureAccess(bool allowAudioCapture, bool allowVideoCapture, bool allowDisplayCapture, WebCore::ProcessIdentifier processID) -> ()` (if ENABLE(MEDIA_STREAM))
- `UpdateCaptureOrigin(WebCore::SecurityOriginData originData, WebCore::ProcessIdentifier processID)` (if ENABLE(MEDIA_STREAM))
- `AddMockMediaDevice(WebCore::MockMediaDevice device)` (if ENABLE(MEDIA_STREAM))
- `ClearMockMediaDevices()` (if ENABLE(MEDIA_STREAM))
- `RemoveMockMediaDevice(String persistentId)` (if ENABLE(MEDIA_STREAM))
- `SetMockMediaDeviceIsEphemeral(String persistentId, bool isEphemeral)` (if ENABLE(MEDIA_STREAM))
- `ResetMockMediaDevices()` (if ENABLE(MEDIA_STREAM))
- `SetMockCaptureDevicesInterrupted(bool isCameraInterrupted, bool isMicrophoneInterrupted)` (if ENABLE(MEDIA_STREAM))
- `TriggerMockCaptureConfigurationChange(bool forMicrophone, bool forDisplay)` (if ENABLE(MEDIA_STREAM))
- `SetShouldListenToVoiceActivity(bool shouldListen)` (if ENABLE(MEDIA_STREAM))
- `EnableMicrophoneMuteStatusAPI()` (if ENABLE(MEDIA_STREAM))
- `SetUseSCContentSharingPicker(bool use)` (if HAVE(SC_CONTENT_SHARING_PICKER))
- `SetScreenProperties(WebCore::ScreenProperties screenProperties)` (if PLATFORM(MAC))
- `PromptForGetDisplayMedia(WebCore::DisplayCapturePromptType type) -> (std::optional<WebCore::CaptureDevice> device)` (if HAVE(SCREEN_CAPTURE_KIT))
- `CancelGetDisplayMediaPrompt()` (if HAVE(SCREEN_CAPTURE_KIT))
- `RequestBitmapImageForCurrentTime(WebCore::ProcessIdentifier processIdentifier, WebCore::MediaPlayerIdentifier playerIdentifier) -> (std::optional<WebCore::ShareableBitmapHandle> handle)` (if ENABLE(VIDEO))
- `OpenDirectoryCacheInvalidated(WebKit::SandboxExtensionHandle handle)` (if PLATFORM(MAC))
- `ConsumeAudioComponentRegistrations(IPC::SharedBufferReference registrationData)` (if HAVE(AUDIO_COMPONENT_SERVER_REGISTRATIONS))
- `EnablePowerLogging(WebKit::SandboxExtensionHandle handle)` (if HAVE(POWERLOG_TASK_MODE_QUERY))
- `UserPreferredLanguagesChanged(Vector<String> languages)`
- `WebProcessConnectionCountForTesting() -> (uint64_t count)`
- `ResolveBookmarkDataForCacheDirectory(std::span<const uint8_t> bookmarkData)` (if USE(EXTENSIONKIT))
- `WebXRPromptAccepted(std::optional<WebCore::ProcessIdentity> processIdentity) -> (bool accepted)` (if ENABLE(WEBXR))
- `SetPresentingApplicationAuditToken(WebCore::ProcessIdentifier processIdentifier, WebCore::PageIdentifier pageIdentifier, std::optional<WebKit::CoreIPCAuditToken> auditToken)` (if HAVE(AUDIT_TOKEN))
- `RequestSharedSimulationConnection(WebKit::CoreIPCAuditToken modelProcessAuditToken) -> (std::optional<IPC::SharedFileHandle> sharedSimulationConnection)` (if PLATFORM(VISION) && ENABLE(MODEL_PROCESS))

## `AuthenticationManager` - UI -> Networking

`NetworkProcess/Authentication/AuthenticationManager.messages.in`

- `CompleteAuthenticationChallenge(WebKit::AuthenticationChallengeIdentifier challengeID, WebKit::AuthenticationChallengeDisposition disposition, WebCore::Credential credential)`

## `LegacyCustomProtocolManager` - UI -> Networking

`NetworkProcess/CustomProtocols/LegacyCustomProtocolManager.messages.in`

- `DidFailWithError(WebKit::LegacyCustomProtocolID customProtocolID, WebCore::ResourceError error)`
- `DidLoadData(WebKit::LegacyCustomProtocolID customProtocolID, std::span<const uint8_t> data)`
- `DidReceiveResponse(WebKit::LegacyCustomProtocolID customProtocolID, WebCore::ResourceResponse response, WebKit::CacheStoragePolicy cacheStoragePolicy)`
- `DidFinishLoading(WebKit::LegacyCustomProtocolID customProtocolID)`
- `WasRedirectedToRequest(WebKit::LegacyCustomProtocolID customProtocolID, WebCore::ResourceRequest request, WebCore::ResourceResponse redirectResponse)`
- `RegisterScheme(String name)`
- `UnregisterScheme(String name)`

## `NetworkContentRuleListManager` - UI -> Networking

`NetworkProcess/NetworkContentRuleListManager.messages.in`

- `Remove(WebKit::UserContentControllerIdentifier identifier)`
- `AddContentRuleLists(WebKit::UserContentControllerIdentifier identifier, Vector<std::pair<WebKit::WebCompiledContentRuleListData, URL>> contentFilters)`
- `RemoveContentRuleList(WebKit::UserContentControllerIdentifier identifier, String name)`
- `RemoveAllContentRuleLists(WebKit::UserContentControllerIdentifier identifier)`

## `NetworkProcess` - UI -> Networking

`NetworkProcess/NetworkProcess.messages.in`

- `InitializeNetworkProcess(WebKit::NetworkProcessCreationParameters processCreationParameters) -> ()`
- `CreateNetworkConnectionToWebProcess(WebCore::ProcessIdentifier processIdentifier, PAL::SessionID sessionID, WebKit::NetworkProcessConnectionParameters parameters) -> (std::optional<IPC::ConnectionHandle> connectionHandle, WebCore::HTTPCookieAcceptPolicy cookieAcceptPolicy)` (AllowedWhenWaitingForSyncReply)
- `SharedPreferencesForWebProcessDidChange(WebCore::ProcessIdentifier processIdentifier, WebKit::SharedPreferencesForWebProcess sharedPreferencesForWebProcess) -> ()`
- `AddAllowedFirstPartyForCookies(WebCore::ProcessIdentifier processIdentifier, WebCore::RegistrableDomain firstPartyForCookies, WebKit::LoadedWebArchive loadedWebArchive) -> ()`
- `SetIgnoreTLSErrors(PAL::SessionID sessionID, bool ignoreTLSErrors)` (if USE(SOUP))
- `UserPreferredLanguagesChanged(Vector<String> languages)` (if USE(SOUP))
- `SetNetworkProxySettings(PAL::SessionID sessionID, WebCore::SoupNetworkProxySettings settings)` (if USE(SOUP))
- `PrefetchDNS(String hostname)` (if USE(SOUP))
- `SetPersistentCredentialStorageEnabled(PAL::SessionID sessionID, bool enabled)` (if USE(SOUP))
- `SetNetworkProxySettings(PAL::SessionID sessionID, WebCore::CurlProxySettings settings)` (if USE(CURL))
- `AddWebsiteDataStore(WebKit::WebsiteDataStoreParameters websiteDataStoreParameters)` (AllowedWhenWaitingForSyncReply)
- `DestroySession(PAL::SessionID sessionID) -> ()`
- `EnsureSessionWithDataStoreIdentifierRemoved(WTF::UUID identifier) -> ()`
- `FetchWebsiteData(PAL::SessionID sessionID, OptionSet<WebKit::WebsiteDataType> websiteDataTypes, OptionSet<WebKit::WebsiteDataFetchOption> fetchOptions) -> (WebKit::WebsiteData websiteData)`
- `DeleteWebsiteData(PAL::SessionID sessionID, OptionSet<WebKit::WebsiteDataType> websiteDataTypes, WallTime modifiedSince, HashSet<WebCore::ProcessIdentifier> activeWebProcesses) -> ()`
- `DeleteWebsiteDataForOrigins(PAL::SessionID sessionID, OptionSet<WebKit::WebsiteDataType> websiteDataTypes, Vector<WebCore::SecurityOriginData> origins, Vector<String> cookieHostNames, Vector<String> HSTSCacheHostNames, Vector<WebCore::RegistrableDomain> registrableDomains) -> ()`
- `RenameOriginInWebsiteData(PAL::SessionID sessionID, WebCore::SecurityOriginData oldOrigin, WebCore::SecurityOriginData newOrigin, OptionSet<WebKit::WebsiteDataType> websiteDataTypes) -> ()`
- `WebsiteDataOriginDirectoryForTesting(PAL::SessionID sessionID, WebCore::ClientOrigin origin, OptionSet<WebKit::WebsiteDataType> websiteDataType) -> (String directory)`
- `DownloadRequest(PAL::SessionID sessionID, WebKit::DownloadID downloadID, WebCore::ResourceRequest request, std::optional<WebCore::SecurityOriginData> topOrigin, std::optional<WebKit::NavigatingToAppBoundDomain> isNavigatingToAppBoundDomain, String suggestedFilename)`
- `ResumeDownload(PAL::SessionID sessionID, WebKit::DownloadID downloadID, std::span<const uint8_t> resumeData, String path, WebKit::SandboxExtensionHandle sandboxExtensionHandle, WebKit::CallDownloadDidStart callDownloadDidStart, std::span<const uint8_t> activityAccessToken)`
- `CancelDownload(WebKit::DownloadID downloadID) -> (std::span<const uint8_t> resumeData)`
- `PublishDownloadProgress(WebKit::DownloadID downloadID, URL url, std::span<const uint8_t> bookmarkData, WebKit::UseDownloadPlaceholder useDownloadPlaceholder, std::span<const uint8_t> activityAccessToken)` (if (PLATFORM(COCOA) && HAVE(MODERN_DOWNLOADPROGRESS)))
- `PublishDownloadProgress(WebKit::DownloadID downloadID, URL url, WebKit::SandboxExtensionHandle sandboxExtensionHandle)` (if (PLATFORM(COCOA) && !HAVE(MODERN_DOWNLOADPROGRESS)))
- `DataTaskWithRequest(WebKit::WebPageProxyIdentifier pageID, PAL::SessionID sessionID, WebCore::ResourceRequest request, std::optional<WebCore::SecurityOriginData> topOrigin, IPC::FormDataReference requestBody) -> (std::optional<WebKit::DataTaskIdentifier> taskIdentifier)`
- `CancelDataTask(WebKit::DataTaskIdentifier taskIdentifier, PAL::SessionID sessionID) -> ()`
- `ApplicationDidEnterBackground()`
- `ApplicationWillEnterForeground()`
- `FlushCookies(PAL::SessionID sessionID) -> ()`
- `AllowSpecificHTTPSCertificateForHost(PAL::SessionID sessionID, WebCore::CertificateInfo certificate, String host)` (if !PLATFORM(COCOA))
- `AllowTLSCertificateChainForLocalPCMTesting(PAL::SessionID sessionID, WebCore::CertificateInfo certificate)`
- `SetCacheModel(WebKit::CacheModel cacheModel)`
- `SetCacheModelSynchronouslyForTesting(WebKit::CacheModel cacheModel) -> ()` (sync)
- `ProcessWillSuspendImminentlyForTestingSync() -> ()` (sync)
- `PrepareToSuspend(bool isSuspensionImminent, MonotonicTime estimatedSuspendTime) -> ()`
- `ProcessDidResume(bool forForegroundActivity)`
- `NotifyMediaStreamingActivity(bool activity)`
- `PreconnectTo(PAL::SessionID sessionID, WebKit::WebPageProxyIdentifier webPageProxyID, WebCore::PageIdentifier webPageID, WebCore::ResourceRequest request, WebCore::StoredCredentialsPolicy storedCredentialsPolicy, std::optional<WebKit::NavigatingToAppBoundDomain> isNavigatingToAppBoundDomain)`
- `SetInspectionForServiceWorkersAllowed(PAL::SessionID sessionID, bool inspectable)`
- `ClearPrevalentResource(PAL::SessionID sessionID, WebCore::RegistrableDomain resourceDomain) -> ()`
- `ClearUserInteraction(PAL::SessionID sessionID, WebCore::RegistrableDomain resourceDomain) -> ()`
- `DumpResourceLoadStatistics(PAL::SessionID sessionID) -> (String dumpedStatistics)`
- `SetTrackingPreventionEnabled(PAL::SessionID sessionID, bool enabled)`
- `UpdateStorageAccessPromptQuirks(Vector<WebCore::OrganizationStorageAccessPromptQuirk> organizationStorageAccessQuirks)`
- `SetResourceLoadStatisticsLogTestingEvent(bool enabled)`
- `UpdatePrevalentDomainsToBlockCookiesFor(PAL::SessionID sessionID, Vector<WebCore::RegistrableDomain> domainsToBlock) -> ()`
- `IsGrandfathered(PAL::SessionID sessionID, WebCore::RegistrableDomain targetDomain) -> (bool isGrandfathered)`
- `IsPrevalentResource(PAL::SessionID sessionID, WebCore::RegistrableDomain targetDomain) -> (bool isPrevalent)`
- `IsVeryPrevalentResource(PAL::SessionID sessionID, WebCore::RegistrableDomain targetDomain) -> (bool isVeryPrevalent)`
- `SetLastSeen(PAL::SessionID sessionID, WebCore::RegistrableDomain resourceDomain, Seconds seconds) -> ()`
- `MergeStatisticForTesting(PAL::SessionID sessionID, WebCore::RegistrableDomain resourceDomain, WebCore::RegistrableDomain topFrameDomain1, WebCore::RegistrableDomain topFrameDomain2, Seconds lastSeen, bool hadUserInteraction, Seconds mostRecentUserInteraction, bool isGrandfathered, bool isPrevalent, bool isVeryPrevalent, uint64_t dataRecordsRemoved) -> ()`
- `InsertExpiredStatisticForTesting(PAL::SessionID sessionID, WebCore::RegistrableDomain resourceDomain, uint64_t numberOfOperatingDaysPassed, bool hadUserInteraction, bool isScheduledForAllButCookieDataRemoval, bool isPrevalent) -> ()`
- `SetPrevalentResource(PAL::SessionID sessionID, WebCore::RegistrableDomain resourceDomain) -> ()`
- `SetPrevalentResourceForDebugMode(PAL::SessionID sessionID, WebCore::RegistrableDomain resourceDomain) -> ()`
- `IsResourceLoadStatisticsEphemeral(PAL::SessionID sessionID) -> (bool isEphemeral)`
- `HadUserInteraction(PAL::SessionID sessionID, WebCore::RegistrableDomain resourceDomain) -> (bool hadUserInteraction)`
- `IsRelationshipOnlyInDatabaseOnce(PAL::SessionID sessionID, WebCore::RegistrableDomain subDomain, WebCore::RegistrableDomain topDomain) -> (bool hadUserInteraction)`
- `HasLocalStorage(PAL::SessionID sessionID, WebCore::RegistrableDomain resourceDomain) -> (bool hadUserInteraction)`
- `GetAllStorageAccessEntries(PAL::SessionID sessionID) -> (Vector<String> domains)`
- `IsRegisteredAsRedirectingTo(PAL::SessionID sessionID, WebCore::RegistrableDomain redirectedFromDomain, WebCore::RegistrableDomain redirectedToDomain) -> (bool isRedirectingTo)`
- `IsRegisteredAsSubFrameUnder(PAL::SessionID sessionID, WebCore::RegistrableDomain subFrameDomain, WebCore::RegistrableDomain topFrameDomain) -> (bool isSubframeUnder)`
- `IsRegisteredAsSubresourceUnder(PAL::SessionID sessionID, WebCore::RegistrableDomain subresourceDomain, WebCore::RegistrableDomain topFrameDomain) -> (bool isSubresourceUnder)`
- `DomainIDExistsInDatabase(PAL::SessionID sessionID, int domainID) -> (bool exists)`
- `LogFrameNavigation(PAL::SessionID sessionID, WebCore::RegistrableDomain targetDomain, WebCore::RegistrableDomain topFrameDomain, WebCore::RegistrableDomain sourceDomain, bool isRedirect, bool isMainFrame, Seconds delayAfterMainFrameDocumentLoad, bool wasPotentiallyInitiatedByUser)`
- `LogUserInteraction(PAL::SessionID sessionID, WebCore::RegistrableDomain topFrameDomain) -> ()`
- `ResetParametersToDefaultValues(PAL::SessionID sessionID) -> ()`
- `ScheduleClearInMemoryAndPersistent(PAL::SessionID sessionID, std::optional<WallTime> modifiedSince, WebKit::ShouldGrandfatherStatistics shouldGrandfather) -> ()`
- `ScheduleCookieBlockingUpdate(PAL::SessionID sessionID) -> ()`
- `ScheduleStatisticsAndDataRecordsProcessing(PAL::SessionID sessionID) -> ()`
- `StatisticsDatabaseHasAllTables(PAL::SessionID sessionID) -> (bool hasAllTables)`
- `SetCacheMaxAgeCapForPrevalentResources(PAL::SessionID sessionID, Seconds seconds) -> ()`
- `SetGrandfathered(PAL::SessionID sessionID, WebCore::RegistrableDomain resourceDomain, bool isGrandfathered) -> ()`
- `GetResourceLoadStatisticsDataSummary(PAL::SessionID sessionID) -> (Vector<WebKit::ITPThirdPartyData> thirdPartyData)`
- `SetGrandfatheringTime(PAL::SessionID sessionID, Seconds seconds) -> ()`
- `SetMaxStatisticsEntries(PAL::SessionID sessionID, uint64_t maximumEntryCount) -> ()`
- `SetMinimumTimeBetweenDataRecordsRemoval(PAL::SessionID sessionID, Seconds seconds) -> ()`
- `SetPruneEntriesDownTo(PAL::SessionID sessionID, uint64_t maximumEntryCount) -> ()`
- `SetShouldClassifyResourcesBeforeDataRecordsRemoval(PAL::SessionID sessionID, bool value) -> ()`
- `SetResourceLoadStatisticsTimeAdvanceForTesting(PAL::SessionID sessionID, Seconds time) -> ()`
- `SetIsRunningResourceLoadStatisticsTest(PAL::SessionID sessionID, bool value) -> ()`
- `SetResourceLoadStatisticsDebugMode(PAL::SessionID sessionID, bool debugMode) -> ()`
- `SetVeryPrevalentResource(PAL::SessionID sessionID, WebCore::RegistrableDomain resourceDomain) -> ()`
- `SetSubframeUnderTopFrameDomain(PAL::SessionID sessionID, WebCore::RegistrableDomain subFrameDomain, WebCore::RegistrableDomain topFrameDomain) -> ()`
- `SetSubresourceUnderTopFrameDomain(PAL::SessionID sessionID, WebCore::RegistrableDomain subresourceDomain, WebCore::RegistrableDomain topFrameDomain) -> ()`
- `SetSubresourceUniqueRedirectTo(PAL::SessionID sessionID, WebCore::RegistrableDomain subresourceDomain, WebCore::RegistrableDomain redirectedToDomain) -> ()`
- `SetSubresourceUniqueRedirectFrom(PAL::SessionID sessionID, WebCore::RegistrableDomain subresourceDomain, WebCore::RegistrableDomain redirectedFromDomain) -> ()`
- `SetTimeToLiveUserInteraction(PAL::SessionID sessionID, Seconds seconds) -> ()`
- `SetTopFrameUniqueRedirectTo(PAL::SessionID sessionID, WebCore::RegistrableDomain topFrameDomain, WebCore::RegistrableDomain redirectedToDomain) -> ()`
- `SetTopFrameUniqueRedirectFrom(PAL::SessionID sessionID, WebCore::RegistrableDomain topFrameDomain, WebCore::RegistrableDomain redirectedFromDomain) -> ()`
- `ResetCacheMaxAgeCapForPrevalentResources(PAL::SessionID sessionID) -> ()`
- `DidCommitCrossSiteLoadWithDataTransfer(PAL::SessionID sessionID, WebCore::RegistrableDomain fromDomain, WebCore::RegistrableDomain toDomain, OptionSet<WebCore::CrossSiteNavigationDataTransferFlag> navigationDataTransfer, WebKit::WebPageProxyIdentifier webPageProxyID, WebCore::PageIdentifier webPageID, WebKit::DidFilterKnownLinkDecoration didFilterKnownLinkDecoration)`
- `SetCrossSiteLoadWithLinkDecorationForTesting(PAL::SessionID sessionID, WebCore::RegistrableDomain fromDomain, WebCore::RegistrableDomain toDomain, WebKit::DidFilterKnownLinkDecoration didFilterKnownLinkDecoration) -> ()`
- `ResetCrossSiteLoadsWithLinkDecorationForTesting(PAL::SessionID sessionID) -> ()`
- `GrantStorageAccessForTesting(PAL::SessionID sessionID, Vector<WebCore::RegistrableDomain> subFrameDomain, WebCore::RegistrableDomain topFrameDomain) -> ()`
- `DeleteCookiesForTesting(PAL::SessionID sessionID, WebCore::RegistrableDomain domain, bool includeHttpOnlyCookies) -> ()`
- `HasIsolatedSession(PAL::SessionID sessionID, WebCore::RegistrableDomain domain) -> (bool hasIsolatedSession)`
- `CloseITPDatabase(PAL::SessionID sessionID) -> ()`
- `SetAppBoundDomainsForResourceLoadStatistics(PAL::SessionID sessionID, HashSet<WebCore::RegistrableDomain> appBoundDomains) -> ()` (if ENABLE(APP_BOUND_DOMAINS))
- `SetManagedDomainsForResourceLoadStatistics(PAL::SessionID sessionID, HashSet<WebCore::RegistrableDomain> appBoundDomains) -> ()` (if ENABLE(MANAGED_DOMAINS))
- `SetShouldDowngradeReferrerForTesting(bool enabled) -> ()`
- `SetThirdPartyCookieBlockingMode(PAL::SessionID sessionID, WebCore::ThirdPartyCookieBlockingMode blockingMode) -> ()`
- `SetShouldEnbleSameSiteStrictEnforcementForTesting(PAL::SessionID sessionID, WebCore::SameSiteStrictEnforcementEnabled enabled) -> ()`
- `SetFirstPartyWebsiteDataRemovalModeForTesting(PAL::SessionID sessionID, WebCore::FirstPartyWebsiteDataRemovalMode mode) -> ()`
- `SetToSameSiteStrictCookiesForTesting(PAL::SessionID sessionID, WebCore::RegistrableDomain domain) -> ()`
- `SetFirstPartyHostCNAMEDomainForTesting(PAL::SessionID sessionID, String firstPartyHost, WebCore::RegistrableDomain cnameDomain) -> ()`
- `SetThirdPartyCNAMEDomainForTesting(PAL::SessionID sessionID, WebCore::RegistrableDomain domain) -> ()`
- `SetPrivateClickMeasurementDebugMode(PAL::SessionID sessionID, bool debugMode)`
- `SetBlobRegistryTopOriginPartitioningEnabled(PAL::SessionID sessionID, bool enabled)`
- `SetShouldSendPrivateTokenIPCForTesting(PAL::SessionID sessionID, bool enabled)`
- `SetOptInCookiePartitioningEnabled(PAL::SessionID sessionID, bool enabled)` (if HAVE(ALLOW_ONLY_PARTITIONED_COOKIES))
- `SetSessionIsControlledByAutomation(PAL::SessionID sessionID, bool controlled)`
- `RegisterURLSchemeAsSecure(String scheme)`
- `RegisterURLSchemeAsBypassingContentSecurityPolicy(String scheme)`
- `RegisterURLSchemeAsLocal(String scheme)`
- `RegisterURLSchemeAsNoAccess(String scheme)`
- `SyncLocalStorage() -> ()`
- `StoreServiceWorkerRegistrations(PAL::SessionID sessionID) -> ()`
- `StorePrivateClickMeasurement(PAL::SessionID sessionID, WebCore::PrivateClickMeasurement privateClickMeasurement)`
- `DumpPrivateClickMeasurement(PAL::SessionID sessionID) -> (String privateClickMeasurementState)`
- `ClearPrivateClickMeasurement(PAL::SessionID sessionID) -> ()`
- `SetPrivateClickMeasurementOverrideTimerForTesting(PAL::SessionID sessionID, bool value) -> ()`
- `MarkAttributedPrivateClickMeasurementsAsExpiredForTesting(PAL::SessionID sessionID) -> ()`
- `SetPrivateClickMeasurementEphemeralMeasurementForTesting(PAL::SessionID sessionID, bool value) -> ()`
- `SimulatePrivateClickMeasurementSessionRestart(PAL::SessionID sessionID) -> ()`
- `SetPrivateClickMeasurementTokenPublicKeyURLForTesting(PAL::SessionID sessionID, URL url) -> ()`
- `SetPrivateClickMeasurementTokenSignatureURLForTesting(PAL::SessionID sessionID, URL url) -> ()`
- `SetPrivateClickMeasurementAttributionReportURLsForTesting(PAL::SessionID sessionID, URL sourceURL, URL destinationURL) -> ()`
- `MarkPrivateClickMeasurementsAsExpiredForTesting(PAL::SessionID sessionID) -> ()`
- `SetPCMFraudPreventionValuesForTesting(PAL::SessionID sessionID, String secretToken, String unlinkableToken, String signature, String keyID) -> ()`
- `SetPrivateClickMeasurementAppBundleIDForTesting(PAL::SessionID sessionID, String appBundleIDForTesting) -> ()`
- `ClosePCMDatabase(PAL::SessionID sessionID) -> ()`
- `SetServiceWorkerFetchTimeoutForTesting(Seconds seconds) -> ()` (sync)
- `ResetServiceWorkerFetchTimeoutForTesting() -> ()` (sync)
- `TerminateIdleServiceWorkers(WebCore::ProcessIdentifier processIdentifier) -> ()`
- `ResetQuota(PAL::SessionID sessionID) -> ()`
- `SetOriginQuotaRatioEnabledForTesting(PAL::SessionID sessionID, bool enabled) -> ()`
- `SetBackupExclusionPeriodForTesting(PAL::SessionID sessionID, Seconds period) -> ()` (if PLATFORM(IOS_FAMILY))
- `ResetStoragePersistedState(PAL::SessionID sessionID) -> ()`
- `CloneSessionStorageForWebPage(PAL::SessionID sessionID, WebKit::WebPageProxyIdentifier sourcePage, WebKit::WebPageProxyIdentifier destinationPage)`
- `DidIncreaseQuota(PAL::SessionID sessionID, WebCore::ClientOrigin origin, WebKit::QuotaIncreaseRequestIdentifier identifier, std::optional<uint64_t> newQuota)`
- `HasAppBoundSession(PAL::SessionID sessionID) -> (bool hasAppBoundSession)` (if ENABLE(APP_BOUND_DOMAINS))
- `ClearAppBoundSession(PAL::SessionID sessionID) -> ()` (if ENABLE(APP_BOUND_DOMAINS))
- `DisableServiceWorkerEntitlement()` (if PLATFORM(IOS_FAMILY) && !PLATFORM(MACCATALYST))
- `ClearServiceWorkerEntitlementOverride() -> ()` (if PLATFORM(IOS_FAMILY) && !PLATFORM(MACCATALYST))
- `UpdateBundleIdentifier(String bundleIdentifier) -> ()`
- `ClearBundleIdentifier() -> ()`
- `AppPrivacyReportTestingData(PAL::SessionID sessionID) -> (WebKit::AppPrivacyReportTestingData data)` (if PLATFORM(COCOA))
- `ClearAppPrivacyReportTestingData(PAL::SessionID sessionID) -> ()` (if PLATFORM(COCOA))
- `AddWebPageNetworkParameters(PAL::SessionID sessionID, WebKit::WebPageProxyIdentifier pageID, WebKit::WebPageNetworkParameters parameters)`
- `RemoveWebPageNetworkParameters(PAL::SessionID sessionID, WebKit::WebPageProxyIdentifier pageID)`
- `CountNonDefaultSessionSets(PAL::SessionID sessionID) -> (size_t count)`
- `AllowFileAccessFromWebProcess(WebCore::ProcessIdentifier processIdentifier, String url) -> ()`
- `AllowFilesAccessFromWebProcess(WebCore::ProcessIdentifier processIdentifier, Vector<String> urls) -> ()` (ReplyCanDispatchOutOfOrder)
- `TerminateRemoteWorkerContextConnectionWhenPossible(WebKit::RemoteWorkerType workerType, PAL::SessionID sessionID, WebCore::RegistrableDomain registrableDomain, WebCore::ProcessIdentifier processIdentifier)`
- `RunningOrTerminatingServiceWorkerCountForTesting(PAL::SessionID sessionID) -> (unsigned count)`
- `GetPendingPushMessage(PAL::SessionID sessionID) -> (std::optional<WebKit::WebPushMessage> message)`
- `GetPendingPushMessages(PAL::SessionID sessionID) -> (Vector<WebKit::WebPushMessage> messages)`
- `ProcessPushMessage(PAL::SessionID sessionID, WebKit::WebPushMessage pushMessage, WebCore::PushPermissionState pushPermissionState, bool builtInNotificationsEnabled) -> (bool didSucceed, std::optional<WebCore::NotificationPayload> displayPayload)`
- `ProcessNotificationEvent(WebCore::NotificationData data, WebCore::NotificationEventType eventType) -> (bool didSucceed)`
- `GetAllBackgroundFetchIdentifiers(PAL::SessionID sessionID) -> (Vector<String> fetches)`
- `GetBackgroundFetchState(PAL::SessionID sessionID, String identifier) -> (std::optional<WebKit::BackgroundFetchState> state)`
- `AbortBackgroundFetch(PAL::SessionID sessionID, String identifier) -> ()`
- `PauseBackgroundFetch(PAL::SessionID sessionID, String identifier) -> ()`
- `ResumeBackgroundFetch(PAL::SessionID sessionID, String identifier) -> ()`
- `ClickBackgroundFetch(PAL::SessionID sessionID, String identifier) -> ()`
- `SetPushAndNotificationsEnabledForOrigin(PAL::SessionID sessionID, WebCore::SecurityOriginData origin, bool enabled) -> ()`
- `RemovePushSubscriptionsForOrigin(PAL::SessionID sessionID, WebCore::SecurityOriginData origin) -> (unsigned unsubscribedCount)`
- `HasPushSubscriptionForTesting(PAL::SessionID sessionID, URL scopeURL) -> (bool hasSubscription)`
- `SetEmulatedConditions(PAL::SessionID sessionID, std::optional<int64_t> bytesPerSecondLimit)` (if ENABLE(INSPECTOR_NETWORK_THROTTLING))
- `ClearProxyConfigData(PAL::SessionID sessionID)` (if HAVE(NW_PROXY_CONFIG))
- `SetProxyConfigData(PAL::SessionID sessionID, Vector<std::pair<Vector<uint8_t>, WTF::UUID>> proxyConfigurations)` (if HAVE(NW_PROXY_CONFIG))
- `SetStorageSiteValidationEnabled(PAL::SessionID sessionID, bool enabled)`
- `SetPersistedDomains(PAL::SessionID sessionsID, HashSet<WebCore::RegistrableDomain> domains)`
- `GetAppBadgeForTesting(PAL::SessionID sessionID) -> (std::optional<uint64_t> badge)`
- `FetchLocalStorage(PAL::SessionID sessionID) -> (HashMap<WebCore::ClientOrigin, HashMap<String, String>> localStorageMap)`
- `RestoreLocalStorage(PAL::SessionID sessionID, HashMap<WebCore::ClientOrigin, HashMap<String, String>> localStorageMap) -> (bool succeeded)`
- `FetchSessionStorage(PAL::SessionID sessionID, WebKit::WebPageProxyIdentifier pageID) -> (HashMap<WebCore::ClientOrigin, HashMap<String, String>> sessionStorageMap)`
- `RestoreSessionStorage(PAL::SessionID sessionID, WebKit::WebPageProxyIdentifier pageID, HashMap<WebCore::ClientOrigin, HashMap<String, String>> localStorageMap) -> (bool succeeded)`
- `SetShouldRelaxThirdPartyCookieBlockingForPage(WebKit::WebPageProxyIdentifier pageID)`

## `WebCookieManager` - UI -> Networking

`NetworkProcess/Cookies/WebCookieManager.messages.in`

- `GetHostnamesWithCookies(PAL::SessionID sessionID) -> (Vector<String> hostnames)`
- `DeleteCookiesForHostnames(PAL::SessionID sessionID, Vector<String> hostnames) -> ()`
- `DeleteAllCookies(PAL::SessionID sessionID) -> ()`
- `SetCookie(PAL::SessionID sessionID, Vector<WebCore::Cookie> cookie) -> ()`
- `SetCookies(PAL::SessionID sessionID, Vector<WebCore::Cookie> cookies, URL url, URL mainDocumentURL) -> ()`
- `GetAllCookies(PAL::SessionID sessionID) -> (Vector<WebCore::Cookie> cookies)`
- `GetCookies(PAL::SessionID sessionID, URL url) -> (Vector<WebCore::Cookie> cookies)`
- `DeleteCookie(PAL::SessionID sessionID, WebCore::Cookie cookie) -> ()`
- `DeleteAllCookiesModifiedSince(PAL::SessionID sessionID, WallTime time) -> ()`
- `SetHTTPCookieAcceptPolicy(PAL::SessionID sessionID, WebCore::HTTPCookieAcceptPolicy policy) -> ()`
- `GetHTTPCookieAcceptPolicy(PAL::SessionID sessionID) -> (WebCore::HTTPCookieAcceptPolicy policy)`
- `StartObservingCookieChanges(PAL::SessionID sessionID)`
- `StopObservingCookieChanges(PAL::SessionID sessionID)`
- `ReplaceCookies(PAL::SessionID sessionID, Vector<WebCore::Cookie> cookies) -> ()` (if USE(SOUP))
- `SetCookiePersistentStorage(PAL::SessionID sessionID, String storagePath, WebKit::SoupCookiePersistentStorageType storageType)` (if USE(SOUP))

## `ModelProcess` - UI -> Model

`ModelProcess/ModelProcess.messages.in`

- `InitializeModelProcess(WebKit::ModelProcessCreationParameters processCreationParameters) -> ()`
- `CreateModelConnectionToWebProcess(WebCore::ProcessIdentifier processIdentifier, PAL::SessionID sessionID, IPC::ConnectionHandle connectionHandle, WebKit::ModelProcessConnectionParameters parameters) -> ()` (AllowedWhenWaitingForSyncReply)
- `SharedPreferencesForWebProcessDidChange(WebCore::ProcessIdentifier processIdentifier, WebKit::SharedPreferencesForWebProcess sharedPreferencesForWebProcess) -> ()`
- `PrepareToSuspend(bool isSuspensionImminent, MonotonicTime estimatedSuspendTime) -> ()`
- `ProcessDidResume()`
- `AddSession(PAL::SessionID sessionID)`
- `RemoveSession(PAL::SessionID sessionID)`
- `WebProcessConnectionCountForTesting() -> (uint64_t count)`

## `GPUProcessConnection` - GPU -> WebContent

`WebProcess/GPU/GPUProcessConnection.messages.in`

- `DidInitialize(std::optional<WebKit::GPUProcessConnectionInfo> info)` (CanDispatchOutOfOrder)
- `DidReceiveRemoteCommand(WebCore::PlatformMediaSessionRemoteControlCommandType type, WebCore::PlatformMediaSession::RemoteCommandArgument argument)`
- `BeginRoutingArbitrationWithCategory(WebCore::AudioSessionCategory category) -> (WebCore::AudioSessionRoutingArbitrationError error, WebCore::AudioSessionRoutingArbitrationClient::DefaultRouteChanged defaultRouteChanged)` (if ENABLE(ROUTING_ARBITRATION))
- `EndRoutingArbitration()` (if ENABLE(ROUTING_ARBITRATION))
- `ResetAudioMediaStreamTrackRendererInternalUnit(WebKit::AudioMediaStreamTrackRendererInternalUnitIdentifier identifier)` (if ENABLE(MEDIA_STREAM) && PLATFORM(COCOA))

## `LibWebRTCCodecs` - GPU -> WebContent

`WebProcess/GPU/webrtc/LibWebRTCCodecs.messages.in`

- `FailedDecoding(WebKit::VideoDecoderIdentifier identifier)`
- `CompletedDecoding(WebKit::VideoDecoderIdentifier identifier, int64_t timeStamp, int64_t timeStampNs, WebKit::RemoteVideoFrameProxyProperties frame)`
- `CompletedDecodingCV(WebKit::VideoDecoderIdentifier identifier, int64_t timeStamp, int64_t timeStampNs, RetainPtr<CVPixelBufferRef> pixelBuffer)`
- `CompletedEncoding(WebKit::VideoEncoderIdentifier identifier, std::span<const uint8_t> data, webrtc::WebKitEncodedFrameInfo info)`
- `SetEncodingConfiguration(WebKit::VideoEncoderIdentifier identifier, std::span<const uint8_t> description, std::optional<WebCore::PlatformVideoColorSpace> colorSpace)`

## `MediaPlayerPrivateRemote` - GPU -> WebContent

`WebProcess/GPU/media/MediaPlayerPrivateRemote.messages.in`

- `NetworkStateChanged(WebKit::RemoteMediaPlayerState state)`
- `ReadyStateChanged(WebKit::RemoteMediaPlayerState state, WebCore::MediaPlayerReadyState readyStat)`
- `FirstVideoFrameAvailable()`
- `VolumeChanged(double volume)`
- `MuteChanged(bool mute)`
- `Seeked(WebKit::MediaTimeUpdateData timeData)`
- `TimeChanged(WebKit::RemoteMediaPlayerState state, WebKit::MediaTimeUpdateData timeData)`
- `DurationChanged(WebKit::RemoteMediaPlayerState state)`
- `RateChanged(double rate, WebKit::MediaTimeUpdateData timeData)`
- `PlaybackStateChanged(bool paused, WebKit::MediaTimeUpdateData timeData)`
- `EngineFailedToLoad(int64_t platformErrorCode)`
- `UpdateCachedState(WebKit::RemoteMediaPlayerState state)`
- `UpdatePlaybackQualityMetrics(WebCore::VideoPlaybackQualityMetrics metrics)`
- `CharacteristicChanged(WebKit::RemoteMediaPlayerState state)`
- `SizeChanged(WebCore::FloatSize naturalSize)`
- `RenderingModeChanged()`
- `CurrentTimeChanged(WebKit::MediaTimeUpdateData timeData)`
- `AddRemoteAudioTrack(WebKit::AudioTrackPrivateRemoteConfiguration configuration)`
- `RemoveRemoteAudioTrack(WebCore::TrackID trackID)`
- `RemoteAudioTrackConfigurationChanged(WebCore::TrackID trackID, WebKit::AudioTrackPrivateRemoteConfiguration configuration)`
- `AddRemoteVideoTrack(WebKit::VideoTrackPrivateRemoteConfiguration configuration)`
- `RemoveRemoteVideoTrack(WebCore::TrackID trackID)`
- `RemoteVideoTrackConfigurationChanged(WebCore::TrackID trackID, WebKit::VideoTrackPrivateRemoteConfiguration configuration)`
- `AddRemoteTextTrack(WebKit::TextTrackPrivateRemoteConfiguration configuration)`
- `RemoveRemoteTextTrack(WebCore::TrackID trackID)`
- `RemoteTextTrackConfigurationChanged(WebCore::TrackID trackID, WebKit::TextTrackPrivateRemoteConfiguration configuration)`
- `ParseWebVTTFileHeader(WebCore::TrackID trackID, String header)`
- `ParseWebVTTCueData(WebCore::TrackID trackID, std::span<const uint8_t> data)`
- `ParseWebVTTCueDataStruct(WebCore::TrackID trackID, WebCore::ISOWebVTTCue cueData)`
- `AddDataCue(WebCore::TrackID trackID, MediaTime start, MediaTime end, std::span<const uint8_t> data)`
- `AddDataCueWithType(WebCore::TrackID trackID, MediaTime start, MediaTime end, WebCore::SerializedPlatformDataCueValue cueData, String type)` (if ENABLE(DATACUE_VALUE))
- `UpdateDataCue(WebCore::TrackID trackID, MediaTime start, MediaTime end, WebCore::SerializedPlatformDataCueValue cueData)` (if ENABLE(DATACUE_VALUE))
- `RemoveDataCue(WebCore::TrackID trackID, MediaTime start, MediaTime end, WebCore::SerializedPlatformDataCueValue cueData)` (if ENABLE(DATACUE_VALUE))
- `AddGenericCue(WebCore::TrackID trackID, WebCore::GenericCueData cue)`
- `UpdateGenericCue(WebCore::TrackID trackID, WebCore::GenericCueData cue)`
- `RemoveGenericCue(WebCore::TrackID trackID, WebCore::GenericCueData cue)`
- `RequestResource(WebKit::RemoteMediaResourceIdentifier remoteMediaResourceIdentifier, WebCore::ResourceRequest request, WebCore::PlatformMediaResourceLoader::LoadOptions options)`
- `RemoveResource(WebKit::RemoteMediaResourceIdentifier remoteMediaResourceIdentifier)`
- `SendH2Ping(URL url) -> (Expected<Seconds, WebCore::ResourceError> result)`
- `ResourceNotSupported()`
- `ActiveSourceBuffersChanged()`
- `WaitingForKeyChanged(bool waitingForKey)` (if ENABLE(ENCRYPTED_MEDIA))
- `InitializationDataEncountered(String initDataType, std::span<const uint8_t> initData)` (if ENABLE(ENCRYPTED_MEDIA))
- `MediaPlayerKeyNeeded(std::span<const uint8_t> message)` (if ENABLE(LEGACY_ENCRYPTED_MEDIA))
- `CurrentPlaybackTargetIsWirelessChanged(bool isCurrentPlaybackTargetWireless)` (if ENABLE(WIRELESS_PLAYBACK_TARGET))
- `GetRawCookies(URL url) -> (Vector<WebCore::Cookie> result)` (if PLATFORM(IOS_FAMILY))
- `PushVideoFrameMetadata(WebCore::VideoFrameMetadata metadata, WebKit::RemoteVideoFrameProxyProperties frameProperties)` (if PLATFORM(COCOA))
- `LayerHostingContextIdChanged(std::optional<WebKit::LayerHostingContextID> inlineLayerHostingContextId, WebCore::FloatSize presentationSize)` (if PLATFORM(COCOA))
- `CommitAllTransactions() -> ()`

## `MediaSourcePrivateRemoteMessageReceiver` - GPU -> WebContent

`WebProcess/GPU/media/MediaSourcePrivateRemoteMessageReceiver.messages.in`

- `ProxyWaitForTarget(WebCore::SeekTarget target) -> (Expected<MediaTime, WebCore::PlatformMediaError> seekedTime)`
- `ProxySeekToTime(MediaTime time) -> (Expected<void, WebCore::PlatformMediaError> result)`

## `RemoteAudioHardwareListener` - GPU -> WebContent

`WebProcess/GPU/media/RemoteAudioHardwareListener.messages.in`

- `AudioHardwareDidBecomeActive()`
- `AudioHardwareDidBecomeInactive()`
- `AudioOutputDeviceChanged(size_t bufferSizeMinimum, size_t bufferSizeMaximum)`

## `RemoteAudioSession` - GPU -> WebContent

`WebProcess/GPU/media/RemoteAudioSession.messages.in`

- `ConfigurationChanged(WebKit::RemoteAudioSessionConfiguration configuration)`
- `BeginInterruptionRemote()`
- `EndInterruptionRemote(WebCore::AudioSession::MayResume flags)`

## `RemoteAudioSourceProviderManager` - GPU -> WebContent

`WebProcess/GPU/media/RemoteAudioSourceProviderManager.messages.in`

- `AudioStorageChanged(WebCore::MediaPlayerIdentifier id, WebKit::ConsumerSharedCARingBufferHandle storageHandle, WebCore::CAAudioStreamDescription description)`
- `AudioSamplesAvailable(WebCore::MediaPlayerIdentifier id, uint64_t startFrame, uint64_t numberOfFrames)`

## `RemoteCDMInstance` - GPU -> WebContent

`WebProcess/GPU/media/RemoteCDMInstance.messages.in`

- `UnrequestedInitializationDataReceived(String type, Ref<WebCore::SharedBuffer> initData)`

## `RemoteCDMInstanceSession` - GPU -> WebContent

`WebProcess/GPU/media/RemoteCDMInstanceSession.messages.in`

- `UpdateKeyStatuses(WebCore::CDMInstanceSession::KeyStatusVector keyStatuses)`
- `SendMessage(WebCore::CDMMessageType type, RefPtr<WebCore::SharedBuffer> message)`
- `SessionIdChanged(String sessionId)`

## `RemoteCaptureSampleManager` - GPU -> WebContent

`WebProcess/cocoa/RemoteCaptureSampleManager.messages.in`

- `AudioStorageChanged(WebCore::RealtimeMediaSourceIdentifier id, WebKit::ConsumerSharedCARingBufferHandle storageHandle, WebCore::CAAudioStreamDescription description, IPC::Semaphore captureSemaphore, MediaTime mediaTime, size_t frameChunkSize)`
- `VideoFrameAvailable(WebCore::RealtimeMediaSourceIdentifier id, WebKit::RemoteVideoFrameProxyProperties sample, WebCore::VideoFrameTimeMetadata metadata)`
- `VideoFrameAvailableCV(WebCore::RealtimeMediaSourceIdentifier id, RetainPtr<CVPixelBufferRef> pixelBuffer, WebCore::VideoFrameRotation rotation, bool mirrored, MediaTime presentationTime, WebCore::VideoFrameTimeMetadata metadata)`

## `RemoteGPUProxy` - GPU -> WebContent

`WebProcess/GPU/graphics/WebGPU/RemoteGPUProxy.messages.in`

- `WasCreated(bool didSucceed, IPC::Semaphore streamWakeUpSemaphore, IPC::Semaphore streamClientWaitSemaphore)` (CanDispatchOutOfOrder)

## `RemoteGraphicsContextGLProxy` - GPU -> WebContent

`WebProcess/GPU/graphics/RemoteGraphicsContextGLProxy.messages.in`

- `WasCreated(IPC::Semaphore streamWakeUpSemaphore, IPC::Semaphore streamClientWaitSemaphore, std::optional<WebKit::RemoteGraphicsContextGLInitializationState> initializationState)` (CanDispatchOutOfOrder)
- `WasLost()`
- `addDebugMessage(GCGLenum type, GCGLenum id, GCGLenum severity, String message)` (CanDispatchOutOfOrder)

## `RemoteImageBufferProxy` - GPU -> WebContent

`WebProcess/GPU/graphics/RemoteImageBufferProxy.messages.in`

- `DidCreateBackend(std::optional<WebKit::ImageBufferBackendHandle> handle)` (CanDispatchOutOfOrder)

## `RemoteImageBufferSetProxy` - GPU -> WebContent

`WebProcess/GPU/graphics/RemoteImageBufferSetProxy.messages.in`

- `DidPrepareForDisplay(WebKit::ImageBufferSetPrepareBufferForDisplayOutputData outputData, WebKit::RenderingUpdateID renderingUpdateID)` (if PLATFORM(COCOA))

## `RemoteImageDecoderAVFManager` - GPU -> WebContent

`WebProcess/GPU/media/RemoteImageDecoderAVFManager.messages.in`

- `EncodedDataStatusChanged(WebCore::ImageDecoderIdentifier identifier, size_t frameCount, WebCore::IntSize size, bool hasTrack)`

## `RemoteLegacyCDMSession` - GPU -> WebContent

`WebProcess/GPU/media/RemoteLegacyCDMSession.messages.in`

- `SendMessage(RefPtr<WebCore::SharedBuffer> message, String destinationURL)`
- `SendError(WebCore::LegacyCDMSessionClient::MediaKeyErrorCode errorCode, uint32_t systemCode)`

## `RemoteMediaSessionHelper` - GPU -> WebContent

`WebProcess/GPU/media/ios/RemoteMediaSessionHelper.messages.in`

- `ApplicationWillEnterForeground(WebKit::RemoteMediaSessionHelper::SuspendedUnderLock suspendedUnderLock)`
- `ApplicationDidEnterBackground(WebKit::RemoteMediaSessionHelper::SuspendedUnderLock suspendedUnderLock)`
- `ApplicationWillBecomeInactive()`
- `ApplicationDidBecomeActive()`
- `ExternalOutputDeviceAvailableDidChange(WebKit::RemoteMediaSessionHelper::HasAvailableTargets hasAvailableTargets)`
- `IsPlayingToAutomotiveHeadUnitDidChange(WebKit::RemoteMediaSessionHelper::PlayingToAutomotiveHeadUnit isPlayingToAutomotiveHeadUnit)`
- `ActiveAudioRouteDidChange(WebKit::RemoteMediaSessionHelper::ShouldPause shouldPause)`
- `ActiveVideoRouteDidChange(WebKit::RemoteMediaSessionHelper::SupportsAirPlayVideo supportsAirPlayVideo, WebKit::MediaPlaybackTargetContextSerialized target)`
- `ActiveAudioRouteSupportsSpatialPlaybackDidChange(WebKit::RemoteMediaSessionHelper::SupportsSpatialAudioPlayback supportsSpatialPlayback)`

## `RemoteRemoteCommandListener` - GPU -> WebContent

`WebProcess/GPU/media/RemoteRemoteCommandListener.messages.in`

- `DidReceiveRemoteControlCommand(WebCore::PlatformMediaSessionRemoteControlCommandType command, WebCore::PlatformMediaSession::RemoteCommandArgument argument)`

## `RemoteRenderingBackendProxy` - GPU -> WebContent

`WebProcess/GPU/graphics/RemoteRenderingBackendProxy.messages.in`

- `DidFinalizeRenderingUpdate(WebKit::RenderingUpdateID didRenderingUpdateID)`
- `DidInitialize(IPC::Semaphore wakeUpSemaphore, IPC::Semaphore clientWaitSemaphore)` (CanDispatchOutOfOrder)
- `DidMarkLayersAsVolatile(WebKit::MarkSurfacesAsVolatileRequestIdentifier requestIdentifier, Vector<std::pair<WebKit::RemoteImageBufferSetIdentifier, OptionSet<WebKit::BufferInSetType>>> markedBufferSets, bool didMarkAllLayersAsVolatile)`

## `RemoteVideoFrameObjectHeapProxyProcessor` - GPU -> WebContent

`WebProcess/GPU/webrtc/RemoteVideoFrameObjectHeapProxyProcessor.messages.in`

- `SetSharedVideoFrameSemaphore(IPC::Semaphore semaphore)`
- `SetSharedVideoFrameMemory(WebCore::SharedMemory::Handle storageHandle)`
- `NewVideoFrameBuffer(WebKit::RemoteVideoFrameIdentifier identifier, std::optional<WebKit::SharedVideoFrame::Buffer> frame)`
- `NewConvertedVideoFrameBuffer(std::optional<WebKit::SharedVideoFrame::Buffer> frame)`

## `SampleBufferDisplayLayer` - GPU -> WebContent

`WebProcess/GPU/webrtc/SampleBufferDisplayLayer.messages.in`

- `SetDidFail(bool value)`

## `SourceBufferPrivateRemoteMessageReceiver` - GPU -> WebContent

`WebProcess/GPU/media/SourceBufferPrivateRemoteMessageReceiver.messages.in`

- `SourceBufferPrivateDidReceiveInitializationSegment(WebKit::InitializationSegmentInfo segmentConfiguration) -> (Expected<void, WebCore::PlatformMediaError> result)`
- `TakeOwnershipOfMemory(WebCore::SharedMemory::Handle remoteData)`
- `SourceBufferPrivateHighestPresentationTimestampChanged(MediaTime timestamp)`
- `SourceBufferPrivateBufferedChanged(Vector<WebCore::PlatformTimeRanges> trackBuffers) -> ()`
- `SourceBufferPrivateDurationChanged(MediaTime duration) -> ()`
- `SourceBufferPrivateDidDropSample()`
- `SourceBufferPrivateDidReceiveRenderingError(int64_t errorCode)`
- `SourceBufferPrivateEvictionDataChanged(WebCore::SourceBufferEvictionData evictionData)`
- `SourceBufferPrivateDidAttach(WebKit::InitializationSegmentInfo segmentConfiguration) -> (Expected<void, WebCore::PlatformMediaError> result)`

## `GPUProcessProxy` - GPU -> UI

`UIProcess/GPU/GPUProcessProxy.messages.in`

- `DidCreateContextForVisibilityPropagation(WebKit::WebPageProxyIdentifier pageProxyID, WebCore::PageIdentifier pageID, WebKit::LayerHostingContextID contextID)` (if HAVE(VISIBILITY_PROPAGATION_VIEW))
- `SetHasVP9HardwareDecoder(bool hasVP9HardwareDecoder)` (if ENABLE(VP9))
- `SetHasAV1HardwareDecoder(bool hasAV1HardwareDecoder)` (if ENABLE(AV1))
- `VoiceActivityDetected()` (if ENABLE(MEDIA_STREAM))
- `StartMonitoringCaptureDeviceRotation(WebCore::PageIdentifier pageID, String devicePersistentId)` (if ENABLE(MEDIA_STREAM))
- `StopMonitoringCaptureDeviceRotation(WebCore::PageIdentifier pageID, String devicePersistentId)` (if ENABLE(MEDIA_STREAM))
- `MicrophoneMuteStatusChanged(bool isMuting)` (if ENABLE(MEDIA_STREAM))
- `StatusBarWasTapped() -> ()` (Async, if (ENABLE(MEDIA_STREAM) && PLATFORM(IOS_FAMILY)))
- `ProcessIsReadyToExit()`
- `TerminateWebProcess(WebCore::ProcessIdentifier webProcessIdentifier)`
- `DidDrawRemoteToPDF(WebCore::PageIdentifier pageID, RefPtr<WebCore::SharedBuffer> data, WebCore::SnapshotIdentifier snapshotIdentifier)` (if PLATFORM(COCOA))

## `LibWebRTCNetwork` - Networking -> WebContent

`WebProcess/Network/webrtc/LibWebRTCNetwork.messages.in`

- `SignalReadPacket(WebCore::LibWebRTCSocketIdentifier socketIdentifier, std::span<const uint8_t> data, WebKit::RTC::Network::IPAddress address, uint16_t port, int64_t timestamp, WebKit::RTC::Network::EcnMarking ecn)`
- `SignalSentPacket(WebCore::LibWebRTCSocketIdentifier socketIdentifier, int64_t rtcPacketID, int64_t timestamp)`
- `SignalAddressReady(WebCore::LibWebRTCSocketIdentifier socketIdentifier, WebKit::RTC::Network::SocketAddress address)`
- `SignalConnect(WebCore::LibWebRTCSocketIdentifier socketIdentifier)`
- `SignalClose(WebCore::LibWebRTCSocketIdentifier socketIdentifier, int error)`
- `SignalUsedInterface(WebCore::LibWebRTCSocketIdentifier socketIdentifier, String interfaceName)`

## `NetworkProcessConnection` - Networking -> WebContent

`WebProcess/Network/NetworkProcessConnection.messages.in`

- `DidCacheResource(WebCore::ResourceRequest request, WebCore::ShareableResourceHandle resource)` (if ENABLE(SHAREABLE_RESOURCE))
- `DidFinishPingLoad(WebCore::ResourceLoaderIdentifier pingLoadIdentifier, WebCore::ResourceError error, WebCore::ResourceResponse response)`
- `DidFinishPreconnection(WebCore::ResourceLoaderIdentifier preconnectionIdentifier, WebCore::ResourceError error)`
- `SetOnLineState(bool isOnLine)`
- `CookieAcceptPolicyChanged(WebCore::HTTPCookieAcceptPolicy policy)`
- `UpdateCachedCookiesEnabled()`
- `CookiesAdded(String host, Vector<WebCore::Cookie> cookies)` (if HAVE(COOKIE_CHANGE_LISTENER_API))
- `CookiesDeleted(String host, Vector<WebCore::Cookie> cookies)` (if HAVE(COOKIE_CHANGE_LISTENER_API))
- `AllCookiesDeleted()` (if HAVE(COOKIE_CHANGE_LISTENER_API))
- `ConnectToRTCDataChannelRemoteSource(WebCore::RTCDataChannelIdentifier source, WebCore::RTCDataChannelIdentifier handler) -> (std::optional<bool> result)` (if ENABLE(WEB_RTC))
- `MessagesAvailableForPort(WebCore::MessagePortIdentifier port)`
- `BroadcastConsoleMessage(JSC::MessageSource messageSource, JSC::MessageLevel messageLevel, String message)`
- `LoadCancelledDownloadRedirectRequestInFrame(WebCore::ResourceRequest request, WebCore::FrameIdentifier frameID, WebCore::PageIdentifier pageID)`

## `RTCDataChannelRemoteManager` - Networking -> WebContent

`WebProcess/Network/webrtc/RTCDataChannelRemoteManager.messages.in`

- `SendData(WebCore::RTCDataChannelIdentifier source, bool isRaw, std::span<const uint8_t> text)`
- `Close(WebCore::RTCDataChannelIdentifier source)`
- `ChangeReadyState(WebCore::RTCDataChannelIdentifier handler, WebCore::RTCDataChannelState state)`
- `ReceiveData(WebCore::RTCDataChannelIdentifier handler, bool isRaw, std::span<const uint8_t> data)`
- `DetectError(WebCore::RTCDataChannelIdentifier handler, WebCore::RTCErrorDetailType type, String message)`
- `BufferedAmountIsDecreasing(WebCore::RTCDataChannelIdentifier handler, size_t amount)`

## `StorageAreaMap` - Networking -> WebContent

`WebProcess/WebStorage/StorageAreaMap.messages.in`

- `DispatchStorageEvent(std::optional<WebKit::StorageAreaImplIdentifier> storageAreaImplID, String key, String oldValue, String newValue, String urlString, uint64_t messageIdentifier)`
- `ClearCache(uint64_t messageIdentifier)`

## `WebBroadcastChannelRegistry` - Networking -> WebContent

`WebProcess/WebCoreSupport/WebBroadcastChannelRegistry.messages.in`

- `PostMessageToRemote(WebCore::ClientOrigin origin, String name, WebCore::MessageWithMessagePorts message) -> ()`

## `WebFileSystemStorageConnection` - Networking -> WebContent

`WebProcess/WebCoreSupport/WebFileSystemStorageConnection.messages.in`

- `InvalidateAccessHandle(WebCore::FileSystemSyncAccessHandleIdentifier identifier)`

## `WebIDBConnectionToServer` - Networking -> WebContent

`WebProcess/Databases/IndexedDB/WebIDBConnectionToServer.messages.in`

- `DidDeleteDatabase(WebCore::IDBResultData result)`
- `DidOpenDatabase(WebCore::IDBResultData result)`
- `DidAbortTransaction(WebCore::IDBResourceIdentifier transactionIdentifier, WebCore::IDBError error)`
- `DidCommitTransaction(WebCore::IDBResourceIdentifier transactionIdentifier, WebCore::IDBError error)`
- `DidCreateObjectStore(WebCore::IDBResultData result)`
- `DidDeleteObjectStore(WebCore::IDBResultData result)`
- `DidRenameObjectStore(WebCore::IDBResultData result)`
- `DidClearObjectStore(WebCore::IDBResultData result)`
- `DidCreateIndex(WebCore::IDBResultData result)`
- `DidDeleteIndex(WebCore::IDBResultData result)`
- `DidRenameIndex(WebCore::IDBResultData result)`
- `DidPutOrAdd(WebCore::IDBResultData result)`
- `DidGetRecord(WebKit::WebIDBResult result)`
- `DidGetAllRecords(WebKit::WebIDBResult result)`
- `DidGetCount(WebCore::IDBResultData result)`
- `DidDeleteRecord(WebCore::IDBResultData result)`
- `DidOpenCursor(WebKit::WebIDBResult result)`
- `DidIterateCursor(WebKit::WebIDBResult result)`
- `FireVersionChangeEvent(WebCore::IDBDatabaseConnectionIdentifier databaseConnectionIdentifier, WebCore::IDBResourceIdentifier requestIdentifier, uint64_t requestedVersion)`
- `DidStartTransaction(WebCore::IDBResourceIdentifier transactionIdentifier, WebCore::IDBError error)`
- `DidCloseFromServer(WebCore::IDBDatabaseConnectionIdentifier databaseConnectionIdentifier, WebCore::IDBError error)` (final;)
- `NotifyOpenDBRequestBlocked(WebCore::IDBResourceIdentifier requestIdentifier, uint64_t oldVersion, uint64_t newVersion)`
- `DidGetAllDatabaseNamesAndVersions(WebCore::IDBResourceIdentifier requestIdentifier, Vector<WebCore::IDBDatabaseNameAndVersion> databases)`

## `WebRTCMonitor` - Networking -> WebContent

`WebProcess/Network/webrtc/WebRTCMonitor.messages.in`

- `NetworksChanged(Vector<WebKit::RTCNetwork> networks, WebKit::RTC::Network::IPAddress defaultIPV4Address, WebKit::RTC::Network::IPAddress defaultIPV6Address)`

## `WebRTCResolver` - Networking -> WebContent

`WebProcess/Network/webrtc/WebRTCResolver.messages.in`

- `SetResolvedAddress(Vector<WebKit::RTC::Network::IPAddress> addresses)`
- `ResolvedAddressError(int error)`

## `WebResourceLoader` - Networking -> WebContent

`WebProcess/Network/WebResourceLoader.messages.in`

- `WillSendRequest(WebCore::ResourceRequest request, IPC::FormDataReference requestBody, WebCore::ResourceResponse redirectResponse) -> (WebCore::ResourceRequest newRequest, bool isAllowedToAskUserForCredentials)`
- `SetWorkerStart(MonotonicTime value)`
- `DidSendData(uint64_t bytesSent, uint64_t totalBytesToBeSent)`
- `DidReceiveResponse(WebCore::ResourceResponse response, WebKit::PrivateRelayed privateRelayed, bool needsContinueDidReceiveResponseMessage, std::optional<WebCore::NetworkLoadMetrics> optionalNetworkLoadMetrics)`
- `DidReceiveData(IPC::SharedBufferReference data, uint64_t encodedDataLength)`
- `DidFinishResourceLoad(WebCore::NetworkLoadMetrics networkLoadMetrics)`
- `DidFailResourceLoad(WebCore::ResourceError error)`
- `DidFailServiceWorkerLoad(WebCore::ResourceError error)`
- `ServiceWorkerDidNotHandle()`
- `DidBlockAuthenticationChallenge()`
- `StopLoadingAfterXFrameOptionsOrContentSecurityPolicyDenied(WebCore::ResourceResponse response)`
- `DidReceiveResource(WebCore::ShareableResourceHandle resource)` (if ENABLE(SHAREABLE_RESOURCE))
- `ContentFilterDidBlockLoad(WebCore::ContentFilterUnblockHandler unblockHandler, String unblockRequestDeniedScript, WebCore::ResourceError error, URL blockedPageURL, WebCore::SubstituteData substituteData)` (if ENABLE(CONTENT_FILTERING))

## `WebSWClientConnection` - Networking -> WebContent

`WebProcess/Storage/WebSWClientConnection.messages.in`

- `JobRejectedInServer(WebCore::ServiceWorkerJobIdentifier jobDataIdentifier, WebCore::ExceptionData exception)`
- `RegistrationJobResolvedInServer(WebCore::ServiceWorkerJobIdentifier jobDataIdentifier, WebCore::ServiceWorkerRegistrationData registration, WebCore::ShouldNotifyWhenResolved shouldNotifyWhenResolved)`
- `StartScriptFetchForServer(WebCore::ServiceWorkerJobIdentifier jobDataIdentifier, WebCore::ServiceWorkerRegistrationKey registrationKey, WebCore::FetchOptionsCache cachePolicy)`
- `UpdateRegistrationState(WebCore::ServiceWorkerRegistrationIdentifier identifier, WebCore::ServiceWorkerRegistrationState state, std::optional<WebCore::ServiceWorkerData> serviceWorkerIdentifier)`
- `UpdateWorkerState(WebCore::ServiceWorkerIdentifier serviceWorkerIdentifier, WebCore::ServiceWorkerState state)`
- `FireUpdateFoundEvent(WebCore::ServiceWorkerRegistrationIdentifier identifier)`
- `SetRegistrationLastUpdateTime(WebCore::ServiceWorkerRegistrationIdentifier identifier, WallTime lastUpdateTime)`
- `SetRegistrationUpdateViaCache(WebCore::ServiceWorkerRegistrationIdentifier identifier, WebCore::ServiceWorkerUpdateViaCache updateViaCache)`
- `NotifyClientsOfControllerChange(HashSet<WebCore::ScriptExecutionContextIdentifier> contextIdentifiers, std::optional<WebCore::ServiceWorkerData> newController)`
- `UpdateBackgroundFetchRegistration(WebCore::BackgroundFetchInformation information)`
- `SetSWOriginTableIsImported()`
- `SetSWOriginTableSharedMemory(WebCore::SharedMemory::Handle handle)`
- `PostMessageToServiceWorkerClient(WebCore::ScriptExecutionContextIdentifier destinationContextIdentifier, WebCore::MessageWithMessagePorts message, WebCore::ServiceWorkerData source, String sourceOrigin)`
- `SetServiceWorkerClientIsControlled(WebCore::ScriptExecutionContextIdentifier workerIdentifier, WebCore::ServiceWorkerRegistrationData data) -> (bool isSuccess)`
- `FocusServiceWorkerClient(WebCore::ScriptExecutionContextIdentifier clientIdentifier) -> (std::optional<WebCore::ServiceWorkerClientData> result)`
- `NotifyRecordResponseBodyChunk(WebKit::RetrieveRecordResponseBodyCallbackIdentifier identifier, IPC::SharedBufferReference data)`
- `NotifyRecordResponseBodyEnd(WebKit::RetrieveRecordResponseBodyCallbackIdentifier identifier, WebCore::ResourceError error)`

## `WebSWContextManagerConnection` - Networking, UI -> WebContent

`WebProcess/Storage/WebSWContextManagerConnection.messages.in`

- `InstallServiceWorker(WebCore::ServiceWorkerContextData contextData, WebCore::ServiceWorkerData workerData, String userAgent, WebCore::WorkerThreadMode workerThreadMode, WebCore::ServiceWorkerIsInspectable inspectable, OptionSet<WebCore::AdvancedPrivacyProtections> protections)`
- `UpdateAppInitiatedValue(WebCore::ServiceWorkerIdentifier serviceWorkerIdentifier, WebCore::LastNavigationWasAppInitiated lastNavigationWasAppInitiated)`
- `StartFetch(WebCore::SWServerConnectionIdentifier serverConnectionIdentifier, WebCore::ServiceWorkerIdentifier serviceWorkerIdentifier, WebCore::FetchIdentifier fetchIdentifier, WebCore::ResourceRequest request, WebCore::FetchOptions options, IPC::FormDataReference requestBody, String referrer, bool isServiceWorkerNavigationPreloadEnabled, String clientIdentifier, String resutlingClientIdentifier)`
- `CancelFetch(WebCore::SWServerConnectionIdentifier serverConnectionIdentifier, WebCore::ServiceWorkerIdentifier serviceWorkerIdentifier, WebCore::FetchIdentifier fetchIdentifier)`
- `ContinueDidReceiveFetchResponse(WebCore::SWServerConnectionIdentifier serverConnectionIdentifier, WebCore::ServiceWorkerIdentifier serviceWorkerIdentifier, WebCore::FetchIdentifier fetchIdentifier)`
- `PostMessageToServiceWorker(WebCore::ServiceWorkerIdentifier destinationIdentifier, WebCore::MessageWithMessagePorts message, WebCore::ServiceWorkerOrClientData sourceData)`
- `FireInstallEvent(WebCore::ServiceWorkerIdentifier identifier)`
- `FireActivateEvent(WebCore::ServiceWorkerIdentifier identifier)`
- `FirePushEvent(WebCore::ServiceWorkerIdentifier identifier, std::optional<std::span<const uint8_t>> data, std::optional<WebCore::NotificationPayload> proposedPayload) -> (bool handled, std::optional<WebCore::NotificationPayload> resultPayload)`
- `FireNotificationEvent(WebCore::ServiceWorkerIdentifier identifier, WebCore::NotificationData data, WebCore::NotificationEventType type) -> (bool result)`
- `FireBackgroundFetchEvent(WebCore::ServiceWorkerIdentifier identifier, WebCore::BackgroundFetchInformation info) -> (bool result)`
- `FireBackgroundFetchClickEvent(WebCore::ServiceWorkerIdentifier identifier, WebCore::BackgroundFetchInformation info) -> (bool result)`
- `TerminateWorker(WebCore::ServiceWorkerIdentifier identifier)`
- `DidSaveScriptsToDisk(WebCore::ServiceWorkerIdentifier serviceWorkerIdentifier, WebCore::ScriptBuffer script, HashMap<URL, WebCore::ScriptBuffer> importedScripts)` (if ENABLE(SHAREABLE_RESOURCE) && PLATFORM(COCOA))
- `SetUserAgent(String userAgent)`
- `UpdatePreferencesStore(WebKit::WebPreferencesStore store)`
- `Close()`
- `SetThrottleState(bool isThrottleable)`
- `SetInspectable(WebCore::ServiceWorkerIsInspectable inspectable)`
- `ConvertFetchToDownload(WebCore::SWServerConnectionIdentifier serverConnectionIdentifier, WebCore::ServiceWorkerIdentifier serviceWorkerIdentifier, WebCore::FetchIdentifier identifier)`
- `NavigationPreloadIsReady(WebCore::SWServerConnectionIdentifier serverConnectionIdentifier, WebCore::ServiceWorkerIdentifier serviceWorkerIdentifier, WebCore::FetchIdentifier identifier, WebCore::ResourceResponse response)`
- `NavigationPreloadFailed(WebCore::SWServerConnectionIdentifier serverConnectionIdentifier, WebCore::ServiceWorkerIdentifier serviceWorkerIdentifier, WebCore::FetchIdentifier identifier, WebCore::ResourceError error)`
- `UpdateRegistrationState(WebCore::ServiceWorkerRegistrationIdentifier identifier, WebCore::ServiceWorkerRegistrationState state, std::optional<WebCore::ServiceWorkerData> serviceWorkerIdentifier)`
- `UpdateWorkerState(WebCore::ServiceWorkerIdentifier serviceWorkerIdentifier, WebCore::ServiceWorkerState state)`
- `FireUpdateFoundEvent(WebCore::ServiceWorkerRegistrationIdentifier identifier)`
- `SetRegistrationLastUpdateTime(WebCore::ServiceWorkerRegistrationIdentifier identifier, WallTime lastUpdateTime)`
- `SetRegistrationUpdateViaCache(WebCore::ServiceWorkerRegistrationIdentifier identifier, WebCore::ServiceWorkerUpdateViaCache updateViaCache)`

## `WebSharedWorkerObjectConnection` - Networking -> WebContent

`WebProcess/Storage/WebSharedWorkerObjectConnection.messages.in`

- `FetchScriptInClient(URL url, WebCore::SharedWorkerObjectIdentifier sharedWorkerObjectIdentifier, WebCore::WorkerOptions workerOptions) -> (WebCore::WorkerFetchResult fetchResult, WebCore::WorkerInitializationData initializationData)`
- `NotifyWorkerObjectOfLoadCompletion(WebCore::SharedWorkerObjectIdentifier sharedWorkerObjectIdentifier, WebCore::ResourceError error)`
- `PostErrorToWorkerObject(WebCore::SharedWorkerObjectIdentifier sharedWorkerObjectIdentifier, String errorMessage, int lineNumber, int columnNumber, String sourceURL, bool isErrorEvent)`

## `WebSocketChannel` - Networking -> WebContent

`WebProcess/Network/WebSocketChannel.messages.in`

- `DidConnect(String subprotocol, String extensions)`
- `DidClose(unsigned short code, String reason)`
- `DidReceiveText(String message)`
- `DidReceiveBinaryData(std::span<const uint8_t> data)`
- `DidReceiveMessageError(String errorMessage)`
- `DidSendHandshakeRequest(WebCore::ResourceRequest request)`
- `DidReceiveHandshakeResponse(WebCore::ResourceResponse response)`

## `WebTransportSession` - Networking -> WebContent

`WebProcess/Network/WebTransportSession.messages.in`

- `ReceiveDatagram(std::span<const uint8_t> datagram, bool withFin, std::optional<WebCore::Exception> exception)`
- `ReceiveIncomingUnidirectionalStream(WebCore::WebTransportStreamIdentifier identifier)`
- `ReceiveBidirectionalStream(WebCore::WebTransportStreamIdentifier identifier)`
- `StreamReceiveBytes(WebCore::WebTransportStreamIdentifier identifier, std::span<const uint8_t> bytes, bool withFin, std::optional<WebCore::Exception> exception)`

## `DownloadProxy` - Networking -> UI

`UIProcess/Downloads/DownloadProxy.messages.in`

- `DidStart(WebCore::ResourceRequest request, String suggestedFilename)`
- `DidReceiveAuthenticationChallenge(WebCore::AuthenticationChallenge challenge, WebKit::AuthenticationChallengeIdentifier challengeID)`
- `WillSendRequest(WebCore::ResourceRequest redirectRequest, WebCore::ResourceResponse redirectResponse) -> (WebCore::ResourceRequest newRequest)`
- `DecideDestinationWithSuggestedFilename(WebCore::ResourceResponse response, String suggestedFilename) -> (String filename, WebKit::SandboxExtensionHandle handle, WebKit::AllowOverwrite allowOverwrite, WebKit::UseDownloadPlaceholder useDownloadPlaceholder, URL alternatePlaceholderURL, WebKit::SandboxExtensionHandle placeholderSandboxExtensionHandle, std::span<const uint8_t> placeholderBookmarkData, std::span<const uint8_t> activityAccessToken)`
- `DidReceiveData(uint64_t bytesWritten, uint64_t totalBytesWritten, uint64_t totalBytesExpectedToWrite)`
- `DidCreateDestination(String path)`
- `DidFinish()`
- `DidFail(WebCore::ResourceError error, std::span<const uint8_t> resumeData)`
- `DidReceivePlaceholderURL(URL placeholderURL, std::span<const uint8_t> bookmarkData, WebKit::SandboxExtensionHandle handle) -> ()` (if HAVE(MODERN_DOWNLOADPROGRESS))
- `DidReceiveFinalURL(URL finalURL, std::span<const uint8_t> bookmarkData, WebKit::SandboxExtensionHandle handle)` (if HAVE(MODERN_DOWNLOADPROGRESS))
- `DidStartUpdatingProgress()` (if HAVE(MODERN_DOWNLOADPROGRESS))

## `LegacyCustomProtocolManagerProxy` - Networking -> UI

`UIProcess/Network/CustomProtocols/LegacyCustomProtocolManagerProxy.messages.in`

- `StartLoading(WebKit::LegacyCustomProtocolID customProtocolID, WebCore::ResourceRequest request)`
- `StopLoading(WebKit::LegacyCustomProtocolID customProtocolID)`

## `NetworkProcessProxy` - Networking -> UI

`UIProcess/Network/NetworkProcessProxy.messages.in`

- `DidReceiveAuthenticationChallenge(PAL::SessionID sessionID, WebKit::WebPageProxyIdentifier pageID, std::optional<WebCore::SecurityOriginData> topOrigin, WebCore::AuthenticationChallenge challenge, bool negotiatedLegacyTLS, WebKit::AuthenticationChallengeIdentifier challengeID)`
- `NegotiatedLegacyTLS(WebKit::WebPageProxyIdentifier pageID)`
- `DidNegotiateModernTLS(WebKit::WebPageProxyIdentifier pageID, URL url)`
- `DidBlockLoadToKnownTracker(WebKit::WebPageProxyIdentifier pageID, URL url)`
- `TestProcessIncomingSyncMessagesWhenWaitingForSyncReply(WebKit::WebPageProxyIdentifier pageID) -> (bool handled)` (sync)
- `ProcessHasUnresponseServiceWorker(WebCore::ProcessIdentifier processIdentifier)`
- `LogDiagnosticMessage(WebKit::WebPageProxyIdentifier pageID, String message, String description, WebCore::ShouldSample shouldSample)`
- `LogDiagnosticMessageWithResult(WebKit::WebPageProxyIdentifier pageID, String message, String description, uint32_t result, WebCore::ShouldSample shouldSample)`
- `LogDiagnosticMessageWithValue(WebKit::WebPageProxyIdentifier pageID, String message, String description, double value, unsigned significantFigures, WebCore::ShouldSample shouldSample)`
- `LogTestingEvent(PAL::SessionID sessionID, String event)`
- `RequestStorageAccessConfirm(WebKit::WebPageProxyIdentifier pageID, WebCore::FrameIdentifier frameID, WebCore::RegistrableDomain subFrameDomain, WebCore::RegistrableDomain topFrameDomain, std::optional<WebCore::OrganizationStorageAccessPromptQuirk> organizationStorageAccessPromptQuirk) -> (bool userDidGrantAccess)`
- `DeleteWebsiteDataInUIProcessForRegistrableDomains(PAL::SessionID sessionID, OptionSet<WebKit::WebsiteDataType> dataTypes, OptionSet<WebKit::WebsiteDataFetchOption> fetchOptions, Vector<WebCore::RegistrableDomain> domains) -> (HashSet<WebCore::RegistrableDomain> domainsWithMatchingDataRecords)`
- `DidCommitCrossSiteLoadWithDataTransferFromPrevalentResource(WebKit::WebPageProxyIdentifier pageID)`
- `SetDomainsWithUserInteraction(HashSet<WebCore::RegistrableDomain> domains)`
- `SetDomainsWithCrossPageStorageAccess(HashMap<WebCore::RegistrableDomain, Vector<WebCore::RegistrableDomain>> domains) -> ()`
- `ContentExtensionRules(WebKit::UserContentControllerIdentifier identifier)` (if ENABLE(CONTENT_EXTENSIONS))
- `TerminateWebProcess(WebCore::ProcessIdentifier webProcessIdentifier)`
- `StartServiceWorkerBackgroundProcessing(WebCore::ProcessIdentifier serviceWorkerProcessIdentifier)`
- `EndServiceWorkerBackgroundProcessing(WebCore::ProcessIdentifier serviceWorkerProcessIdentifier)`
- `RequestBackgroundFetchPermission(PAL::SessionID sessionID, WebCore::ClientOrigin origin) -> (bool result)`
- `NotifyBackgroundFetchChange(PAL::SessionID sessionID, String backgroundFetchIdentifier, WebKit::BackgroundFetchChange change)`
- `EstablishRemoteWorkerContextConnectionToNetworkProcess(WebKit::RemoteWorkerType workerType, WebCore::Site site, std::optional<WebCore::ProcessIdentifier> requestingProcessIdentifier, std::optional<WebCore::ScriptExecutionContextIdentifier> serviceWorkerPageIdentifier, PAL::SessionID sessionID) -> (std::optional<WebCore::ProcessIdentifier> remoteProcessIdentifier)`
- `RemoteWorkerContextConnectionNoLongerNeeded(WebKit::RemoteWorkerType workerType, WebCore::ProcessIdentifier identifier)`
- `RegisterRemoteWorkerClientProcess(WebKit::RemoteWorkerType workerType, WebCore::ProcessIdentifier clientProcessIdentifier, WebCore::ProcessIdentifier remoteWorkerProcessIdentifier)`
- `UnregisterRemoteWorkerClientProcess(WebKit::RemoteWorkerType workerType, WebCore::ProcessIdentifier clientProcessIdentifier, WebCore::ProcessIdentifier remoteWorkerProcessIdentifier)`
- `SetWebProcessHasUploads(WebCore::ProcessIdentifier processID, bool hasUpload)`
- `GetAppBoundDomains(PAL::SessionID sessionID) -> (HashSet<WebCore::RegistrableDomain> appBoundDomains)` (if ENABLE(APP_BOUND_DOMAINS))
- `IncreaseQuota(PAL::SessionID sessionID, WebCore::ClientOrigin origin, WebKit::QuotaIncreaseRequestIdentifier identifier, uint64_t quota, uint64_t currentSize, uint64_t spaceRequested)`
- `ResourceLoadDidSendRequest(WebKit::WebPageProxyIdentifier pageIdentifier, WebKit::ResourceLoadInfo resourceLoadInfo, WebCore::ResourceRequest request, std::optional<IPC::FormDataReference> httpBody)`
- `ResourceLoadDidPerformHTTPRedirection(WebKit::WebPageProxyIdentifier pageIdentifier, WebKit::ResourceLoadInfo resourceLoadInfo, WebCore::ResourceResponse resourceResponse, WebCore::ResourceRequest request)`
- `ResourceLoadDidReceiveChallenge(WebKit::WebPageProxyIdentifier pageIdentifier, WebKit::ResourceLoadInfo resourceLoadInfo, WebCore::AuthenticationChallenge challenge)`
- `ResourceLoadDidReceiveResponse(WebKit::WebPageProxyIdentifier pageIdentifier, WebKit::ResourceLoadInfo resourceLoadInfo, WebCore::ResourceResponse response)`
- `ResourceLoadDidCompleteWithError(WebKit::WebPageProxyIdentifier pageIdentifier, WebKit::ResourceLoadInfo resourceLoadInfo, WebCore::ResourceResponse response, WebCore::ResourceError error)`
- `DidAllowPrivateTokenUsageByThirdPartyForTesting(PAL::SessionID sessionID, bool wasAllowed, URL resourceURL)`
- `TriggerBrowsingContextGroupSwitchForNavigation(WebKit::WebPageProxyIdentifier pageIdentifier, WebCore::NavigationIdentifier navigationID, WebCore::BrowsingContextGroupSwitchDecision browsingContextGroupSwitchDecision, WebCore::Site responseSite, WebKit::NetworkResourceLoadIdentifier existingNetworkResourceLoadIdentifierToResume) -> (bool success)`
- `DidExceedMemoryLimit()` (if USE(SOUP))
- `GetWindowSceneAndBundleIdentifierForPaymentPresentation(WebKit::WebPageProxyIdentifier webPageProxyIdentifier) -> (String sceneIdentifier, String bundleIdentifier)` (if ENABLE(APPLE_PAY_REMOTE_UI_USES_SCENE))
- `GetPaymentCoordinatorEmbeddingUserAgent(WebKit::WebPageProxyIdentifier webPageProxyIdentifier) -> (String userAgent)` (if ENABLE(APPLE_PAY_REMOTE_UI))
- `DataTaskReceivedChallenge(WebKit::DataTaskIdentifier identifier, WebCore::AuthenticationChallenge challenge) -> (WebKit::AuthenticationChallengeDisposition disposition, WebCore::Credential credential)`
- `DataTaskWillPerformHTTPRedirection(WebKit::DataTaskIdentifier identifier, WebCore::ResourceResponse response, WebCore::ResourceRequest request) -> (bool allowed)`
- `DataTaskDidReceiveResponse(WebKit::DataTaskIdentifier identifier, WebCore::ResourceResponse response) -> (bool allowed)`
- `DataTaskDidReceiveData(WebKit::DataTaskIdentifier identifier, std::span<const uint8_t> data)`
- `DataTaskDidCompleteWithError(WebKit::DataTaskIdentifier identifier, WebCore::ResourceError error)`
- `OpenWindowFromServiceWorker(PAL::SessionID sessionID, String urlString, WebCore::SecurityOriginData serviceWorkerOrigin) -> (std::optional<WebCore::PageIdentifier> newPage)`
- `NavigateServiceWorkerClient(WebCore::FrameIdentifier frameIdentifier, WebCore::ScriptExecutionContextIdentifier documentIdentifier, URL url) -> (std::optional<WebCore::PageIdentifier> page, std::optional<WebCore::FrameIdentifier> frame)`
- `ReportConsoleMessage(PAL::SessionID sessionID, URL scriptURL, WebCore::SecurityOriginData serviceWorkerOrigin, JSC::MessageSource messageSource, JSC::MessageLevel messageLevel, String message, unsigned long requestIdentifier)`
- `CookiesDidChange(PAL::SessionID sessionID)`
- `DeleteWebsiteDataInWebProcessesForOrigin(OptionSet<WebKit::WebsiteDataType> websiteDataTypes, WebCore::ClientOrigin origin, PAL::SessionID sessionID, WebKit::WebPageProxyIdentifier webPageProxyID) -> ()`
- `ReloadExecutionContextsForOrigin(WebCore::ClientOrigin origin, PAL::SessionID sessionID, std::optional<WebCore::FrameIdentifier> triggeringFrame) -> ()`
- `WakeUpWebProcessForIPC(WebCore::ProcessIdentifier processIdentifier)` (if USE(RUNNINGBOARD))
- `ReportNetworkIssue(WebKit::WebPageProxyIdentifier webPageProxyIdentifier, URL requestURL)` (if ENABLE(NETWORK_ISSUE_REPORTING))

## `SecItemShimProxy` - Networking -> UI

`UIProcess/mac/SecItemShimProxy.messages.in`

- `SecItemRequestSync(WebKit::SecItemRequestData request) -> (std::optional<WebKit::SecItemResponseData> response)` (sync, if ENABLE(SEC_ITEM_SHIM))
- `SecItemRequest(WebKit::SecItemRequestData request) -> (std::optional<WebKit::SecItemResponseData> response)` (if ENABLE(SEC_ITEM_SHIM))

## `PushClientConnection` - Networking, UI -> webpushd

`webpushd/PushClientConnection.messages.in`

- `SetPushAndNotificationsEnabledForOrigin(String originString, bool enabled) -> ()`
- `GetPendingPushMessage() -> (std::optional<WebKit::WebPushMessage> message)`
- `GetPendingPushMessages() -> (Vector<WebKit::WebPushMessage> messages)`
- `InitializeConnection(WebKit::WebPushD::WebPushDaemonConnectionConfiguration configuration)`
- `InjectPushMessageForTesting(WebKit::WebPushD::PushMessageForTesting message) -> (String error)`
- `InjectEncryptedPushMessageForTesting(String encryptedMessage) -> (bool injected)`
- `SubscribeToPushService(URL scopeURL, Vector<uint8_t> vapidPublicKey) -> (Expected<WebCore::PushSubscriptionData, WebCore::ExceptionData> result)`
- `UnsubscribeFromPushService(URL scopeURL, std::optional<WebCore::PushSubscriptionIdentifier> identifier) -> (Expected<bool, WebCore::ExceptionData> result)`
- `GetPushSubscription(URL scopeURL) -> (Expected<std::optional<WebCore::PushSubscriptionData>, WebCore::ExceptionData> result)`
- `GetPushPermissionState(WebCore::SecurityOriginData origin) -> (WebCore::PushPermissionState result)`
- `IncrementSilentPushCount(WebCore::SecurityOriginData origin) -> (unsigned newCount)`
- `RemoveAllPushSubscriptions() -> (unsigned removed)`
- `RemovePushSubscriptionsForOrigin(WebCore::SecurityOriginData origin) -> (unsigned removed)`
- `SetPublicTokenForTesting(String token) -> ()`
- `GetPushTopicsForTesting() -> (Vector<String> enabled, Vector<String> ignored)`
- `ShowNotification(WebCore::NotificationData notificationData, RefPtr<WebCore::NotificationResources> notificationResources) -> ()`
- `GetNotifications(URL registrationURL, String tag) -> (Expected<Vector<WebCore::NotificationData>, WebCore::ExceptionData> result)`
- `CancelNotification(WebCore::SecurityOriginData origin, WTF::UUID notificationID)`
- `RequestPushPermission(WebCore::SecurityOriginData origin) -> (bool granted)`
- `SetAppBadge(WebCore::SecurityOriginData origin, std::optional<uint64_t> badge)`
- `GetAppBadgeForTesting() -> (std::optional<uint64_t> badge)`
- `SetProtocolVersionForTesting(unsigned version) -> ()`

## `ModelProcessConnection` - Model -> WebContent

`WebProcess/Model/ModelProcessConnection.messages.in`

- `DidInitialize(std::optional<WebKit::ModelProcessConnectionInfo> info)` (CanDispatchOutOfOrder)

## `ModelProcessModelPlayer` - Model -> WebContent

`WebProcess/Model/ModelProcessModelPlayer.messages.in`

- `DidCreateLayer(WebCore::LayerHostingContextIdentifier identifier)`
- `DidFinishLoading(WebCore::FloatPoint3D center, WebCore::FloatPoint3D extents)`
- `DidUpdateEntityTransform(WebCore::TransformationMatrix transform)`
- `DidUpdateAnimationPlaybackState(bool isPaused, double playbackRate, Seconds duration, Seconds currentTime, MonotonicTime clockTimestamp)`
- `DidFinishEnvironmentMapLoading(bool succeeded)`

## `ModelProcessProxy` - Model -> UI

`UIProcess/Model/ModelProcessProxy.messages.in`

- `TerminateWebProcess(WebCore::ProcessIdentifier webProcessIdentifier)`
- `DidCreateContextForVisibilityPropagation(WebKit::WebPageProxyIdentifier pageProxyID, WebCore::PageIdentifier pageID, WebKit::LayerHostingContextID contextID)` (if HAVE(VISIBILITY_PROPAGATION_VIEW))
- `ProcessIsReadyToExit()`
- `RequestSharedSimulationConnection(WebCore::ProcessIdentifier webProcessIdentifier) -> (std::optional<IPC::SharedFileHandle> sharedSimulationConnection)` (if PLATFORM(VISION) && ENABLE(GPU_PROCESS))

## `IPCConnectionTester` - test harness -> any process

`Shared/IPCConnectionTester.messages.in`

- `AsyncMessage(uint32_t value)`
- `SyncMessage(uint32_t value) -> (uint32_t sameValue)` (sync)

## `IPCStreamTester` - test harness -> any process

`Shared/IPCStreamTester.messages.in`

- `SyncMessage(uint32_t value) -> (uint32_t sameValue)` (sync)
- `SyncMessageNotStreamEncodableReply(uint32_t value) -> (uint32_t sameValue)` (NotStreamEncodableReply, sync)
- `SyncMessageNotStreamEncodableBoth(uint32_t value) -> (uint32_t sameValue)` (NotStreamEncodable, NotStreamEncodableReply, sync)
- `SyncMessageReturningSharedMemory1(uint32_t byteCount) -> (std::optional<WebCore::SharedMemory::Handle> handle)` (NotStreamEncodableReply, sync)
- `SyncMessageEmptyReply(uint32_t value) -> ()` (sync)
- `SyncCrashOnZero(int32_t value) -> (int32_t sameValue)` (sync)
- `CheckAutoreleasePool() -> (int32_t previousUseCount)` (sync)
- `AsyncPing(uint32_t value) -> (uint32_t nextValue)`
- `EmptyMessage()`

## `IPCStreamTesterProxy` - test harness -> any process

`Shared/IPCStreamTesterProxy.messages.in`

- `WasCreated(IPC::Semaphore streamWakeUpSemaphore, IPC::Semaphore streamClientWaitSemaphore)`

## `IPCTester` - test harness -> any process

`Shared/IPCTester.messages.in`

- `StartMessageTesting(String driverName)`
- `StopMessageTesting() -> ()` (sync)
- `CreateStreamTester(WebKit::IPCStreamTesterIdentifier identifier, IPC::StreamServerConnectionHandle serverConnection)`
- `ReleaseStreamTester(WebKit::IPCStreamTesterIdentifier identifier) -> ()` (sync)
- `CreateConnectionTester(WebKit::IPCConnectionTesterIdentifier identifier, IPC::ConnectionHandle connection)`
- `CreateConnectionTesterAndSendAsyncMessages(WebKit::IPCConnectionTesterIdentifier identifier, IPC::ConnectionHandle connection, uint32_t messageCount)`
- `ReleaseConnectionTester(WebKit::IPCConnectionTesterIdentifier identifier) -> ()` (sync)
- `SendSameSemaphoreBack(IPC::Semaphore semaphore)`
- `SendSemaphoreBackAndSignalProtocol(IPC::Semaphore semaphore)`
- `AsyncPing(uint32_t value) -> (uint32_t nextValue)`
- `SyncPing(uint32_t value) -> (uint32_t nextValue)` (sync)
- `SyncPingEmptyReply(uint32_t value) -> ()` (sync)
- `SendAsyncMessageToReceiver(uint32_t arg0)`
- `AsyncOptionalExceptionData(bool sendEngaged) -> (std::optional<WebCore::ExceptionData> exceptionData, String other)`

## `IPCTesterReceiver` - test harness -> any process

`Shared/IPCTesterReceiver.messages.in`

- `AsyncMessage(uint32_t arg1) -> (uint32_t reply)` (Asynchronous)
