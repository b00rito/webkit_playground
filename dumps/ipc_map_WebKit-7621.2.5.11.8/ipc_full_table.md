<details>
<summary><b>WebContent -> UI</b>: 36 interfaces, 780 messages</summary>

| Source | IPC interface (receiver) | Destination | Messages (sync) | Notes | Defined in |
|---|---|---|---|---|---|
| WebContent | `AcceleratedBackingStoreDMABuf` | UI | 4 (0) | non-Apple ports, observed send sites | `UIProcess/dmabuf/AcceleratedBackingStoreDMABuf.messages.in` |
| WebContent | `AudioSessionRoutingArbitratorProxy` | UI | 2 (0) |  | `UIProcess/Media/AudioSessionRoutingArbitratorProxy.messages.in` |
| WebContent | `DigitalCredentialsCoordinatorProxy` | UI | 2 (0) |  | `UIProcess/DigitalCredentials/DigitalCredentialsCoordinatorProxy.messages.in` |
| WebContent | `DrawingAreaProxy` | UI | 6 (0) |  | `UIProcess/DrawingAreaProxy.messages.in` |
| WebContent | `LogStream` | UI | 1 (0) | stream, manual: created in UIProcess/Cocoa/WebProcessProxyCocoa.mm; WebContent logs through it when logd is blocked | `Shared/LogStream.messages.in` |
| WebContent | `NotificationManagerMessageHandler` | UI | 9 (1) | manual: sent from WebProcess/; handled in UI and Networking (ExceptionForDispatchedTo on main), also to Networking | `Shared/Notifications/NotificationManagerMessageHandler.messages.in` |
| WebContent | `PlatformXRSystem` | UI | 7 (0) |  | `UIProcess/XR/PlatformXRSystem.messages.in` |
| WebContent | `PlaybackSessionManagerProxy` | UI | 24 (0) |  | `UIProcess/Cocoa/PlaybackSessionManagerProxy.messages.in` |
| WebContent | `RemoteLayerTreeDrawingAreaProxy` | UI | 5 (0) |  | `UIProcess/RemoteLayerTree/RemoteLayerTreeDrawingAreaProxy.messages.in` |
| WebContent | `RemoteMediaSessionCoordinatorProxy` | UI | 10 (0) |  | `UIProcess/Media/RemoteMediaSessionCoordinatorProxy.messages.in` |
| WebContent | `RemoteObjectRegistry` | UI | 3 (0) | manual: bidirectional UI <-> WebContent (injected-bundle remote objects), also from UI, also to WebContent | `Shared/API/Cocoa/RemoteObjectRegistry.messages.in` |
| WebContent | `RemoteWebInspectorUIProxy` | UI | 16 (0) |  | `UIProcess/Inspector/RemoteWebInspectorUIProxy.messages.in` |
| WebContent | `SmartMagnificationController` | UI | 2 (0) |  | `UIProcess/ios/SmartMagnificationController.messages.in` |
| WebContent | `SpeechRecognitionRemoteRealtimeMediaSourceManager` | UI | 4 (0) |  | `UIProcess/SpeechRecognitionRemoteRealtimeMediaSourceManager.messages.in` |
| WebContent | `SpeechRecognitionServer` | UI | 4 (0) |  | `UIProcess/SpeechRecognitionServer.messages.in` |
| WebContent | `VideoPresentationManagerProxy` | UI | 19 (0) |  | `UIProcess/Cocoa/VideoPresentationManagerProxy.messages.in` |
| WebContent | `ViewGestureController` | UI | 3 (0) |  | `UIProcess/ViewGestureController.messages.in` |
| WebContent | `VisitedLinkStore` | UI | 1 (0) |  | `UIProcess/VisitedLinkStore.messages.in` |
| WebContent | `WebAuthenticatorCoordinatorProxy` | UI | 6 (0) |  | `UIProcess/WebAuthentication/WebAuthenticatorCoordinatorProxy.messages.in` |
| WebContent | `WebAutomationSession` | UI | 1 (0) |  | `UIProcess/Automation/WebAutomationSession.messages.in` |
| WebContent | `WebDeviceOrientationUpdateProviderProxy` | UI | 4 (0) |  | `UIProcess/ios/WebDeviceOrientationUpdateProviderProxy.messages.in` |
| WebContent | `WebExtensionContext` | UI | 108 (0) |  | `UIProcess/Extensions/WebExtensionContext.messages.in` |
| WebContent | `WebExtensionController` | UI | 9 (0) |  | `UIProcess/Extensions/WebExtensionController.messages.in` |
| WebContent | `WebFullScreenManagerProxy` | UI | 6 (0) |  | `UIProcess/WebFullScreenManagerProxy.messages.in` |
| WebContent | `WebGeolocationManagerProxy` | UI | 3 (0) |  | `UIProcess/WebGeolocationManagerProxy.messages.in` |
| WebContent | `WebInspectorUIExtensionControllerProxy` | UI | 4 (0) |  | `UIProcess/Inspector/WebInspectorUIExtensionControllerProxy.messages.in` |
| WebContent | `WebInspectorUIProxy` | UI | 31 (0) |  | `UIProcess/Inspector/WebInspectorUIProxy.messages.in` |
| WebContent | `WebLockRegistryProxy` | UI | 5 (0) |  | `UIProcess/WebLockRegistryProxy.messages.in` |
| WebContent | `WebPageProxy` | UI | 375 (48) |  | `UIProcess/WebPageProxy.messages.in` |
| WebContent | `WebPasteboardProxy` | UI | 42 (33) |  | `UIProcess/WebPasteboardProxy.messages.in` |
| WebContent | `WebPaymentCoordinatorProxy` | UI | 15 (2) | manual: DispatchedFrom=WebContent; To=UI, or Networking when APPLE_PAY_REMOTE_UI (comment on main) | `Shared/ApplePay/WebPaymentCoordinatorProxy.messages.in` |
| WebContent | `WebPermissionControllerProxy` | UI | 1 (0) |  | `UIProcess/WebPermissionControllerProxy.messages.in` |
| WebContent | `WebProcessPool` | UI | 7 (1) |  | `UIProcess/WebProcessPool.messages.in` |
| WebContent | `WebProcessProxy` | UI | 36 (7) |  | `UIProcess/WebProcessProxy.messages.in` |
| WebContent | `WebScreenOrientationManagerProxy` | UI | 4 (1) |  | `UIProcess/WebScreenOrientationManagerProxy.messages.in` |
| WebContent | `WebUserContentControllerProxy` | UI | 1 (0) |  | `UIProcess/UserContent/WebUserContentControllerProxy.messages.in` |

</details>

<details>
<summary><b>WebContent -> GPU</b>: 64 interfaces, 845 messages</summary>

| Source | IPC interface (receiver) | Destination | Messages (sync) | Notes | Defined in |
|---|---|---|---|---|---|
| WebContent | `GPUConnectionToWebProcess` | GPU | 23 (1) |  | `GPUProcess/GPUConnectionToWebProcess.messages.in` |
| WebContent | `LibWebRTCCodecsProxy` | GPU | 15 (0) |  | `GPUProcess/webrtc/LibWebRTCCodecsProxy.messages.in` |
| WebContent | `RemoteAdapter` | GPU | 2 (1) | stream | `GPUProcess/graphics/WebGPU/RemoteAdapter.messages.in` |
| WebContent | `RemoteAudioDestinationManager` | GPU | 5 (0) |  | `GPUProcess/media/RemoteAudioDestinationManager.messages.in` |
| WebContent | `RemoteAudioMediaStreamTrackRendererInternalUnitManager` | GPU | 5 (0) |  | `GPUProcess/webrtc/RemoteAudioMediaStreamTrackRendererInternalUnitManager.messages.in` |
| WebContent | `RemoteAudioSessionProxy` | GPU | 10 (1) |  | `GPUProcess/media/RemoteAudioSessionProxy.messages.in` |
| WebContent | `RemoteBarcodeDetector` | GPU | 1 (0) | stream | `GPUProcess/ShapeDetection/RemoteBarcodeDetector.messages.in` |
| WebContent | `RemoteBindGroup` | GPU | 3 (1) | stream | `GPUProcess/graphics/WebGPU/RemoteBindGroup.messages.in` |
| WebContent | `RemoteBindGroupLayout` | GPU | 2 (0) | stream | `GPUProcess/graphics/WebGPU/RemoteBindGroupLayout.messages.in` |
| WebContent | `RemoteBuffer` | GPU | 7 (1) | stream | `GPUProcess/graphics/WebGPU/RemoteBuffer.messages.in` |
| WebContent | `RemoteCDMFactoryProxy` | GPU | 4 (2) |  | `GPUProcess/media/RemoteCDMFactoryProxy.messages.in` |
| WebContent | `RemoteCDMInstanceProxy` | GPU | 4 (1) |  | `GPUProcess/media/RemoteCDMInstanceProxy.messages.in` |
| WebContent | `RemoteCDMInstanceSessionProxy` | GPU | 7 (0) |  | `GPUProcess/media/RemoteCDMInstanceSessionProxy.messages.in` |
| WebContent | `RemoteCDMProxy` | GPU | 4 (1) |  | `GPUProcess/media/RemoteCDMProxy.messages.in` |
| WebContent | `RemoteCommandBuffer` | GPU | 2 (0) | stream | `GPUProcess/graphics/WebGPU/RemoteCommandBuffer.messages.in` |
| WebContent | `RemoteCommandEncoder` | GPU | 15 (0) | stream | `GPUProcess/graphics/WebGPU/RemoteCommandEncoder.messages.in` |
| WebContent | `RemoteCompositorIntegration` | GPU | 4 (3) | stream | `GPUProcess/graphics/WebGPU/RemoteCompositorIntegration.messages.in` |
| WebContent | `RemoteComputePassEncoder` | GPU | 10 (0) | stream | `GPUProcess/graphics/WebGPU/RemoteComputePassEncoder.messages.in` |
| WebContent | `RemoteComputePipeline` | GPU | 3 (0) | stream | `GPUProcess/graphics/WebGPU/RemoteComputePipeline.messages.in` |
| WebContent | `RemoteDevice` | GPU | 27 (0) | stream | `GPUProcess/graphics/WebGPU/RemoteDevice.messages.in` |
| WebContent | `RemoteDisplayListRecorder` | GPU | 77 (0) | stream | `GPUProcess/graphics/RemoteDisplayListRecorder.messages.in` |
| WebContent | `RemoteExternalTexture` | GPU | 4 (0) | stream | `GPUProcess/graphics/WebGPU/RemoteExternalTexture.messages.in` |
| WebContent | `RemoteFaceDetector` | GPU | 1 (0) | stream | `GPUProcess/ShapeDetection/RemoteFaceDetector.messages.in` |
| WebContent | `RemoteGPU` | GPU | 4 (2) | stream | `GPUProcess/graphics/WebGPU/RemoteGPU.messages.in` |
| WebContent | `RemoteGraphicsContextGL` | GPU | 295 (74) | stream | `GPUProcess/graphics/RemoteGraphicsContextGL.messages.in` |
| WebContent | `RemoteImageBuffer` | GPU | 10 (6) | stream | `GPUProcess/graphics/RemoteImageBuffer.messages.in` |
| WebContent | `RemoteImageBufferSet` | GPU | 3 (1) | stream | `GPUProcess/graphics/RemoteImageBufferSet.messages.in` |
| WebContent | `RemoteImageDecoderAVFProxy` | GPU | 6 (3) |  | `GPUProcess/media/RemoteImageDecoderAVFProxy.messages.in` |
| WebContent | `RemoteLegacyCDMFactoryProxy` | GPU | 3 (2) |  | `GPUProcess/media/RemoteLegacyCDMFactoryProxy.messages.in` |
| WebContent | `RemoteLegacyCDMProxy` | GPU | 3 (2) |  | `GPUProcess/media/RemoteLegacyCDMProxy.messages.in` |
| WebContent | `RemoteLegacyCDMSessionProxy` | GPU | 4 (3) |  | `GPUProcess/media/RemoteLegacyCDMSessionProxy.messages.in` |
| WebContent | `RemoteMediaEngineConfigurationFactoryProxy` | GPU | 2 (0) |  | `GPUProcess/media/RemoteMediaEngineConfigurationFactoryProxy.messages.in` |
| WebContent | `RemoteMediaPlayerManagerProxy` | GPU | 5 (3) |  | `GPUProcess/media/RemoteMediaPlayerManagerProxy.messages.in` |
| WebContent | `RemoteMediaPlayerProxy` | GPU | 70 (6) |  | `GPUProcess/media/RemoteMediaPlayerProxy.messages.in` |
| WebContent | `RemoteMediaRecorderPrivateWriterManager` | GPU | 6 (3) | observed send sites | `GPUProcess/media/RemoteMediaRecorderPrivateWriterManager.messages.in` |
| WebContent | `RemoteMediaResourceManager` | GPU | 7 (0) |  | `GPUProcess/media/RemoteMediaResourceManager.messages.in` |
| WebContent | `RemoteMediaSessionHelperProxy` | GPU | 3 (0) |  | `GPUProcess/media/ios/RemoteMediaSessionHelperProxy.messages.in` |
| WebContent | `RemoteMediaSourceProxy` | GPU | 8 (1) |  | `GPUProcess/media/RemoteMediaSourceProxy.messages.in` |
| WebContent | `RemotePipelineLayout` | GPU | 2 (0) | stream | `GPUProcess/graphics/WebGPU/RemotePipelineLayout.messages.in` |
| WebContent | `RemotePresentationContext` | GPU | 4 (0) | stream | `GPUProcess/graphics/WebGPU/RemotePresentationContext.messages.in` |
| WebContent | `RemoteQuerySet` | GPU | 3 (0) | stream | `GPUProcess/graphics/WebGPU/RemoteQuerySet.messages.in` |
| WebContent | `RemoteQueue` | GPU | 7 (0) | stream | `GPUProcess/graphics/WebGPU/RemoteQueue.messages.in` |
| WebContent | `RemoteRemoteCommandListenerProxy` | GPU | 1 (0) |  | `GPUProcess/media/RemoteRemoteCommandListenerProxy.messages.in` |
| WebContent | `RemoteRenderBundle` | GPU | 2 (0) | stream | `GPUProcess/graphics/WebGPU/RemoteRenderBundle.messages.in` |
| WebContent | `RemoteRenderBundleEncoder` | GPU | 15 (0) | stream | `GPUProcess/graphics/WebGPU/RemoteRenderBundleEncoder.messages.in` |
| WebContent | `RemoteRenderPassEncoder` | GPU | 22 (0) | stream | `GPUProcess/graphics/WebGPU/RemoteRenderPassEncoder.messages.in` |
| WebContent | `RemoteRenderPipeline` | GPU | 3 (0) | stream | `GPUProcess/graphics/WebGPU/RemoteRenderPipeline.messages.in` |
| WebContent | `RemoteRenderingBackend` | GPU | 30 (1) | stream | `GPUProcess/graphics/RemoteRenderingBackend.messages.in` |
| WebContent | `RemoteSampleBufferDisplayLayer` | GPU | 11 (0) |  | `GPUProcess/webrtc/RemoteSampleBufferDisplayLayer.messages.in` |
| WebContent | `RemoteSampleBufferDisplayLayerManager` | GPU | 2 (0) |  | `GPUProcess/webrtc/RemoteSampleBufferDisplayLayerManager.messages.in` |
| WebContent | `RemoteSampler` | GPU | 2 (0) | stream | `GPUProcess/graphics/WebGPU/RemoteSampler.messages.in` |
| WebContent | `RemoteShaderModule` | GPU | 3 (0) | stream | `GPUProcess/graphics/WebGPU/RemoteShaderModule.messages.in` |
| WebContent | `RemoteSharedResourceCache` | GPU | 1 (0) |  | `GPUProcess/RemoteSharedResourceCache.messages.in` |
| WebContent | `RemoteSourceBufferProxy` | GPU | 35 (3) |  | `GPUProcess/media/RemoteSourceBufferProxy.messages.in` |
| WebContent | `RemoteTextDetector` | GPU | 1 (0) | stream | `GPUProcess/ShapeDetection/RemoteTextDetector.messages.in` |
| WebContent | `RemoteTexture` | GPU | 5 (0) | stream | `GPUProcess/graphics/WebGPU/RemoteTexture.messages.in` |
| WebContent | `RemoteTextureView` | GPU | 2 (0) | stream | `GPUProcess/graphics/WebGPU/RemoteTextureView.messages.in` |
| WebContent | `RemoteVideoFrameObjectHeap` | GPU | 6 (2) |  | `GPUProcess/media/RemoteVideoFrameObjectHeap.messages.in` |
| WebContent | `RemoteWCLayerTreeHost` | GPU | 1 (0) | non-Apple ports, observed send sites | `GPUProcess/graphics/wc/RemoteWCLayerTreeHost.messages.in` |
| WebContent | `RemoteXRBinding` | GPU | 3 (0) | stream | `GPUProcess/graphics/WebGPU/RemoteXRBinding.messages.in` |
| WebContent | `RemoteXRProjectionLayer` | GPU | 3 (0) | stream | `GPUProcess/graphics/WebGPU/RemoteXRProjectionLayer.messages.in` |
| WebContent | `RemoteXRSubImage` | GPU | 3 (0) | stream | `GPUProcess/graphics/WebGPU/RemoteXRSubImage.messages.in` |
| WebContent | `RemoteXRView` | GPU | 1 (0) | stream | `GPUProcess/graphics/WebGPU/RemoteXRView.messages.in` |
| WebContent | `UserMediaCaptureManagerProxy` | GPU | 13 (1) |  | `UIProcess/Cocoa/UserMediaCaptureManagerProxy.messages.in` |

</details>

<details>
<summary><b>WebContent -> Networking</b>: 17 interfaces, 266 messages</summary>

| Source | IPC interface (receiver) | Destination | Messages (sync) | Notes | Defined in |
|---|---|---|---|---|---|
| WebContent | `NetworkBroadcastChannelRegistry` | Networking | 3 (0) |  | `NetworkProcess/NetworkBroadcastChannelRegistry.messages.in` |
| WebContent | `NetworkConnectionToWebProcess` | Networking | 86 (12) |  | `NetworkProcess/NetworkConnectionToWebProcess.messages.in` |
| WebContent | `NetworkMDNSRegister` | Networking | 2 (0) |  | `NetworkProcess/webrtc/NetworkMDNSRegister.messages.in` |
| WebContent | `NetworkRTCMonitor` | Networking | 2 (0) |  | `NetworkProcess/webrtc/NetworkRTCMonitor.messages.in` |
| WebContent | `NetworkRTCProvider` | Networking | 8 (0) |  | `NetworkProcess/webrtc/NetworkRTCProvider.messages.in` |
| WebContent | `NetworkResourceLoader` | Networking | 1 (0) |  | `NetworkProcess/NetworkResourceLoader.messages.in` |
| WebContent | `NetworkSocketChannel` | Networking | 3 (0) |  | `NetworkProcess/NetworkSocketChannel.messages.in` |
| WebContent | `NetworkStorageManager` | Networking | 66 (1) |  | `NetworkProcess/storage/NetworkStorageManager.messages.in` |
| WebContent | `NetworkTransportSession` | Networking | 8 (0) |  | `NetworkProcess/webtransport/NetworkTransportSession.messages.in` |
| WebContent | `NotificationManagerMessageHandler` | Networking | 9 (1) | manual: sent from WebProcess/; handled in UI and Networking (ExceptionForDispatchedTo on main), also to UI | `Shared/Notifications/NotificationManagerMessageHandler.messages.in` |
| WebContent | `RTCDataChannelRemoteManagerProxy` | Networking | 6 (0) |  | `NetworkProcess/webrtc/RTCDataChannelRemoteManagerProxy.messages.in` |
| WebContent | `ServiceWorkerDownloadTask` | Networking | 4 (0) |  | `NetworkProcess/ServiceWorker/ServiceWorkerDownloadTask.messages.in` |
| WebContent | `ServiceWorkerFetchTask` | Networking | 9 (0) |  | `NetworkProcess/ServiceWorker/ServiceWorkerFetchTask.messages.in` |
| WebContent | `WebSWServerConnection` | Networking | 35 (0) |  | `NetworkProcess/ServiceWorker/WebSWServerConnection.messages.in` |
| WebContent | `WebSWServerToContextConnection` | Networking | 18 (0) |  | `NetworkProcess/ServiceWorker/WebSWServerToContextConnection.messages.in` |
| WebContent | `WebSharedWorkerServerConnection` | Networking | 4 (0) |  | `NetworkProcess/SharedWorker/WebSharedWorkerServerConnection.messages.in` |
| WebContent | `WebSharedWorkerServerToContextConnection` | Networking | 2 (0) |  | `NetworkProcess/SharedWorker/WebSharedWorkerServerToContextConnection.messages.in` |

</details>

<details>
<summary><b>WebContent -> Model</b>: 3 interfaces, 17 messages</summary>

| Source | IPC interface (receiver) | Destination | Messages (sync) | Notes | Defined in |
|---|---|---|---|---|---|
| WebContent | `ModelConnectionToWebProcess` | Model | 3 (0) |  | `ModelProcess/ModelConnectionToWebProcess.messages.in` |
| WebContent | `ModelProcessModelPlayerManagerProxy` | Model | 2 (0) |  | `ModelProcess/ModelProcessModelPlayerManagerProxy.messages.in` |
| WebContent | `ModelProcessModelPlayerProxy` | Model | 12 (0) |  | `ModelProcess/cocoa/ModelProcessModelPlayerProxy.messages.in` |

</details>

<details>
<summary><b>UI -> WebContent</b>: 41 interfaces, 920 messages</summary>

| Source | IPC interface (receiver) | Destination | Messages (sync) | Notes | Defined in |
|---|---|---|---|---|---|
| UI | `AcceleratedSurfaceDMABuf` | WebContent | 2 (0) | non-Apple ports, observed send sites | `WebProcess/WebPage/dmabuf/AcceleratedSurfaceDMABuf.messages.in` |
| UI | `AuxiliaryProcess` | WebContent | 5 (0) | manual: received by every auxiliary process; sent only from UIProcess/, also to GPU, Networking, Model | `Shared/AuxiliaryProcess.messages.in` |
| UI | `DrawingArea` | WebContent | 14 (0) |  | `WebProcess/WebPage/DrawingArea.messages.in` |
| UI | `EventDispatcher` | WebContent | 6 (0) |  | `WebProcess/WebPage/EventDispatcher.messages.in` |
| UI | `PlatformXRSystemProxy` | WebContent | 2 (0) |  | `WebProcess/XR/PlatformXRSystemProxy.messages.in` |
| UI | `PlaybackSessionManager` | WebContent | 27 (0) |  | `WebProcess/cocoa/PlaybackSessionManager.messages.in` |
| UI | `RemoteMediaSessionCoordinator` | WebContent | 5 (0) |  | `WebProcess/MediaSession/RemoteMediaSessionCoordinator.messages.in` |
| UI | `RemoteObjectRegistry` | WebContent | 3 (0) | manual: bidirectional UI <-> WebContent (injected-bundle remote objects), also from WebContent, also to UI | `Shared/API/Cocoa/RemoteObjectRegistry.messages.in` |
| UI | `RemoteScrollingCoordinator` | WebContent | 9 (0) |  | `WebProcess/WebPage/RemoteLayerTree/RemoteScrollingCoordinator.messages.in` |
| UI | `RemoteWebInspectorUI` | WebContent | 6 (0) |  | `WebProcess/Inspector/RemoteWebInspectorUI.messages.in` |
| UI | `RemoteWebLockRegistry` | WebContent | 2 (0) |  | `WebProcess/WebCoreSupport/RemoteWebLockRegistry.messages.in` |
| UI | `SpeechRecognitionRealtimeMediaSourceManager` | WebContent | 4 (0) |  | `WebProcess/Speech/SpeechRecognitionRealtimeMediaSourceManager.messages.in` |
| UI | `SystemSettingsManager` | WebContent | 1 (0) | non-Apple ports, observed send sites | `WebProcess/glib/SystemSettingsManager.messages.in` |
| UI | `TextCheckingControllerProxy` | WebContent | 2 (0) |  | `WebProcess/WebPage/Cocoa/TextCheckingControllerProxy.messages.in` |
| UI | `UserMediaCaptureManager` | WebContent | 6 (0) | observed send sites | `WebProcess/cocoa/UserMediaCaptureManager.messages.in` |
| UI | `UserMediaCaptureManager` | WebContent | 2 (0) | non-Apple ports, observed send sites | `WebProcess/glib/UserMediaCaptureManager.messages.in` |
| UI | `VideoPresentationManager` | WebContent | 19 (0) |  | `WebProcess/cocoa/VideoPresentationManager.messages.in` |
| UI | `ViewGestureGeometryCollector` | WebContent | 3 (0) |  | `WebProcess/WebPage/ViewGestureGeometryCollector.messages.in` |
| UI | `ViewUpdateDispatcher` | WebContent | 1 (0) |  | `WebProcess/WebPage/ViewUpdateDispatcher.messages.in` |
| UI | `VisitedLinkTableController` | WebContent | 4 (0) |  | `WebProcess/WebPage/VisitedLinkTableController.messages.in` |
| UI | `WebAutomationSessionProxy` | WebContent | 14 (0) |  | `WebProcess/Automation/WebAutomationSessionProxy.messages.in` |
| UI | `WebDeviceOrientationUpdateProvider` | WebContent | 2 (0) |  | `WebProcess/WebCoreSupport/WebDeviceOrientationUpdateProvider.messages.in` |
| UI | `WebExtensionContextProxy` | WebContent | 42 (0) |  | `WebProcess/Extensions/WebExtensionContextProxy.messages.in` |
| UI | `WebExtensionControllerProxy` | WebContent | 2 (0) |  | `WebProcess/Extensions/WebExtensionControllerProxy.messages.in` |
| UI | `WebFullScreenManager` | WebContent | 10 (0) |  | `WebProcess/FullScreen/WebFullScreenManager.messages.in` |
| UI | `WebGeolocationManager` | WebContent | 3 (0) |  | `WebProcess/Geolocation/WebGeolocationManager.messages.in` |
| UI | `WebInspector` | WebContent | 11 (0) |  | `WebProcess/Inspector/WebInspector.messages.in` |
| UI | `WebInspectorInterruptDispatcher` | WebContent | 1 (0) |  | `WebProcess/Inspector/WebInspectorInterruptDispatcher.messages.in` |
| UI | `WebInspectorUI` | WebContent | 19 (0) | observed send sites | `WebProcess/Inspector/WebInspectorUI.messages.in` |
| UI | `WebInspectorUIExtensionController` | WebContent | 8 (0) |  | `WebProcess/Inspector/WebInspectorUIExtensionController.messages.in` |
| UI | `WebNotificationManager` | WebContent | 5 (0) | observed send sites | `WebProcess/Notifications/WebNotificationManager.messages.in` |
| UI | `WebPage` | WebContent | 501 (11) | also from Networking | `WebProcess/WebPage/WebPage.messages.in` |
| UI | `WebPageTesting` | WebContent | 10 (1) |  | `WebProcess/WebPage/WebPageTesting.messages.in` |
| UI | `WebPaymentCoordinator` | WebContent | 7 (0) |  | `WebProcess/ApplePay/WebPaymentCoordinator.messages.in` |
| UI | `WebPermissionController` | WebContent | 1 (0) |  | `WebProcess/WebCoreSupport/WebPermissionController.messages.in` |
| UI | `WebProcess` | WebContent | 109 (0) |  | `WebProcess/WebProcess.messages.in` |
| UI | `WebSWContextManagerConnection` | WebContent | 27 (0) | observed send sites, also from Networking | `WebProcess/Storage/WebSWContextManagerConnection.messages.in` |
| UI | `WebScreenOrientationManager` | WebContent | 1 (0) |  | `WebProcess/WebCoreSupport/WebScreenOrientationManager.messages.in` |
| UI | `WebSharedWorkerContextManagerConnection` | WebContent | 8 (0) |  | `WebProcess/Storage/WebSharedWorkerContextManagerConnection.messages.in` |
| UI | `WebSpeechRecognitionConnection` | WebContent | 1 (0) |  | `WebProcess/WebCoreSupport/WebSpeechRecognitionConnection.messages.in` |
| UI | `WebUserContentController` | WebContent | 15 (0) |  | `WebProcess/UserContent/WebUserContentController.messages.in` |

</details>

<details>
<summary><b>UI -> GPU</b>: 2 interfaces, 42 messages</summary>

| Source | IPC interface (receiver) | Destination | Messages (sync) | Notes | Defined in |
|---|---|---|---|---|---|
| UI | `AuxiliaryProcess` | GPU | 5 (0) | manual: received by every auxiliary process; sent only from UIProcess/, also to WebContent, Networking, Model | `Shared/AuxiliaryProcess.messages.in` |
| UI | `GPUProcess` | GPU | 37 (0) |  | `GPUProcess/GPUProcess.messages.in` |

</details>

<details>
<summary><b>UI -> Networking</b>: 6 interfaces, 210 messages</summary>

| Source | IPC interface (receiver) | Destination | Messages (sync) | Notes | Defined in |
|---|---|---|---|---|---|
| UI | `AuthenticationManager` | Networking | 1 (0) |  | `NetworkProcess/Authentication/AuthenticationManager.messages.in` |
| UI | `AuxiliaryProcess` | Networking | 5 (0) | manual: received by every auxiliary process; sent only from UIProcess/, also to WebContent, GPU, Model | `Shared/AuxiliaryProcess.messages.in` |
| UI | `LegacyCustomProtocolManager` | Networking | 7 (0) |  | `NetworkProcess/CustomProtocols/LegacyCustomProtocolManager.messages.in` |
| UI | `NetworkContentRuleListManager` | Networking | 4 (0) |  | `NetworkProcess/NetworkContentRuleListManager.messages.in` |
| UI | `NetworkProcess` | Networking | 178 (4) |  | `NetworkProcess/NetworkProcess.messages.in` |
| UI | `WebCookieManager` | Networking | 15 (0) |  | `NetworkProcess/Cookies/WebCookieManager.messages.in` |

</details>

<details>
<summary><b>UI -> Model</b>: 2 interfaces, 13 messages</summary>

| Source | IPC interface (receiver) | Destination | Messages (sync) | Notes | Defined in |
|---|---|---|---|---|---|
| UI | `AuxiliaryProcess` | Model | 5 (0) | manual: received by every auxiliary process; sent only from UIProcess/, also to WebContent, GPU, Networking | `Shared/AuxiliaryProcess.messages.in` |
| UI | `ModelProcess` | Model | 8 (0) |  | `ModelProcess/ModelProcess.messages.in` |

</details>

<details>
<summary><b>UI -> webpushd</b>: 1 interfaces, 22 messages</summary>

| Source | IPC interface (receiver) | Destination | Messages (sync) | Notes | Defined in |
|---|---|---|---|---|---|
| UI | `PushClientConnection` | webpushd | 22 (0) | observed send sites, also from Networking | `webpushd/PushClientConnection.messages.in` |

</details>

<details>
<summary><b>GPU -> WebContent</b>: 22 interfaces, 112 messages</summary>

| Source | IPC interface (receiver) | Destination | Messages (sync) | Notes | Defined in |
|---|---|---|---|---|---|
| GPU | `GPUProcessConnection` | WebContent | 5 (0) |  | `WebProcess/GPU/GPUProcessConnection.messages.in` |
| GPU | `LibWebRTCCodecs` | WebContent | 5 (0) |  | `WebProcess/GPU/webrtc/LibWebRTCCodecs.messages.in` |
| GPU | `MediaPlayerPrivateRemote` | WebContent | 49 (0) |  | `WebProcess/GPU/media/MediaPlayerPrivateRemote.messages.in` |
| GPU | `MediaSourcePrivateRemoteMessageReceiver` | WebContent | 2 (0) |  | `WebProcess/GPU/media/MediaSourcePrivateRemoteMessageReceiver.messages.in` |
| GPU | `RemoteAudioHardwareListener` | WebContent | 3 (0) |  | `WebProcess/GPU/media/RemoteAudioHardwareListener.messages.in` |
| GPU | `RemoteAudioSession` | WebContent | 3 (0) |  | `WebProcess/GPU/media/RemoteAudioSession.messages.in` |
| GPU | `RemoteAudioSourceProviderManager` | WebContent | 2 (0) |  | `WebProcess/GPU/media/RemoteAudioSourceProviderManager.messages.in` |
| GPU | `RemoteCDMInstance` | WebContent | 1 (0) |  | `WebProcess/GPU/media/RemoteCDMInstance.messages.in` |
| GPU | `RemoteCDMInstanceSession` | WebContent | 3 (0) |  | `WebProcess/GPU/media/RemoteCDMInstanceSession.messages.in` |
| GPU | `RemoteCaptureSampleManager` | WebContent | 3 (0) |  | `WebProcess/cocoa/RemoteCaptureSampleManager.messages.in` |
| GPU | `RemoteGPUProxy` | WebContent | 1 (0) |  | `WebProcess/GPU/graphics/WebGPU/RemoteGPUProxy.messages.in` |
| GPU | `RemoteGraphicsContextGLProxy` | WebContent | 3 (0) |  | `WebProcess/GPU/graphics/RemoteGraphicsContextGLProxy.messages.in` |
| GPU | `RemoteImageBufferProxy` | WebContent | 1 (0) |  | `WebProcess/GPU/graphics/RemoteImageBufferProxy.messages.in` |
| GPU | `RemoteImageBufferSetProxy` | WebContent | 1 (0) |  | `WebProcess/GPU/graphics/RemoteImageBufferSetProxy.messages.in` |
| GPU | `RemoteImageDecoderAVFManager` | WebContent | 1 (0) |  | `WebProcess/GPU/media/RemoteImageDecoderAVFManager.messages.in` |
| GPU | `RemoteLegacyCDMSession` | WebContent | 2 (0) |  | `WebProcess/GPU/media/RemoteLegacyCDMSession.messages.in` |
| GPU | `RemoteMediaSessionHelper` | WebContent | 9 (0) |  | `WebProcess/GPU/media/ios/RemoteMediaSessionHelper.messages.in` |
| GPU | `RemoteRemoteCommandListener` | WebContent | 1 (0) |  | `WebProcess/GPU/media/RemoteRemoteCommandListener.messages.in` |
| GPU | `RemoteRenderingBackendProxy` | WebContent | 3 (0) |  | `WebProcess/GPU/graphics/RemoteRenderingBackendProxy.messages.in` |
| GPU | `RemoteVideoFrameObjectHeapProxyProcessor` | WebContent | 4 (0) |  | `WebProcess/GPU/webrtc/RemoteVideoFrameObjectHeapProxyProcessor.messages.in` |
| GPU | `SampleBufferDisplayLayer` | WebContent | 1 (0) |  | `WebProcess/GPU/webrtc/SampleBufferDisplayLayer.messages.in` |
| GPU | `SourceBufferPrivateRemoteMessageReceiver` | WebContent | 9 (0) |  | `WebProcess/GPU/media/SourceBufferPrivateRemoteMessageReceiver.messages.in` |

</details>

<details>
<summary><b>GPU -> UI</b>: 1 interfaces, 11 messages</summary>

| Source | IPC interface (receiver) | Destination | Messages (sync) | Notes | Defined in |
|---|---|---|---|---|---|
| GPU | `GPUProcessProxy` | UI | 11 (0) |  | `UIProcess/GPU/GPUProcessProxy.messages.in` |

</details>

<details>
<summary><b>Networking -> WebContent</b>: 16 interfaces, 627 messages</summary>

| Source | IPC interface (receiver) | Destination | Messages (sync) | Notes | Defined in |
|---|---|---|---|---|---|
| Networking | `LibWebRTCNetwork` | WebContent | 6 (0) |  | `WebProcess/Network/webrtc/LibWebRTCNetwork.messages.in` |
| Networking | `NetworkProcessConnection` | WebContent | 13 (0) |  | `WebProcess/Network/NetworkProcessConnection.messages.in` |
| Networking | `RTCDataChannelRemoteManager` | WebContent | 6 (0) |  | `WebProcess/Network/webrtc/RTCDataChannelRemoteManager.messages.in` |
| Networking | `StorageAreaMap` | WebContent | 2 (0) |  | `WebProcess/WebStorage/StorageAreaMap.messages.in` |
| Networking | `WebBroadcastChannelRegistry` | WebContent | 1 (0) |  | `WebProcess/WebCoreSupport/WebBroadcastChannelRegistry.messages.in` |
| Networking | `WebFileSystemStorageConnection` | WebContent | 1 (0) |  | `WebProcess/WebCoreSupport/WebFileSystemStorageConnection.messages.in` |
| Networking | `WebIDBConnectionToServer` | WebContent | 23 (0) |  | `WebProcess/Databases/IndexedDB/WebIDBConnectionToServer.messages.in` |
| Networking | `WebPage` | WebContent | 501 (11) | also from UI | `WebProcess/WebPage/WebPage.messages.in` |
| Networking | `WebRTCMonitor` | WebContent | 1 (0) |  | `WebProcess/Network/webrtc/WebRTCMonitor.messages.in` |
| Networking | `WebRTCResolver` | WebContent | 2 (0) |  | `WebProcess/Network/webrtc/WebRTCResolver.messages.in` |
| Networking | `WebResourceLoader` | WebContent | 13 (0) |  | `WebProcess/Network/WebResourceLoader.messages.in` |
| Networking | `WebSWClientConnection` | WebContent | 17 (0) |  | `WebProcess/Storage/WebSWClientConnection.messages.in` |
| Networking | `WebSWContextManagerConnection` | WebContent | 27 (0) | observed send sites, also from UI | `WebProcess/Storage/WebSWContextManagerConnection.messages.in` |
| Networking | `WebSharedWorkerObjectConnection` | WebContent | 3 (0) |  | `WebProcess/Storage/WebSharedWorkerObjectConnection.messages.in` |
| Networking | `WebSocketChannel` | WebContent | 7 (0) |  | `WebProcess/Network/WebSocketChannel.messages.in` |
| Networking | `WebTransportSession` | WebContent | 4 (0) |  | `WebProcess/Network/WebTransportSession.messages.in` |

</details>

<details>
<summary><b>Networking -> UI</b>: 4 interfaces, 66 messages</summary>

| Source | IPC interface (receiver) | Destination | Messages (sync) | Notes | Defined in |
|---|---|---|---|---|---|
| Networking | `DownloadProxy` | UI | 11 (0) |  | `UIProcess/Downloads/DownloadProxy.messages.in` |
| Networking | `LegacyCustomProtocolManagerProxy` | UI | 2 (0) |  | `UIProcess/Network/CustomProtocols/LegacyCustomProtocolManagerProxy.messages.in` |
| Networking | `NetworkProcessProxy` | UI | 51 (1) |  | `UIProcess/Network/NetworkProcessProxy.messages.in` |
| Networking | `SecItemShimProxy` | UI | 2 (1) |  | `UIProcess/mac/SecItemShimProxy.messages.in` |

</details>

<details>
<summary><b>Networking -> webpushd</b>: 1 interfaces, 22 messages</summary>

| Source | IPC interface (receiver) | Destination | Messages (sync) | Notes | Defined in |
|---|---|---|---|---|---|
| Networking | `PushClientConnection` | webpushd | 22 (0) | observed send sites, also from UI | `webpushd/PushClientConnection.messages.in` |

</details>

<details>
<summary><b>Model -> WebContent</b>: 2 interfaces, 6 messages</summary>

| Source | IPC interface (receiver) | Destination | Messages (sync) | Notes | Defined in |
|---|---|---|---|---|---|
| Model | `ModelProcessConnection` | WebContent | 1 (0) |  | `WebProcess/Model/ModelProcessConnection.messages.in` |
| Model | `ModelProcessModelPlayer` | WebContent | 5 (0) |  | `WebProcess/Model/ModelProcessModelPlayer.messages.in` |

</details>

<details>
<summary><b>Model -> UI</b>: 1 interfaces, 4 messages</summary>

| Source | IPC interface (receiver) | Destination | Messages (sync) | Notes | Defined in |
|---|---|---|---|---|---|
| Model | `ModelProcessProxy` | UI | 4 (0) |  | `UIProcess/Model/ModelProcessProxy.messages.in` |

</details>

<details>
<summary><b>test harness -> any process</b>: 5 interfaces, 27 messages</summary>

| Source | IPC interface (receiver) | Destination | Messages (sync) | Notes | Defined in |
|---|---|---|---|---|---|
| test harness | `IPCConnectionTester` | any process | 2 (1) | testing only, manual: IPC testing API only | `Shared/IPCConnectionTester.messages.in` |
| test harness | `IPCStreamTester` | any process | 9 (7) | testing only, stream, manual: IPC testing API only | `Shared/IPCStreamTester.messages.in` |
| test harness | `IPCStreamTesterProxy` | any process | 1 (0) | testing only, manual: IPC testing API only | `Shared/IPCStreamTesterProxy.messages.in` |
| test harness | `IPCTester` | any process | 14 (5) | testing only, manual: IPC testing API only | `Shared/IPCTester.messages.in` |
| test harness | `IPCTesterReceiver` | any process | 1 (0) | testing only, manual: IPC testing API only | `Shared/IPCTesterReceiver.messages.in` |

</details>

