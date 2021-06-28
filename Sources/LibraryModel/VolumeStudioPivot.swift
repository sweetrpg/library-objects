//
// Created by paulyhedral on 6/25/21.
//

import Vapor
import Fluent


public final class VolumeStudioPivot : Model {
    public static let schema = "volume_studios"

    @ID
    public var id : UUID?

    @Parent(key: "volumeId")
    public var volume : Volume

    @Parent(key: "studioId")
    public var studio : Studio

    public init() {}

    public init(id : UUID? = nil, volume : Volume, studio : Studio) throws {
        self.id = id
        self.$volume.id = try volume.requireID()
        self.$studio.id = try studio.requireID()
    }

}
