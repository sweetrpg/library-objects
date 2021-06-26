//
// Created by paulyhedral on 6/25/21.
//

import Vapor
import Fluent


class VolumeStudioPivot : Model {
    static let schema = "volume_studios"

    @ID
    var id : UUID?

    @Parent(key: "volumeId")
    var volume : Volume

    @Parent(key: "studioId")
    var studio : Studio

    init() {}

    init(id : UUID? = nil, volume : Volume, studio : Studio) throws {
        self.id = id
        self.$volume.id = try volume.requireID()
        self.$studio.id = try studio.requireID()
    }

}
