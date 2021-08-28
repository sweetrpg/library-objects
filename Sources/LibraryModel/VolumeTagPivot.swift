//
// Created by paulyhedral on 6/25/21.
//

import Vapor
import Fluent


public final class VolumeTagPivot : Model {
    public static let schema = "volume_tags"

    @ID
    public var id : UUID?

    @Parent(key: "volumeId")
    public var volume : Volume

    @Parent(key: "tagId")
    public var tag : Tag

    public init() {}

    public init(id : UUID? = nil, volume : Volume, tag : Tag) throws {
        self.id = id
        self.$volume.id = try volume.requireID()
        self.$tag.id = try tag.requireID()
    }

}
