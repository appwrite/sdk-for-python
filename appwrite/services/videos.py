from ..service import Service
from urllib.parse import quote
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.video_list import VideoList
from ..models.video import Video
from ..models.video_codec_list import VideoCodecList
from ..models.video_caption_list import VideoCaptionList
from ..models.video_caption import VideoCaption
from ..enums.video_output import VideoOutput
from ..models.video_rendition_list import VideoRenditionList
from ..models.video_rendition import VideoRendition
from ..enums.image_format import ImageFormat


class Videos(Service):

    def __init__(self, client) -> None:
        super(Videos, self).__init__(client)

    def list(
        self,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None,
    ) -> VideoList:
        """
        Get a list of videos in the current project. Sessions receive only videos they can read according to each video's `$permissions`. API keys and admins receive the full project catalog. Playback uses the same document read ACL plus the `videos.play` (or `videos.read`) scope: a guest can stream a video that grants `read("any")` or `read("guests")` even though guests lack `videos.read` and will not see it in this list.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: bucketId, fileId, name, size, format, duration, width, height, videoCodec, videoBitRate, audioCodec, audioBitRate, search
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        Returns
        -------
        VideoList
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/videos'
        api_params = {}
        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=VideoList)

    def create(
        self,
        video_id: str,
        bucket_id: str,
        file_id: str,
        name: Optional[str] = None,
        permissions: Optional[List[str]] = None,
    ) -> Video:
        """
        Create a video resource from an existing file in a storage bucket. The source file must be a video or audio file, and the caller must be able to read that file. Creating a video stores the document and queues timeline generation. The worker downloads the source, probes metadata, extracts embedded captions once, and deletes its working copy when finished. Sources with a video track also get a thumbnail timeline. Call create-rendition to package a streaming output.

        An optional `name` defaults to the source file name. An optional `permissions` array sets the video document ACL (list, get, update, delete, manage child resources, and playback). By default, only the current user is granted all permissions; API keys and admins create with empty permissions when omitted. Guests with `videos.play` can stream when the video grants them read (`read("any")` or `read("guests")`).

        Uploaded caption files stay listed alongside auto-extracted tracks for the same language; when the current default is an auto-extracted track with that code, the upload takes the default flag.

        Parameters
        ----------
        video_id : str
            Video ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        bucket_id : str
            Storage bucket unique ID holding the source file.
        file_id : str
            Source file unique ID.
        name : Optional[str]
            Video name. Defaults to the source file name. Max length: 2048 chars.
        permissions : Optional[List[str]]
            An array of permission strings. By default, only the current user is granted all permissions. [Learn more about permissions](https://appwrite.io/docs/permissions).
        Returns
        -------
        Video
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/videos'
        api_params = {}
        if video_id is None:
            raise AppwriteException('Missing required parameter: "video_id"')
        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')
        if file_id is None:
            raise AppwriteException('Missing required parameter: "file_id"')
        api_params['videoId'] = self._normalize_value(video_id)
        api_params['bucketId'] = self._normalize_value(bucket_id)
        api_params['fileId'] = self._normalize_value(file_id)
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if permissions is not None:
            api_params['permissions'] = self._normalize_value(permissions)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Video)

    def list_codecs(
        self,
    ) -> VideoCodecList:
        """
        Get a list of video encode codecs enabled on this instance. Each codec includes the output formats it may be packaged into.
        Returns
        -------
        VideoCodecList
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/videos/codecs'
        api_params = {}

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=VideoCodecList)

    def get(
        self,
        video_id: str,
    ) -> Video:
        """
        Get a video by its unique ID. This endpoint response returns a JSON object with the video metadata.

        Parameters
        ----------
        video_id : str
            Video unique ID.
        Returns
        -------
        Video
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/videos/{videoId}'
        api_params = {}
        if video_id is None or video_id == '':
            raise AppwriteException('Missing required parameter: "video_id"')
        api_path = api_path.replace('{videoId}', self._encode_path(video_id))

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Video)

    def update(
        self,
        video_id: str,
        name: Optional[str] = None,
        permissions: Optional[List[str]] = None,
    ) -> Video:
        """
        Update a video's name, permissions, or both. Only the fields you pass are changed: omit `name` to keep the current name and `permissions` to keep the current ACL. The caller must hold update permission on the video document. The source file cannot be replaced; delete the video and create a new one to point at a different file.

        Parameters
        ----------
        video_id : str
            Video unique ID.
        name : Optional[str]
            Video name. Max length: 2048 chars.
        permissions : Optional[List[str]]
            An array of permission strings. By default, the current permissions are inherited. [Learn more about permissions](https://appwrite.io/docs/permissions).
        Returns
        -------
        Video
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/videos/{videoId}'
        api_params = {}
        if video_id is None or video_id == '':
            raise AppwriteException('Missing required parameter: "video_id"')
        api_path = api_path.replace('{videoId}', self._encode_path(video_id))
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if permissions is not None:
            api_params['permissions'] = self._normalize_value(permissions)

        response = self.client.call(
            'patch',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Video)

    def delete(
        self,
        video_id: str,
    ) -> Dict[str, Any]:
        """
        Delete a video by its unique ID. This also removes every rendition, caption, preview and transcoded artifact derived from it. Fails with `video_rendition_in_progress` while a rendition is started or ended, unless that rendition has not been updated within the rendition retention window. Fails with `video_timeline_in_progress` while the video's timeline is being generated, unless the video has not been updated within the same window.

        Parameters
        ----------
        video_id : str
            Video unique ID.
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/videos/{videoId}'
        api_params = {}
        if video_id is None or video_id == '':
            raise AppwriteException('Missing required parameter: "video_id"')
        api_path = api_path.replace('{videoId}', self._encode_path(video_id))

        response = self.client.call(
            'delete',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return response

    def list_captions(
        self,
        video_id: str,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None,
    ) -> VideoCaptionList:
        """
        Get a list of all the caption tracks attached to a video. You can use the query params to filter your results.

        Parameters
        ----------
        video_id : str
            Video unique ID.
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, language, default, status, size, bucketId, fileId
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        Returns
        -------
        VideoCaptionList
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/videos/{videoId}/captions'
        api_params = {}
        if video_id is None or video_id == '':
            raise AppwriteException('Missing required parameter: "video_id"')
        api_path = api_path.replace('{videoId}', self._encode_path(video_id))
        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=VideoCaptionList)

    def create_caption(
        self,
        video_id: str,
        bucket_id: str,
        file_id: str,
        name: str,
        language: str,
        default: Optional[bool] = None,
    ) -> VideoCaption:
        """
        Add a caption track to a video from a WebVTT or SubRip file in a storage bucket. The file is normalised to WebVTT and segmented in the background. Subscribe to `videos.[videoId].captions.[captionId].update` for `started`, `ready`, and `error` status changes instead of only polling the caption document.

        Uploaded tracks are listed alongside auto-extracted embedded tracks (`embedded: true`). When the current default is an auto-extracted track for the same language code, the upload takes the default flag so players pick the authored file first. Auto-extracted tracks are never removed automatically — delete a track explicitly to remove it. Extraction runs once per video, so a deleted extracted track is not re-created.

        Parameters
        ----------
        video_id : str
            Video unique ID.
        bucket_id : str
            Storage bucket unique ID holding the caption file.
        file_id : str
            Caption file unique ID.
        name : str
            Caption display name. Allowed characters: a-z, A-Z, 0-9, space, and - . , ( ) _ '
        language : str
            Caption ISO 639-2 three-letter language code.
        default : Optional[bool]
            Make this the default caption track for the video.
        Returns
        -------
        VideoCaption
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/videos/{videoId}/captions'
        api_params = {}
        if video_id is None or video_id == '':
            raise AppwriteException('Missing required parameter: "video_id"')
        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')
        if file_id is None:
            raise AppwriteException('Missing required parameter: "file_id"')
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')
        if language is None:
            raise AppwriteException('Missing required parameter: "language"')
        api_path = api_path.replace('{videoId}', self._encode_path(video_id))
        api_params['bucketId'] = self._normalize_value(bucket_id)
        api_params['fileId'] = self._normalize_value(file_id)
        api_params['name'] = self._normalize_value(name)
        api_params['language'] = self._normalize_value(language)
        if default is not None:
            api_params['default'] = self._normalize_value(default)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=VideoCaption)

    def update_caption(
        self,
        video_id: str,
        caption_id: str,
        bucket_id: Optional[str] = None,
        file_id: Optional[str] = None,
        name: Optional[str] = None,
        language: Optional[str] = None,
        default: Optional[bool] = None,
    ) -> VideoCaption:
        """
        Update a caption track by its unique ID. Pass only `name`, `language`, and/or `default` to retag an extracted track (for example `und` → `heb` for Hebrew) without replacing the file. Changing `bucketId`/`fileId` re-packages the track in the background.

        Parameters
        ----------
        video_id : str
            Video unique ID.
        caption_id : str
            Caption unique ID.
        bucket_id : Optional[str]
            Storage bucket unique ID holding the caption file. Omit together with fileId to only update name, language, or default.
        file_id : Optional[str]
            Caption file unique ID. Omit together with bucketId to only update name, language, or default.
        name : Optional[str]
            Caption display name. Allowed characters: a-z, A-Z, 0-9, space, and - . , ( ) _ '
        language : Optional[str]
            Caption ISO 639-2 three-letter language code (for example `heb` for Hebrew).
        default : Optional[bool]
            Make this the default caption track for the video. Omit to leave unchanged.
        Returns
        -------
        VideoCaption
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/videos/{videoId}/captions/{captionId}'
        api_params = {}
        if video_id is None or video_id == '':
            raise AppwriteException('Missing required parameter: "video_id"')
        if caption_id is None or caption_id == '':
            raise AppwriteException('Missing required parameter: "caption_id"')
        api_path = api_path.replace('{videoId}', self._encode_path(video_id))
        api_path = api_path.replace('{captionId}', self._encode_path(caption_id))
        if bucket_id is not None:
            api_params['bucketId'] = self._normalize_value(bucket_id)
        if file_id is not None:
            api_params['fileId'] = self._normalize_value(file_id)
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if language is not None:
            api_params['language'] = self._normalize_value(language)
        if default is not None:
            api_params['default'] = self._normalize_value(default)

        response = self.client.call(
            'patch',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=VideoCaption)

    def delete_caption(
        self,
        video_id: str,
        caption_id: str,
    ) -> Dict[str, Any]:
        """
        Delete a caption track by its unique ID, along with its packaged segments.

        Parameters
        ----------
        video_id : str
            Video unique ID.
        caption_id : str
            Caption unique ID.
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/videos/{videoId}/captions/{captionId}'
        api_params = {}
        if video_id is None or video_id == '':
            raise AppwriteException('Missing required parameter: "video_id"')
        if caption_id is None or caption_id == '':
            raise AppwriteException('Missing required parameter: "caption_id"')
        api_path = api_path.replace('{videoId}', self._encode_path(video_id))
        api_path = api_path.replace('{captionId}', self._encode_path(caption_id))

        response = self.client.call(
            'delete',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return response

    def get_cmaf_hls_manifest(
        self,
        video_id: str,
    ) -> bytes:
        """
        Get the top-level streaming manifest for a video output: an HLS master playlist (`master.m3u8`) or a DASH MPD (`master.mpd`). Hand this URL to a player to begin adaptive playback.

        Guests can request this URL when they hold `videos.play` (or `videos.read`) **and** the video document grants them read. A video with `read("any")` or `read("guests")` is playable without a session.

        For CMAF renditions, use `getCmafHlsManifest` or `getCmafDashManifest`. Both masters point at the same fMP4 segment set.

        Parameters
        ----------
        video_id : str
            Video unique ID.
        Returns
        -------
        bytes
            Response as bytes

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/videos/{videoId}/outputs/cmaf/master.m3u8'
        api_params = {}
        if video_id is None or video_id == '':
            raise AppwriteException('Missing required parameter: "video_id"')
        api_path = api_path.replace('{videoId}', self._encode_path(video_id))

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': '*/*',
            },
            api_params,
        )

        return response

    def get_cmaf_dash_manifest(
        self,
        video_id: str,
    ) -> bytes:
        """
        Get the top-level streaming manifest for a video output: an HLS master playlist (`master.m3u8`) or a DASH MPD (`master.mpd`). Hand this URL to a player to begin adaptive playback.

        Guests can request this URL when they hold `videos.play` (or `videos.read`) **and** the video document grants them read. A video with `read("any")` or `read("guests")` is playable without a session.

        For CMAF renditions, use `getCmafHlsManifest` or `getCmafDashManifest`. Both masters point at the same fMP4 segment set.

        Parameters
        ----------
        video_id : str
            Video unique ID.
        Returns
        -------
        bytes
            Response as bytes

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/videos/{videoId}/outputs/cmaf/master.mpd'
        api_params = {}
        if video_id is None or video_id == '':
            raise AppwriteException('Missing required parameter: "video_id"')
        api_path = api_path.replace('{videoId}', self._encode_path(video_id))

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': '*/*',
            },
            api_params,
        )

        return response

    def get_dash_manifest(
        self,
        video_id: str,
    ) -> bytes:
        """
        Get the top-level streaming manifest for a video output: an HLS master playlist (`master.m3u8`) or a DASH MPD (`master.mpd`). Hand this URL to a player to begin adaptive playback.

        Guests can request this URL when they hold `videos.play` (or `videos.read`) **and** the video document grants them read. A video with `read("any")` or `read("guests")` is playable without a session.

        For CMAF renditions, use `getCmafHlsManifest` or `getCmafDashManifest`. Both masters point at the same fMP4 segment set.

        Parameters
        ----------
        video_id : str
            Video unique ID.
        Returns
        -------
        bytes
            Response as bytes

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/videos/{videoId}/outputs/dash/master.mpd'
        api_params = {}
        if video_id is None or video_id == '':
            raise AppwriteException('Missing required parameter: "video_id"')
        api_path = api_path.replace('{videoId}', self._encode_path(video_id))

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': '*/*',
            },
            api_params,
        )

        return response

    def get_hls_manifest(
        self,
        video_id: str,
    ) -> bytes:
        """
        Get the top-level streaming manifest for a video output: an HLS master playlist (`master.m3u8`) or a DASH MPD (`master.mpd`). Hand this URL to a player to begin adaptive playback.

        Guests can request this URL when they hold `videos.play` (or `videos.read`) **and** the video document grants them read. A video with `read("any")` or `read("guests")` is playable without a session.

        For CMAF renditions, use `getCmafHlsManifest` or `getCmafDashManifest`. Both masters point at the same fMP4 segment set.

        Parameters
        ----------
        video_id : str
            Video unique ID.
        Returns
        -------
        bytes
            Response as bytes

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/videos/{videoId}/outputs/hls/master.m3u8'
        api_params = {}
        if video_id is None or video_id == '':
            raise AppwriteException('Missing required parameter: "video_id"')
        api_path = api_path.replace('{videoId}', self._encode_path(video_id))

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': '*/*',
            },
            api_params,
        )

        return response

    def get_caption_manifest(
        self,
        video_id: str,
        output: VideoOutput,
        caption_id: str,
    ) -> bytes:
        """
        Get the playable caption resource for a video output: an HLS captions playlist, or the WebVTT file itself for DASH.

        Guests can request this URL when they hold `videos.play` (or `videos.read`) **and** the video document grants them read.

        Parameters
        ----------
        video_id : str
            Video unique ID.
        output : VideoOutput
            Streaming output format.
        caption_id : str
            Caption unique ID.
        Returns
        -------
        bytes
            Response as bytes

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/videos/{videoId}/outputs/{output}/captions/{captionId}/manifest'
        api_params = {}
        if video_id is None or video_id == '':
            raise AppwriteException('Missing required parameter: "video_id"')
        if output is None:
            raise AppwriteException('Missing required parameter: "output"')
        if caption_id is None or caption_id == '':
            raise AppwriteException('Missing required parameter: "caption_id"')
        api_path = api_path.replace('{videoId}', self._encode_path(video_id))
        api_path = api_path.replace('{output}', self._encode_path(output))
        api_path = api_path.replace('{captionId}', self._encode_path(caption_id))

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': '*/*',
            },
            api_params,
        )

        return response

    def list_renditions(
        self,
        video_id: str,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None,
    ) -> VideoRenditionList:
        """
        Get a list of all the renditions of a video. You can use the query params to filter your results.

        Parameters
        ----------
        video_id : str
            Video unique ID.
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: profileId, name, status, output, codec, width, height, videoBitRate, audioBitRate, size, startedAt, endedAt
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        Returns
        -------
        VideoRenditionList
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/videos/{videoId}/renditions'
        api_params = {}
        if video_id is None or video_id == '':
            raise AppwriteException('Missing required parameter: "video_id"')
        api_path = api_path.replace('{videoId}', self._encode_path(video_id))
        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=VideoRenditionList)

    def create_rendition(
        self,
        video_id: str,
        profile_id: str,
        output: VideoOutput,
    ) -> VideoRendition:
        """
        Request a new rendition of a video, encoded against a video profile and packaged for HLS, DASH, or CMAF. The rendition is created immediately with a `pending` status and transcoded in the background; poll it or subscribe to realtime events to follow its progress. The worker downloads the source file for this job, probes metadata and extracts embedded captions when needed, then deletes the working copy when the job ends.

        The profile codec must be enabled on this instance. A disabled codec fails with `video_codec_disabled`.

        Each video may have only one rendition per profile and output combination. Creating a duplicate fails with `video_rendition_already_exists`. After an encode fails or is aborted, delete the rendition and create it again. The same profile may still be encoded for different outputs (for example HLS and DASH).

        A video accepts 10 rendition creates per hour. The next create returns `general_rate_limit_exceeded`.

        CMAF packs shared fMP4 segments once and exposes both HLS (`/outputs/cmaf/master.m3u8`) and DASH (`/outputs/cmaf/master.mpd`) masters for the same encode.

        Renditions can only be created from the Console or a server SDK with an API key that has the `videos.write` scope. Each encode spends the project's compute, so client sessions receive `user_unauthorized`.

        Parameters
        ----------
        video_id : str
            Video unique ID.
        profile_id : str
            Video profile unique ID to encode against.
        output : VideoOutput
            Streaming output format to package as.
        Returns
        -------
        VideoRendition
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/videos/{videoId}/renditions'
        api_params = {}
        if video_id is None or video_id == '':
            raise AppwriteException('Missing required parameter: "video_id"')
        if profile_id is None:
            raise AppwriteException('Missing required parameter: "profile_id"')
        if output is None:
            raise AppwriteException('Missing required parameter: "output"')
        api_path = api_path.replace('{videoId}', self._encode_path(video_id))
        api_params['profileId'] = self._normalize_value(profile_id)
        api_params['output'] = self._normalize_value(output)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=VideoRendition)

    def get_rendition(
        self,
        video_id: str,
        rendition_id: str,
    ) -> VideoRendition:
        """
        Get a rendition by its unique ID, including its current transcoding status and progress.

        Parameters
        ----------
        video_id : str
            Video unique ID.
        rendition_id : str
            Rendition unique ID.
        Returns
        -------
        VideoRendition
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/videos/{videoId}/renditions/{renditionId}'
        api_params = {}
        if video_id is None or video_id == '':
            raise AppwriteException('Missing required parameter: "video_id"')
        if rendition_id is None or rendition_id == '':
            raise AppwriteException('Missing required parameter: "rendition_id"')
        api_path = api_path.replace('{videoId}', self._encode_path(video_id))
        api_path = api_path.replace('{renditionId}', self._encode_path(rendition_id))

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=VideoRendition)

    def delete_rendition(
        self,
        video_id: str,
        rendition_id: str,
    ) -> Dict[str, Any]:
        """
        Delete a rendition by its unique ID, along with its packaged segments and transcoded output. Fails with `video_rendition_in_progress` while the rendition is started or ended, unless it has not been updated within the rendition retention window.

        Parameters
        ----------
        video_id : str
            Video unique ID.
        rendition_id : str
            Rendition unique ID.
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/videos/{videoId}/renditions/{renditionId}'
        api_params = {}
        if video_id is None or video_id == '':
            raise AppwriteException('Missing required parameter: "video_id"')
        if rendition_id is None or rendition_id == '':
            raise AppwriteException('Missing required parameter: "rendition_id"')
        api_path = api_path.replace('{videoId}', self._encode_path(video_id))
        api_path = api_path.replace('{renditionId}', self._encode_path(rendition_id))

        response = self.client.call(
            'delete',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return response

    def get_thumbnail(
        self,
        video_id: str,
        thumbnail_id: str,
        width: Optional[float] = None,
        height: Optional[float] = None,
        output: Optional[ImageFormat] = None,
    ) -> bytes:
        """
        Get a single thumbnail sheet from a video's timeline as an image. You can resize the returned image and choose its output format.

        Guests can request this URL when they hold `videos.play` (or `videos.read`) **and** the video document grants them read.

        Parameters
        ----------
        video_id : str
            Video unique ID.
        thumbnail_id : str
            Thumbnail unique ID.
        width : Optional[float]
            Resize thumbnail image width, in pixels.
        height : Optional[float]
            Resize thumbnail image height, in pixels.
        output : Optional[ImageFormat]
            Output format type (jpeg, jpg, png, gif and webp).
        Returns
        -------
        bytes
            Response as bytes

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/videos/{videoId}/thumbnails/{thumbnailId}'
        api_params = {}
        if video_id is None or video_id == '':
            raise AppwriteException('Missing required parameter: "video_id"')
        if thumbnail_id is None or thumbnail_id == '':
            raise AppwriteException('Missing required parameter: "thumbnail_id"')
        api_path = api_path.replace('{videoId}', self._encode_path(video_id))
        api_path = api_path.replace('{thumbnailId}', self._encode_path(thumbnail_id))
        if width is not None:
            api_params['width'] = self._normalize_value(width)
        if height is not None:
            api_params['height'] = self._normalize_value(height)
        if output is not None:
            api_params['output'] = self._normalize_value(output)

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'image/*',
            },
            api_params,
        )

        return response

    def get_timeline(
        self,
        video_id: str,
    ) -> bytes:
        """
        Get the WebVTT thumbnail timeline for a video, used to render scrubbing thumbnails in a player. Timeline generation is queued when the video is created. Subscribe to `videos.[videoId].timelines.update` for probe and terminal updates, or poll this endpoint until it returns a WebVTT document. Audio-only sources produce no timeline and this endpoint returns `video_timelines_not_found`.

        Guests can request this URL when they hold `videos.play` (or `videos.read`) **and** the video document grants them read. A video with `read("any")` or `read("guests")` is playable without a session.

        Parameters
        ----------
        video_id : str
            Video unique ID.
        Returns
        -------
        bytes
            Response as bytes

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/videos/{videoId}/timeline'
        api_params = {}
        if video_id is None or video_id == '':
            raise AppwriteException('Missing required parameter: "video_id"')
        api_path = api_path.replace('{videoId}', self._encode_path(video_id))

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': '*/*',
            },
            api_params,
        )

        return response
